# from core.decorators.cache_db import results_db
from core.utils.database import Database


def read_country_data(db_alias, query, where_clause=None):
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
