from sqlalchemy import create_engine
import pandas as pd

con = create_engine("sqlite:///data/my_database.db")

query = '''
    SELECT * FROM bens_candidatos WHERE ano_eleicao >= 2000
'''
df_full = pd.read_sql_query( query, con )

con_new = create_engine( 'sqlite:///data/dados.db' )
df_full.to_sql('bens_candidatos', con_new, if_exists="replace" )