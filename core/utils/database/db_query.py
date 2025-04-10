from core.utils.database.database import Database


@staticmethod
def execute_query(db_alias, query, params=None):
    """
    Retrieves data from a legacy database.

    Args:
        query: A SQL query string
        params: A tuple of parameters to replace the placeholders in the query.
                Pass None or an empty tuple if there are no parameters.

    Returns:
        A list of dictionaries representing the rows found in the database.
        Each dictionary contains the column names as keys and the corresponding values.
        If no data is found, an empty list is returned.
    """
    database = Database(db_alias)
    data = []

    with database as connection:
        if connection:
            try:
                with connection.cursor() as cursor:
                    print('Executando query...')
                    cursor.execute(query, params)

                    columns = [desc[0] for desc in cursor.description]

                    for row in cursor.fetchall():
                        data.append(dict(zip(columns, row)))
            except Exception as e:
                print(f'Erro ao buscar dados do banco legado: {e}')
                data = []
        else:
            print('Não foi possível conectar ao banco de dados legado.')
            data = []

    return data
