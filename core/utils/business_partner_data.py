from decouple import config

# from core.decorators.cache_db import results_db
from core.utils.database.database import Database


# @results_db(timeout=300, cache_key_prefix='customers')
def read_customer_data():
    """Retrieves customer data from the legacy database."""
    schema = config('DB_SCHEMA', default='')

    if not schema:
        print('Não foi possível buscar os clientes, pois o DB_SCHEMA não foi configurado.')
        return []

    database = Database('default')
    customers = []

    with database as connection:
        if connection:
            # Build query to get the customers data
            query, where_clause = database.build_query(
                table=f'{schema}.BPCUSTOMER',
                columns=[
                    'ROWID',
                    'BPCNUM_0',
                    'BPCNAM_0',
                ],
                options={'ORDER BY': 'BPCNAM_0'},
                # where_clauses={'INVOICE_NUM_0': Condition('=', 'NC-01425/00001')},
            )

            try:
                with connection.cursor() as cursor:
                    print('Executando query...')
                    cursor.execute(query, where_clause)
                    for row in cursor.fetchall():
                        customers.append((row[0], row[1]))
            except Exception as e:
                print(f'Erro ao buscar clientes do banco legado: {e}')
                customers = []
        else:
            print('Não foi possível conectar ao banco de dados legado.')
            customers = []

    return customers


def read_partner_data(db_alias, query, where_clause=None):
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
