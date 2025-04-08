import datetime
import uuid

from django.db import connections

from core.utils.database import Database
from core.utils.helpers import PositionType

COMPLEMENT_TYPE = 9
SEQUENCE_TYPE = 8


class CounterService:
    def __init__(self, db_alias='default'):
        self.connection = connections[db_alias]
        self.utils = Database()

    def get_counter(self, value):
        """
        Retorna os dados das tabelas ACODNUM.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                (
                    'SELECT CODNUM_0, NIVDEF_0, NIVRAZ_0, TYP_0, NBPOS_0, POSTYP_0, POSTYP_1, POSTYP_2, '
                    'POSTYP_3, POSTYP_4, POSTYP_5, POSTYP_6, POSTYP_7, POSTYP_8, POSTYP_9, POSLNG_0, '
                    'POSLNG_1, POSLNG_2, POSLNG_3, POSLNG_4, POSLNG_5, POSLNG_6, POSLNG_7, POSLNG_8, '
                    'POSCTE_0, POSCTE_1, POSCTE_2, POSCTE_3, POSCTE_4, POSCTE_5, POSCTE_6, POSCTE_7, '
                    'POSCTE_8, POSCTE_9, CTLCHR_0, ZERO_0, SEQ_0, SEQTBL_0, SEQABR_0, SEQNBR_0, LEG_0 '
                    'FROM ACODNUM WHERE CODNUM_0 = %s'
                ),
                [value],
            )
            acodnum = self.utils._fetch_all_as_dicts(cursor)

        return acodnum

    def get_sequence(self, counter, site, period, complement):
        """
        Retorna os dados da tabela AVALNUM para o contador e o site especificados.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                (
                    'SELECT CODNUM_0, SITE_0, PERIODE_0, COMP_0, VALEUR_0 '
                    'FROM AVALNUM '
                    'WHERE CODNUM_0 = %s AND SITE_0 = %s AND PERIODE_0 = %s AND COMP_0 = %s'
                ),
                [counter, site, period, complement],
            )
            avalnum = self.utils._fetch_all_as_dicts(cursor)

        return avalnum

    def get_full_counters(self, value):
        """
        Retorna uma lista com os dados de ACODNUM e seus AVALNUMs vinculados.
        Exemplo de retorno:
        [
            {
                ... dados do ACODNUM ...,
                'avalnum': [ {dados do avalnum 1}, {avalnum 2}, ... ]
            },
            ...
        ]
        """

        dados = self.get_counters(value)
        acodnum = dados['acodnum']
        avalnum_map = {}

        for a in dados['avalnum']:
            key = a['CODNUM_0']
            avalnum_map.setdefault(key, []).append(a)

        for ac in acodnum:
            ac['avalnum'] = avalnum_map.get(ac['CODNUM_0'], [])

        return acodnum

    def is_complement(self, field_values):
        """
        Verifica se o número é um complemento.
        """
        for key, value in field_values:
            if key.startswith('POSTYP_'):
                if value == COMPLEMENT_TYPE:
                    return True

        return False

    def exist_sequence(self, field_value):
        """
        Verifica se existe uma sequência no contador.
        """
        for key, value in field_value:
            if key.startswith('POSTYP_'):
                if value == SEQUENCE_TYPE:
                    return True

        return False

    @staticmethod
    def _get_period(field_value, date):
        """
        Estabelece o período do contador
        """
        current_date = datetime.datetime.now()

        if field_value == 2:  # noqa: PLR2004
            return current_date.year % 100
        elif field_value == 3:  # noqa: PLR2004
            return 100 * (current_date.year % 100) + current_date.month

        return 0

    def _get_constant_segment(self, counter, index):
        key = f'POSCTE_{index}'
        return counter.get(key, '')

    def _get_year_segment(self, counter, index, current_date):
        size_key = f'POSLNG_{index}'
        size = counter.get(size_key, 0)
        if size == 1:
            return str(current_date.year % 10)
        if size == 2:
            return f'{current_date.year % 100:02d}'
        if size == 4:
            return f'{current_date.year:04d}'
        print(f'Aviso: Tamanho de ano inválido ({size}) para índice {index}')
        return ''

    def _get_month_segment(self, counter, index, current_date):
        size_key = f'POSLNG_{index}'
        size = counter.get(size_key, 0)
        if size == 2:
            return f'{current_date.month:02d}'
        if size == 3:
            # Idealmente, locale configurado globalmente
            # try: locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
            # except locale.Error: print("Aviso: Locale não definido.")
            return current_date.strftime('%b').upper()
        print(f'Aviso: Tamanho de mês inválido ({size}) para índice {index}')
        return ''

    def _get_week_number_segment(self, current_date):
        return current_date.strftime('%W')

    def _get_day_segment(self, counter, index, current_date):
        size_key = f'POSLNG_{index}'
        size = counter.get(size_key, 0)
        if size == 1:
            return str(current_date.isoweekday())  # Seg=1..Dom=7
        if size == 2:
            return f'{current_date.day:02d}'
        if size == 4:
            return current_date.strftime('%j')  # Dia do ano (001-366)
        print(f'Aviso: Tamanho de dia inválido ({size}) para índice {index}')
        return ''

    def _get_sequence_segment(self, counter, index, sequence_number, max_value):
        # TODO: Lógica de max_value/status
        size_key = f'POSLNG_{index}'
        size = counter.get(size_key, 0)
        if size <= 0:
            print(f'Aviso: Tamanho de sequência inválido ({size}) para índice {index}')
            return ''
        return f'{sequence_number:0{size}d}'

    def _get_complement_segment(self, counter, index, sequence_number, max_value):
        if sequence_number > max_value:
            status = 2

        size_key = f'POSLNG_{index}'
        size = counter.get(size_key, 0)
        if size <= 0:
            print(f'Aviso: Tamanho de sequência inválido ou zero ({size}) para índice {index}')
            return ''  # Ou talvez retornar o número sem padding?

        return f'{sequence_number:0{size}d}', status

    def assigns_counter_value(self, sequence_number, counter, date, complement, max_value):  # noqa: PLR0912
        """
        Atribui o valor do contador.
        """
        if not isinstance(date, (datetime.date, datetime.datetime)):
            raise TypeError("O parâmetro 'date' deve ser um objeto date ou datetime.")
        # Garante que temos um objeto date para consistência nos cálculos
        current_date = date.date() if isinstance(date, datetime.datetime) else date

        # Mapeia o tipo da posição (valor numérico) para a função handler correspondente
        handler_map = {
            PositionType.CONSTANT: self._get_constant_segment,
            PositionType.YEAR: self._get_year_segment,
            PositionType.MONTH: self._get_month_segment,
            PositionType.WEEK_NUM_MON: self._get_week_number_segment,
            PositionType.DAY: self._get_day_segment,
            PositionType.SEQUENCE: self._get_sequence_segment,
            PositionType.COMPLEMENT: self._get_complement_segment,
        }

        counter_value_parts = []
        num_positions = counter.get('NBPOS_0', 0)  # Número total de posições

        for i in range(num_positions):
            pos_type_key = f'POSTYP_{i}'
            pos_type_value = counter.get(pos_type_key)

            segment = ''
            pos_type_enum = None

            if pos_type_value is not None:
                try:
                    pos_type_enum = PositionType(pos_type_value)
                except ValueError:
                    print(f'Aviso: Valor de tipo de posição inválido ({pos_type_value}) para índice {i}')
                    segment = f'[TIPO INVÁLIDO {pos_type_value}]'

            if pos_type_enum:
                handler = handler_map.get(pos_type_enum)

                if handler:
                    # Chama o handler apropriado, passando os argumentos necessários
                    # Usando try-except genérico ou mais específico se souber os args exatos
                    try:
                        if pos_type_enum == PositionType.CONSTANT:
                            segment = handler(counter, i)
                        elif pos_type_enum == PositionType.YEAR:
                            segment = handler(counter, i, current_date)
                        elif pos_type_enum == PositionType.MONTH:
                            segment = handler(counter, i, current_date)
                        elif pos_type_enum == PositionType.WEEK_NUM_MON:
                            segment = handler(current_date)
                        elif pos_type_enum == PositionType.DAY:
                            segment = handler(counter, i, current_date)
                        elif pos_type_enum == PositionType.SEQUENCE:
                            segment = handler(counter, i, sequence_number, max_value)
                        elif pos_type_enum == PositionType.COMPLEMENT:
                            segment = handler(counter, i, complement)
                    except Exception as e:
                        print(f'Erro ao processar posição {i} (Tipo: {pos_type_enum.name}): {e}')
                        segment = f'[ERRO TIPO {pos_type_enum.name}]'
                else:
                    # Caso um tipo válido exista no Enum mas não no handler_map
                    print(f'Aviso: Handler não definido para o tipo de posição {pos_type_enum.name} (índice {i})')
                    segment = f'[NO HANDLER {pos_type_enum.name}]'

            elif not segment:  # Se não houve erro de conversão mas pos_type_value era None
                print(f'Aviso: Tipo de posição não encontrado (chave: {pos_type_key})')
                segment = '[TIPO AUSENTE]'

            counter_value_parts.append(str(segment))  # Garante que é string

        return ''.join(counter_value_parts)

        # counter_value = ''
        # current_date = date

        # limit = range(counter['NBPOS_0'])

        # for i in limit:
        #     for key, value in counter.items():
        #         if key.startswith('POSTYP_'):
        #             if value == 1:
        #                 counter_value += counter['POSCTE_' + str(i)]
        #             elif value == 2:  # noqa: PLR2004
        #                 size = counter['POSLNG_' + str(i)]

        #                 if size == 1:
        #                     period = current_date.year % 10
        #                     counter_value += str(period)
        #                 elif size == 2:  # noqa: PLR2004
        #                     period = current_date.year % 100
        #                     counter_value += f'{period:02}'
        #                 elif size == 4:  # noqa: PLR2004
        #                     period = current_date.year
        #                     counter_value += f'{period:04}'
        #             elif value == 3:  # noqa: PLR2004
        #                 size = counter['POSLNG_' + str(i)]
        #                 if size == 2:  # noqa: PLR2004
        #                     period = current_date.month
        #                     counter_value += f'{period:02}'
        #                 elif size == 3:  # noqa: PLR2004
        #                     counter_value += current_date.strftime('%b').upper()
        #             elif value == 4:  # noqa: PLR2004
        #                 counter_value += current_date.strftime('%W')
        #             elif value == 5:  # noqa: PLR2004
        #                 size = counter['POSLNG_' + str(i)]

        #                 if size == 1:
        #                     counter_value += str(current_date.weekday() + 1)
        #                 elif size == 2:  # noqa: PLR2004
        #                     counter_value += str(current_date.day)
        #                 elif size == 4:  # noqa: PLR2004
        #                     initial_date = f'01/01/{current_date.year}'
        #                     initial_date = datetime.datetime.strptime(initial_date, '%d/%m/%Y').date()
        #                     period = calculate_number_of_days(current_date, initial_date)
        #                     counter_value += f'{period:03}'
        #             elif value == 8:  # noqa: PLR2004
        #                 if sequence_number > max_value:
        #                     status = 2

        #                 size = counter['POSLNG_' + str(i)]
        #                 counter_value += f'{sequence_number:0{size}d}'
        #             elif value == 9:  # noqa: PLR2004
        #                 size = counter['POSLNG_' + str(i)]

        #                 if size == 0:
        #                     if len(complement) > 0 and counter['CTLCHR_0'] == 2:
        #                         status = 4

        #                     counter_value += complement
        #                 else:
        #                     if len(complement) < size and counter['CTLCHR_0'] == 2:
        #                         status = 4

        #                     counter_value += complement[:size]

        # return counter_value

    def generate_number(self, compteur, _site, date, complement):
        counter = CounterService().get_counter(compteur)

        if not counter:
            pass

        counter = counter[0]

        if not self.exist_sequence(counter.items()):
            return None, 4

        if self.is_complement(counter.items()):
            comp = ''
        else:
            comp = complement

        period = self._get_period(counter['NIVRAZ_0'], date)

        # if not _site:
        #     if counter['NIVDEF_0'] > 1:
        #         return None, 5

        # if counter['NIVDEF_0'] == 1:
        #     site = None
        # elif counter['NIVDEF_0'] == 2:  # noqa: PLR2004
        #     company = Group.objects.filter(site=site).first()
        #     site = company.code if company else None

        # Calcula valor do contador
        max_value = int(('9' * counter['NBPOS_0']))
        sequence_number = 0

        available_sequence = self.get_sequence(compteur, _site, period, comp)

        if available_sequence:
            create_record = False
            sequence_number = available_sequence[0]['VALEUR_0']
            sequence_number += 1
        else:
            create_record = True
            sequence_number = 1

        # Atualiza o contador
        if create_record:
            uuid_bytes = uuid.uuid4().bytes

            if comp is None:
                comp = ''

            if period is None:
                period = 0

            if _site is None:
                _site = ''

            Database().insert_into_table(
                'AVALNUM',
                {
                    'UPDTICK_0': 1,
                    'CODNUM_0': compteur,
                    'SITE_0': _site,
                    'PERIODE_0': period,
                    'COMP_0': comp,
                    'VALEUR_0': sequence_number,
                    'AUUID_0': uuid_bytes,
                    'CREUSR_0': 'INTER',
                    'UPDUSR_0': 'INTER',
                    'CREDATTIM_0': datetime.datetime.now(),
                    'UPDDATTIM_0': datetime.datetime.now(),
                },
            )

        # Atribui o valor do contador
        counter_value, status = self.assigns_counter_value(sequence_number, counter, date, comp, max_value)
