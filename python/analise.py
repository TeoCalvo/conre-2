import os
from sqlalchemy import create_engine
import pandas as pd

BASE_DIR =  os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
SQL_DIR = os.path.join( BASE_DIR, "sql" ) # hguvibihb
DATA_DIR = os.path.join( BASE_DIR, "data" )

def import_query( path ):
    with open( path ,'r' ) as query_file:
        query = query_file.read()
    return query

query_path = os.path.join(SQL_DIR, 'patrimonio_ano.sql')
query = import_query( query_path )

con = create_engine( 'sqlite:///' + os.path.join( DATA_DIR, 'my_database.db' ) )
print(con.table_names())