class Cliente:
    def __init__(self, id_cliente=None, nome=None, cpf=None, telefone=None, email=None, endereco=None):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nome": self.nome,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "email": self.email,
            "endereco": self.endereco
        }

class Carro:
    def __init__(self, id_carro=None, modelo=None, marca=None, placa=None, ano=None, categoria=None, quilometragem=None):
        self.id_carro = id_carro
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.categoria = categoria
        self.quilometragem = quilometragem
    
    def to_dict(self):
        return {
            "id_carro": self.id_carro,
            "modelo": self.modelo,
            "marca": self.marca,
            "placa": self.placa,
            "ano": self.ano,
            "categoria": self.categoria,
            "quilometragem": self.quilometragem
        }

class Agencia:
    def __init__(self, id_agencia=None, nome=None, cidade=None, endereco=None, telefone=None):
        self.id_agencia = id_agencia
        self.nome = nome
        self.cidade = cidade
        self.endereco = endereco
        self.telefone = telefone
    
    def to_dict(self):
        return {
            "id_agencia": self.id_agencia,
            "nome": self.nome,
            "cidade": self.cidade,
            "endereco": self.endereco,
            "telefone": self.telefone
        }

class Funcionario:
    def __init__(self, id_funcionario=None, nome=None, cpf=None, cargo=None, salario=None, id_agencia=None):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario
        self.id_agencia = id_agencia
    
    def to_dict(self):
        return {
            "id_funcionario": self.id_funcionario,
            "nome": self.nome,
            "cpf": self.cpf,
            "cargo": self.cargo,
            "salario": self.salario,
            "id_agencia": self.id_agencia
        }

class Contrato:
    def __init__(self, id_contrato=None, data_inicio=None, data_fim=None, valor_total=None, id_cliente=None, id_agencia=None, id_carro=None):
        self.id_contrato = id_contrato
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor_total = valor_total
        self.id_cliente = id_cliente
        self.id_agencia = id_agencia
        self.id_carro = id_carro
    
    def to_dict(self):
        return {
            "id_contrato": self.id_contrato,
            "data_inicio": self.data_inicio,
            "data_fim": self.data_fim,
            "valor_total": self.valor_total,
            "id_cliente": self.id_cliente,
            "id_agencia": self.id_agencia,
            "id_carro": self.id_carro
        }

class Manutencao:
    def __init__(self, id_manutencao=None, id_carro=None, descricao=None, data=None, custo=None):
        self.id_manutencao = id_manutencao
        self.id_carro = id_carro
        self.descricao = descricao
        self.data = data
        self.custo = custo
    
    def to_dict(self):
        return {
            "id_manutencao": self.id_manutencao,
            "id_carro": self.id_carro,
            "descricao": self.descricao,
            "data": self.data,
            "custo": self.custo
        }