from database import engine, SessionLocal, Base, create_database
from models import Cliente, Carro, Agencia, Funcionario, Contrato, Manutencao
from repository import Repositorio
from popula_bd import popular_banco  # Importa a função de popular o banco

# Criar o banco de dados caso não exista
create_database()

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

repo = Repositorio()

# Popular as tabelas com os dados iniciais
popular_banco()

def input_int(mensagem):
    """Solicita um número inteiro do usuário e trata erro de entrada."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")

def input_float(mensagem):
    """Solicita um número decimal do usuário e trata erro de entrada."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

def menu():
    while True:
        print("\n--- Sistema de Gestão de Locadora de Carros ---")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Carro")
        print("3. Cadastrar Agência")
        print("4. Cadastrar Funcionário")
        print("5. Cadastrar Contrato")
        print("6. Cadastrar Manutenção")
        print("7. Listar Clientes")
        print("8. Listar Carros")
        print("9. Listar Agências")
        print("10. Listar Funcionários")
        print("11. Listar Contratos")
        print("12. Listar Manutenções")
        print("13. Atualizar Cliente")
        print("14. Atualizar Carro")
        print("15. Atualizar Agência")
        print("16. Atualizar Funcionário")
        print("17. Atualizar Contrato")
        print("18. Atualizar Manutenção")
        print("19. Remover Cliente")
        print("20. Remover Carro")
        print("21. Remover Agência")
        print("22. Remover Funcionário")
        print("23. Remover Contrato")
        print("24. Remover Manutenção")
        print("0. Sair")
        print("------------------------------------")

        opcao = input("Escolha uma opção: ")

        #  1. Cadastrar Cliente
        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            endereco = input("Endereço: ")
            cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email, endereco=endereco)
            repo.adicionar(cliente)


        #  2. Cadastrar Carro
        elif opcao == "2":
            modelo = input("Modelo: ")
            marca = input("Marca: ")
            placa = input("Placa: ")
            ano = input_int("Ano: ")
            categoria = input("Categoria: ")
            quilometragem = input_int("Quilometragem: ")
            carro = Carro(modelo=modelo, marca=marca, placa=placa, ano=ano, categoria=categoria, quilometragem=quilometragem)
            repo.adicionar(carro)

        #  3. Cadastrar Agência
        elif opcao == "3":
            nome = input("Nome da Agência: ")
            cidade = input("Cidade: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            agencia = Agencia(nome=nome, cidade=cidade, endereco=endereco, telefone=telefone)
            repo.adicionar(agencia)

        #  4. Cadastrar Funcionário
        elif opcao == "4":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            cargo = input("Cargo: ")
            salario = input_float("Salário: ")
            id_agencia = input_int("ID da Agência: ")
            agencia = next((a for a in repo.listar("agencia") if a.id_agencia == id_agencia), None)
            if agencia:
                funcionario = Funcionario(nome=nome, cpf=cpf, cargo=cargo, salario=salario, id_agencia=id_agencia)
                repo.adicionar(funcionario)
            else:
                print("Erro: Agência não encontrada. Funcionário não cadastrado.")

        #  5. Cadastrar Contrato
        elif opcao == "5":
            data_inicio = input("Data de Início (YYYY-MM-DD): ")
            data_fim = input("Data de Fim (YYYY-MM-DD): ")
            valor_total = input_float("Valor Total: ")
            id_cliente = input_int("ID do Cliente: ")
            id_agencia = input_int("ID da Agência: ")
            id_carro = input_int("ID do Carro: ")
            
            cliente = next((c for c in repo.listar("cliente") if c.id_cliente == id_cliente), None)
            agencia = next((a for a in repo.listar("agencia") if a.id_agencia == id_agencia), None)
            carro = next((c for c in repo.listar("carro") if c.id_carro == id_carro), None)

            if cliente and agencia and carro:
                contrato = Contrato(data_inicio=data_inicio, data_fim=data_fim, valor_total=valor_total, cliente=cliente, agencia=agencia, carro=carro)
                repo.adicionar(contrato)
            else:
                print("Erro: Cliente, Agência ou Carro não encontrados.")

        #  6. Cadastrar Manutenção
        elif opcao == "6":
            id_carro = input_int("ID do Carro: ")
            descricao = input("Descrição: ")
            data = input("Data (YYYY-MM-DD): ")
            custo = input_float("Custo: ")
            
            carro = next((c for c in repo.listar("carro") if c.id_carro == id_carro), None)
            if carro:
                manutencao = Manutencao(carro=carro, descricao=descricao, data=data, custo=custo)
                repo.adicionar(manutencao)
            else:
                print("Erro: Carro não encontrado.")

        #  7-12. Listar Registros
        elif opcao == "7":
            repo.listar("cliente")
        elif opcao == "8":
            repo.listar("carro")
        elif opcao == "9":
            repo.listar("agencia")
        elif opcao == "10":
            repo.listar("funcionario")
        elif opcao == "11":
            repo.listar("contrato")
        elif opcao == "12":
            repo.listar("manutencao")

        #  13-18. Atualizar Registros
        elif opcao == "13":
            id_cliente = input_int("Digite o ID do cliente: ")
            nome = input("Novo Nome (Enter para manter): ")
            telefone = input("Novo Telefone (Enter para manter): ")
            email = input("Novo Email (Enter para manter): ")
            endereco = input("Novo Endereço (Enter para manter): ")
            campos = {k: v for k, v in {"nome": nome, "telefone": telefone, "email": email, "endereco": endereco}.items() if v}
            repo.atualizar("cliente", id_cliente, **campos)

        elif opcao == "14":
            id_carro = input_int("Digite o ID do carro: ")
            modelo = input("Novo Modelo (Enter para manter): ")
            marca = input("Nova Marca (Enter para manter): ")
            quilometragem = input("Nova Quilometragem (Enter para manter): ")
            campos = {k: v for k, v in {"modelo": modelo, "marca": marca, "quilometragem": quilometragem}.items() if v}
            repo.atualizar("carro", id_carro, **campos)

        elif opcao == "15":
            id_agencia = input_int("Digite o ID da Agência: ")
            nome = input("Novo Nome (Enter para manter): ")
            cidade = input("Nova Cidade (Enter para manter): ")
            endereco = input("Novo Endereço (Enter para manter): ")
            telefone = input("Novo Telefone (Enter para manter): ")
            campos = {k: v for k, v in {"nome": nome, "cidade": cidade, "endereco": endereco, "telefone": telefone}.items() if v}
            repo.atualizar("agencia", id_agencia, **campos)

        elif opcao == "16":
            id_funcionario = input_int("Digite o ID do Funcionário: ")
            nome = input("Novo Nome (Enter para manter): ")
            cargo = input("Novo Cargo (Enter para manter): ")
            salario = input("Novo Salário (Enter para manter): ")
            id_agencia = input("Novo ID da Agência (Enter para manter): ")

            campos = {k: v for k, v in {"nome": nome, "cargo": cargo, "salario": salario, "id_agencia": id_agencia}.items() if v}
            repo.atualizar("funcionario", id_funcionario, **campos)

        elif opcao == "17":
            id_contrato = input_int("Digite o ID do Contrato: ")
            data_inicio = input("Nova Data de Início (YYYY-MM-DD) (Enter para manter): ")
            data_fim = input("Nova Data de Fim (YYYY-MM-DD) (Enter para manter): ")
            valor_total = input("Novo Valor Total (Enter para manter): ")

            campos = {k: v for k, v in {"data_inicio": data_inicio, "data_fim": data_fim, "valor_total": valor_total}.items() if v}
            repo.atualizar("contrato", id_contrato, **campos)

        elif opcao == "18":
            id_manutencao = input_int("Digite o ID da Manutenção: ")
            descricao = input("Nova Descrição (Enter para manter): ")
            data = input("Nova Data (YYYY-MM-DD) (Enter para manter): ")
            custo = input("Novo Custo (Enter para manter): ")

            campos = {k: v for k, v in {"descricao": descricao, "data": data, "custo": custo}.items() if v}
            repo.atualizar("manutencao", id_manutencao, **campos)

        #  19-24. Remover Registros
        elif opcao == "19":
            id_cliente = input_int("Digite o ID do cliente a remover: ")
            repo.remover("cliente", id_cliente)

        elif opcao == "20":
            id_carro = input_int("Digite o ID do carro a remover: ")
            repo.remover("carro", id_carro)

        elif opcao == "21":
            id_agencia = input_int("Digite o ID da agência a remover: ")
            repo.remover("agencia", id_agencia)

        elif opcao == "22":
            id_funcionario = input_int("Digite o ID do funcionário a remover: ")
            repo.remover("funcionario", id_funcionario)
        
        elif opcao == "23":
            id_contrato = input_int("Digite o ID do contrato a remover: ")
            repo.remover("contrato", id_contrato)

        elif opcao == "24":
            id_manutencao = input_int("Digite o ID da manutenção a remover: ")
            repo.remover("manutencao", id_manutencao)

        #  0. Sair
        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
