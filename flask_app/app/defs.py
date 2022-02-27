import psycopg2
import pandas as pd

# PG
import sqlalchemy


def query_as_df(env, query):
    # els01
    con_els01 = env
    engine_els01 = sqlalchemy.create_engine(con_els01)
    con2els01 = engine_els01.connect()

    df = pd.read_sql(query, con2els01)



    return df
