from typing import Any, Dict, Optional, Tuple

from django.conf import settings
from django.db import DatabaseError, connections, transaction


class Database:
    def __init__(self, connection_name='default'):
        """
        Inicializa a classe Database com o nome da conexão a ser usada.
        """
        self.connection_name = connection_name
        self.connection = None  # Inicializa a conexão como None

    def __enter__(self):
        """
        Método chamado ao entrar no bloco 'with'.
        Estabelece a conexão com o banco de dados.
        """
        try:
            self.connection = connections[self.connection_name]
            self.connection.ensure_connection()
            return self.connection  # Retorna a conexão para ser usada no bloco 'with'
        except DatabaseError:
            # import logging

            # logger = logging.getLogger(__name__)
            # logger.error(f'Erro ao conectar ao banco de dados {self.connection_name}: {e}')
            pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Método chamado ao sair do bloco 'with'.
        Fecha a conexão com o banco de dados, lidando com possíveis erros.
        """
        if self.connection:
            try:
                self.connection.close()
            except Exception:
                pass
                # import logging

                # logger = logging.getLogger(__name__)
                # logger.error(f'Erro ao desconectar do banco de dados: {e}')

    @staticmethod
    def build_query(
        table: str,
        columns: Optional[list[str]] = None,
        where_clauses: Optional[Dict[str, Tuple[str, Any]]] = None,
        options: Optional[Dict[str, str]] = None,
        limit: Optional[int] = None,
    ):
        # Build the SELECT clause dynamically
        placeholder = settings.QUERY_PLACEHOLDER
        select_clause = ', '.join(columns) if columns else '*'

        if limit and limit > 0:
            query = f'SELECT TOP {limit} {select_clause} FROM {table}'
        else:
            query = f'SELECT {select_clause} FROM {table}'

        # Build the WHERE clause dynamically with multiple conditions
        if where_clauses:
            where_clause = ' AND '.join([
                f'{column} {operator} {placeholder}' for column, (operator, _) in where_clauses.items()
            ])
            query += f' WHERE {where_clause}'
            where_values = tuple(value for _, value in where_clauses.values())
        else:
            where_values = ()

        # Add GROUP BY clause if provided
        # Add GROUP BY and ORDER BY clauses if provided
        if options:
            if 'group_by' in options:
                query += f' GROUP BY {options["group_by"]}'
            if 'order_by' in options:
                query += f' ORDER BY {options["order_by"]}'

        return query, where_values

    @staticmethod
    def execute_query(db_alias, query, where_clause=None):
        """
        Retrieves data from a legacy database.

        Args:
            query: A SQL query string
            params: A tuple of parameters to replace the placeholders in the query.
                    Pass None or an empty tuple if there are no parameters.

        Returns:
            A list of tuples representing the rows found (only the first two columns),
            or an empty list in case of an error or if no data is found.
        """
        database = Database(db_alias)
        data = []

        with database as connection:
            if connection:
                try:
                    with connection.cursor() as cursor:
                        print('Executando query...')
                        cursor.execute(query, where_clause)
                        for row in cursor.fetchall():
                            data.append((row[0], row[1]))
                except Exception as e:
                    print(f'Erro ao buscar dados do banco legado: {e}')
                    data = []
            else:
                print('Não foi possível conectar ao banco de dados legado.')
                data = []

        return data

    @staticmethod
    def _fetch_all_as_dicts(cursor):
        """
        Utilitário interno para converter resultados de SELECT em lista de dicionários.
        """
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    @transaction.atomic
    def insert_into_table(self, table_name: str, data: dict):
        """
        Insere um novo registro em qualquer tabela, com base em um dicionário.
        """

        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = list(data.values())

        sql = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
        with self.connection.cursor() as cursor:
            cursor.execute(sql, values)

    @transaction.atomic
    def update_table(self, table_name: str, data: dict, where: dict):
        """
        Atualiza registros em qualquer tabela com base em dicionários.
        - data: campos a serem atualizados
        - where: condições do WHERE
        """

        set_clause = ', '.join([f'{k} = %s' for k in data.keys()])
        where_clause = ' AND '.join([f'{k} = %s' for k in where.keys()])
        values = list(data.values()) + list(where.values())

        sql = f'UPDATE {table_name} SET {set_clause} WHERE {where_clause}'
        with self.connection.cursor() as cursor:
            cursor.execute(sql, values)

    @transaction.atomic
    def bulk_insert_into_table(self, table_name: str, rows: list[dict], batch_size=1000):
        """
        Insere vários registros de uma vez só em uma tabela.
        - `rows`: lista de dicionários com os mesmos campos.
        """

        if not rows:
            return

        columns = list(rows[0].keys())
        col_clause = ', '.join(columns)
        row_placeholder = '(' + ', '.join(['%s'] * len(columns)) + ')'

        def chunks(lst, size):
            for i in range(0, len(lst), size):
                yield lst[i : i + size]

        with self.connection.cursor() as cursor:
            for batch in chunks(rows, batch_size):
                placeholders = ', '.join([row_placeholder] * len(batch))
                values = [item for row in batch for item in row.values()]
                sql = f'INSERT INTO {table_name} ({col_clause}) VALUES {placeholders}'
                cursor.execute(sql, values)
