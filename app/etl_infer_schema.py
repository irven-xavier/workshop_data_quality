import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os
import pandera as pa

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

# rodar o script e fazer query para a inferência do schema da tabela no banco de dados
if __name__ == "__main__" :

    query = "SELECT * FROM produtos_bronze LIMIT 100" # pra inferência ser baseada em uma amostra da tabela
    df_crm = extrair_do_sql(query=query)
    schema_crm = pa.infer_schema(df_crm)

    with open("schema_crm.py", "w", encoding="utf-8") as arquivo:
        arquivo.write(schema_crm.to_script())

    print(df_crm)