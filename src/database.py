import mysql.connector
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a conexão com o banco de dados
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def get_connection():
    """Retorna uma conexão com o banco de dados."""
    return mysql.connector.connect(**DB_CONFIG)

def create_database():
    """Cria o banco de dados caso não exista."""
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
    cursor.close()
    connection.close()
    print(f"Banco de dados '{os.getenv('DB_NAME')}' criado/verificado.")

def create_tables():
    """Cria as tabelas no banco de dados."""
    connection = get_connection()
    cursor = connection.cursor()
    
    tables = [
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cpf VARCHAR(11) UNIQUE NOT NULL,
            telefone VARCHAR(15),
            email VARCHAR(100),
            endereco VARCHAR(200)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS carros (
            id_carro INT AUTO_INCREMENT PRIMARY KEY,
            modelo VARCHAR(50) NOT NULL,
            marca VARCHAR(50) NOT NULL,
            placa VARCHAR(7) UNIQUE NOT NULL,
            ano INT,
            categoria VARCHAR(50),
            quilometragem INT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS agencias (
            id_agencia INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cidade VARCHAR(100) NOT NULL,
            endereco VARCHAR(200) NOT NULL,
            telefone VARCHAR(15)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS funcionarios (
            id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cpf VARCHAR(11) UNIQUE NOT NULL,
            cargo VARCHAR(50),
            salario FLOAT,
            id_agencia INT,
            FOREIGN KEY (id_agencia) REFERENCES agencias(id_agencia)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS contratos (
            id_contrato INT AUTO_INCREMENT PRIMARY KEY,
            data_inicio DATE,
            data_fim DATE,
            valor_total FLOAT,
            id_cliente INT,
            id_agencia INT,
            id_carro INT,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
            FOREIGN KEY (id_agencia) REFERENCES agencias(id_agencia),
            FOREIGN KEY (id_carro) REFERENCES carros(id_carro)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS manutencoes (
            id_manutencao INT AUTO_INCREMENT PRIMARY KEY,
            id_carro INT,
            descricao VARCHAR(200),
            data DATE,
            custo FLOAT,
            FOREIGN KEY (id_carro) REFERENCES carros(id_carro)
        )
        """
    ]
    
    for table in tables:
        cursor.execute(table)
    
    connection.commit()
    cursor.close()
    connection.close()
    print("Tabelas criadas/verificadas com sucesso.")

create_database()
create_tables()
