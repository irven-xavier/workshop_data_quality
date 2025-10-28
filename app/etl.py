import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os
import pandera.pandas as pa # usar assim pra mexer com pandas
from prod_schema import ProdutoSchema

# variaveis de ambiente do postgresql
def load_settings():
    
    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        'db_host': os.getenv('POSTGRES_HOST'),
        'db_user': os.getenv('POSTGRES_USER'),
        'db_pass': os.getenv('POSTGRES_PASSWORD'),
        'db_name': os.getenv('POSTGRES_DB'),
        'db_port': os.getenv('POSTGRES_PORT')
    }

    return settings

# criar conexão com o banco de dados
@pa.check_output(ProdutoSchema.to_schema(), lazy=True)
def extrair_do_sql(query: str) -> pd.DataFrame:

    settings = load_settings()

    connection_string = (
    f"postgresql://{settings['db_user']}:{settings['db_pass']}@"
    f"{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"
)


    engine = create_engine(connection_string)

    with engine.connect() as conn, conn.begin():
        df_crm = pd.read_sql(query, conn)

    return df_crm   

# rodar o script e fazer query 
if __name__ == "__main__" :

    query = "SELECT * FROM produtos_bronze LIMIT 100" 
    df_crm = extrair_do_sql(query=query)

    print(df_crm)