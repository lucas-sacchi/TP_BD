from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(50), unique=True, nullable=False)
    telefone = Column(String(15))
    email = Column(String(100))
    endereco = Column(String(200))

    contratos = relationship("Contrato", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente(id_cliente={self.id_cliente}, nome='{self.nome}', cpf='{self.cpf}', telefone='{self.telefone}', email='{self.email}', endereco='{self.endereco}')>"

class Carro(Base):
    __tablename__ = "carros"

    id_carro = Column(Integer, primary_key=True, autoincrement=True)
    modelo = Column(String(50), nullable=False)  # Modelo do carro
    marca = Column(String(50), nullable=False)  # Marca do carro
    placa = Column(String(7), unique=True, nullable=False)  # Placa do carro
    ano = Column(Integer)
    categoria = Column(String(50))  # Categoria do carro
    quilometragem = Column(Integer)

    manutencoes = relationship("Manutencao", back_populates="carro")
    contratos = relationship("Contrato", back_populates="carro")

class Agencia(Base):
    __tablename__ = "agencias"

    id_agencia = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)  # Nome da agência
    cidade = Column(String(100), nullable=False)  # Cidade da agência
    endereco = Column(String(200), nullable=False)  # Endereço da agência
    telefone = Column(String(15))  # Telefone da agência

    funcionarios = relationship("Funcionario", back_populates="agencia")
    contratos = relationship("Contrato", back_populates="agencia")

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id_funcionario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)  # Nome do funcionário
    cpf = Column(String(11), unique=True, nullable=False)  # CPF do funcionário
    cargo = Column(String(50))  # Cargo do funcionário
    salario = Column(Float)
    id_agencia = Column(Integer, ForeignKey("agencias.id_agencia"))

    agencia = relationship("Agencia", back_populates="funcionarios")

class Contrato(Base):
    __tablename__ = "contratos"

    id_contrato = Column(Integer, primary_key=True, autoincrement=True)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    valor_total = Column(Float)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"))
    id_agencia = Column(Integer, ForeignKey("agencias.id_agencia"))
    id_carro = Column(Integer, ForeignKey("carros.id_carro"))

    cliente = relationship("Cliente", back_populates="contratos")
    agencia = relationship("Agencia", back_populates="contratos")
    carro = relationship("Carro", back_populates="contratos")

class Manutencao(Base):
    __tablename__ = "manutencoes"

    id_manutencao = Column(Integer, primary_key=True, autoincrement=True)
    id_carro = Column(Integer, ForeignKey("carros.id_carro"))
    descricao = Column(String(200))  # Descrição da manutenção
    data = Column(Date)
    custo = Column(Float)

    carro = relationship("Carro", back_populates="manutencoes")