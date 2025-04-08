import datetime
import enum


def calculate_number_of_days(start_date, end_date):
    """
    Calcula o número ordinal do dia dentro do ano usando strftime('%j').

    Args:
      start_date: Um objeto datetime.date ou datetime.datetime.

    Returns:
      Um inteiro representando o dia do ano (1 a 366).
    """
    if not isinstance(start_date, (datetime.date, datetime.datetime)) or not isinstance(
        end_date, (datetime.date, datetime.datetime)
    ):
        raise TypeError('Entrada deve ser um objeto datetime.date ou datetime.datetime')

    if start_date > end_date:
        raise ValueError('A data de início deve ser anterior à data de término')

    # Calcula o número de dias entre as duas datas
    delta = end_date - start_date

    return delta.days + 1  # Adiciona 1 para incluir o dia de início


class PositionType(enum.IntEnum):
    """Define os tipos de segmentos que compõem o valor do contador."""

    CONSTANT = 1
    YEAR = 2
    MONTH = 3
    WEEK_NUM_MON = 4
    DAY = 5
    SEQUENCE = 8
    COMPLEMENT = 9

    # Você pode adicionar métodos ao Enum se precisar de lógica extra
    # def describe(self):
    #     return f"{self.name}: {self.value}"
