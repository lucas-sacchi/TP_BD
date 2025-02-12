from datetime import date
from repository import Repositorio
from models import Cliente, Carro, Agencia, Funcionario, Contrato, Manutencao

def popular_banco():
    repo = Repositorio()

    # Dados de exemplo para popular as tabelas
    clientes = [
        Cliente( nome="João Silva", cpf="12345678900", telefone="987654321", email="joao.silva@gmail.com", endereco="Rua A, 123"),
        Cliente( nome="Maria Oliveira", cpf="23456789011", telefone="912345678", email="maria.oliveira@gmail.com", endereco="Avenida B, 456"),
        Cliente( nome="Pedro Souza", cpf="34567890122", telefone="945678123", email="pedro.souza@gmail.com", endereco="Rua C, 789"),
        Cliente( nome="Ana Costa", cpf="45678901233", telefone="958745612", email="ana.costa@gmail.com", endereco="Rua D, 101"),
        Cliente(nome="Lucas Almeida", cpf="56789012344", telefone="961234578", email="lucas.almeida@gmail.com", endereco="Avenida E, 202")
    ]

    carros = [
        Carro( modelo="Fusca", marca="Volkswagen", placa="ABC1234", ano=2000, categoria="Hatch", quilometragem=150000),
        Carro( modelo="Civic", marca="Honda", placa="DEF5678", ano=2020, categoria="Sedan", quilometragem=25000),
        Carro( modelo="Gol", marca="Volkswagen", placa="GHI9012", ano=2018, categoria="Hatch", quilometragem=50000),
        Carro( modelo="Corolla", marca="Toyota", placa="JKL3456", ano=2021, categoria="Sedan", quilometragem=15000),
        Carro( modelo="Fiesta", marca="Ford", placa="MNO7890", ano=2019, categoria="Hatch", quilometragem=40000)
    ]

    agencias = [
        Agencia( nome="Agência Centro", cidade="São João del-Rei", endereco="Rua Dom Bosco, 100, Centro", telefone="1122334455"),
        Agencia( nome="Agência Sul", cidade="São João del-Rei", endereco="Avenida Tancredo Neves, 200, Centro", telefone="2233445566"),
        Agencia( nome="Agência Norte", cidade="São João del-Rei", endereco="Praça Brasil, 300, Centro", telefone="3344556677"),
        Agencia( nome="Agência Leste", cidade="São João del-Rei", endereco="Rua Getúlio Vargas, 400, Centro", telefone="4455667788"),
        Agencia( nome="Agência Oeste", cidade="São João del-Rei", endereco="Avenida 7 de Setembro, 500, Centro", telefone="5566778899")
    ]

    funcionarios = [
        Funcionario( nome="Ana Ribeirao", cpf="45678901234", cargo="CEO", salario=5000.00, id_agencia=1),
        Funcionario( nome="Victor Brita", cpf="56789012345", cargo="Assistente", salario=3000.00, id_agencia=2),
        Funcionario( nome="Bernardo Oitto", cpf="67890123456", cargo="Estagiario", salario=2500.00, id_agencia=3),
        Funcionario( nome="Gabriel Mourao", cpf="78901234567", cargo="Gerente", salario=4500.00, id_agencia=4),
        Funcionario( nome="Beatriz Romera", cpf="89012345678", cargo="Supervisor", salario=4000.00, id_agencia=5)
    ]

    contratos = [
        Contrato( data_inicio=date(2024, 1, 10), data_fim=date(2024, 1, 20), valor_total=1200.00, id_cliente=1, id_agencia=1, id_carro=1),
        Contrato( data_inicio=date(2024, 2, 15), data_fim=date(2024, 2, 25), valor_total=2500.00, id_cliente=2, id_agencia=2, id_carro=2),
        Contrato( data_inicio=date(2024, 3, 5), data_fim=date(2024, 3, 15), valor_total=1800.00, id_cliente=3, id_agencia=3, id_carro=3),
        Contrato( data_inicio=date(2024, 4, 1), data_fim=date(2024, 4, 10), valor_total=2000.00, id_cliente=4, id_agencia=4, id_carro=4),
        Contrato( data_inicio=date(2024, 5, 1), data_fim=date(2024, 5, 15), valor_total=1500.00, id_cliente=5, id_agencia=5, id_carro=5)
    ]

    manutencao = [
        Manutencao( id_carro=1, descricao="Troca de óleo", data=date(2024, 1, 15), custo=200.00),
        Manutencao( id_carro=2, descricao="Troca de pneu", data=date(2024, 2, 20), custo=400.00),
        Manutencao( id_carro=3, descricao="Reparo no motor", data=date(2024, 3, 10), custo=800.00),
        Manutencao( id_carro=4, descricao="Revisão geral", data=date(2024, 4, 5), custo=350.00),
        Manutencao( id_carro=5, descricao="Troca de bateria", data=date(2024, 5, 10), custo=250.00)
    ]

    try:
        # Adicionando os dados ao banco de dados
        for cliente in clientes:
            repo.adicionar(cliente)

        for carro in carros:
            repo.adicionar(carro)

        for agencia in agencias:
            repo.adicionar(agencia)

        for funcionario in funcionarios:
            repo.adicionar(funcionario)

        for contrato in contratos:
            repo.adicionar(contrato)

        for manutencao_item in manutencao:
            repo.adicionar(manutencao_item)

        print("Banco de dados populado com sucesso!")

    except Exception as e:
        print(f"Erro ao popular o banco de dados: {e}")
