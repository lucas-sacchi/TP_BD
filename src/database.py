import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Definir a URL de conexão com o MySQL
DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/"

# Conectar ao MySQL para verificar se o banco de dados existe e criar se necessário
def create_database():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cursor = connection.cursor()
    
    # Tentar criar o banco de dados, caso não exista
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
        print(f"Banco de dados '{os.getenv('DB_NAME')}' criado ou já existente.")
    except mysql.connector.Error as err:
        print(f"Erro ao criar banco de dados: {err}")
    finally:
        cursor.close()
        connection.close()

# Criar a conexão com o banco de dados (após garantir que o banco foi criado)
create_database()

# Criar o engine para SQLAlchemy conectar ao banco de dados
engine = create_engine(DATABASE_URL + os.getenv('DB_NAME'), echo=True)

# Criar a sessão de banco de dados
SessionLocal = sessionmaker(bind=engine)

# Base para os modelos ORM
Base = declarative_base()