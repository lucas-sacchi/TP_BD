class Cliente:
    def __init__(self, id_cliente, nome, cpf, telefone, email, endereco):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.contratos = []  # Um cliente pode ter vários contratos

    def adicionar_contrato(self, contrato):
        self.contratos.append(contrato)

    def __repr__(self):
        return f"Cliente({self.id_cliente}, {self.nome}, {self.cpf})"

class Carro:
    def __init__(self, id_carro, modelo, marca, placa, ano, categoria, quilometragem):
        self.id_carro = id_carro
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.categoria = categoria
        self.quilometragem = quilometragem
        self.manutencoes = []  # Um carro pode ter várias manutenções

    def adicionar_manutencao(self, manutencao):
        self.manutencoes.append(manutencao)

    def __repr__(self):
        return f"Carro({self.id_carro}, {self.modelo}, {self.placa})"

class Agencia:
    def __init__(self, id_agencia, nome, cidade, endereco, telefone):
        self.id_agencia = id_agencia
        self.nome = nome
        self.cidade = cidade
        self.endereco = endereco
        self.telefone = telefone
        self.funcionarios = []  # Uma agência pode ter vários funcionários

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def __repr__(self):
        return f"Agencia({self.id_agencia}, {self.nome})"

class Funcionario:
    def __init__(self, id_funcionario, nome, cpf, cargo, salario, id_agencia):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario
        self.id_agencia = id_agencia

    def __repr__(self):
        return f"Funcionario({self.id_funcionario}, {self.nome}, {self.cargo})"

class Contrato:
    def __init__(self, id_contrato, data_inicio, data_fim, valor_total, cliente, agencia, carro):
        self.id_contrato = id_contrato
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor_total = valor_total
        self.cliente = cliente
        self.agencia = agencia
        self.carro = carro

    def __repr__(self):
        return f"Contrato({self.id_contrato}, Cliente: {self.cliente.nome}, Carro: {self.carro.modelo})"

class Manutencao:
    def __init__(self, id_manutencao, carro, descricao, data, custo):
        self.id_manutencao = id_manutencao
        self.carro = carro
        self.descricao = descricao
        self.data = data
        self.custo = custo

    def __repr__(self):
        return f"Manutencao({self.id_manutencao}, Carro: {self.carro.modelo})"