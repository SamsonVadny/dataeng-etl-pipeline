import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

def load_to_postgres(df, table_name):
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}')

    df.to_sql(table_name,
                engine,
                if_exists='replace',
                index=False)

    print('Data loaded to MySQL successfully')