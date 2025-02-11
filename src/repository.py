from models import Cliente, Carro, Agencia, Funcionario, Contrato, Manutencao

class Repositorio:
    def __init__(self):
        self.clientes = []
        self.carros = []
        self.agencias = []
        self.funcionarios = []
        self.contratos = []
        self.manutencoes = []

    def adicionar(self, objeto):
        """Adiciona um objeto ao repositório."""
        if isinstance(objeto, Cliente):
            self.clientes.append(objeto)
        elif isinstance(objeto, Carro):
            self.carros.append(objeto)
        elif isinstance(objeto, Agencia):
            self.agencias.append(objeto)
        elif isinstance(objeto, Funcionario):
            self.funcionarios.append(objeto)
        elif isinstance(objeto, Contrato):
            objeto.cliente.adicionar_contrato(objeto)
            self.contratos.append(objeto)
        elif isinstance(objeto, Manutencao):
            objeto.carro.adicionar_manutencao(objeto)
            self.manutencoes.append(objeto)
        print(f"{objeto.__class__.__name__} adicionado com sucesso!")

    def listar(self, tipo):
        """Lista objetos do tipo especificado."""
        lista = getattr(self, tipo + 's', [])
        if lista:
            for obj in lista:
                print(obj)
        else:
            print(f"Nenhum {tipo} cadastrado.")

    def remover(self, tipo, id_obj):
        """Remove um objeto do repositório."""
        lista = self.listar(tipo)
        for obj in lista:
            if getattr(obj, f'id_{tipo}') == id_obj:
                lista.remove(obj)
                print(f"{tipo.capitalize()} {id_obj} removido.")
                return
        print(f"{tipo.capitalize()} {id_obj} não encontrado.")

    def atualizar(self, tipo, id_obj, **kwargs):
        """Atualiza atributos de um objeto no repositório."""
        lista = self.listar(tipo)
        for obj in lista:
            if getattr(obj, f'id_{tipo}') == id_obj:
                for key, value in kwargs.items():
                    setattr(obj, key, value)
                print(f"{tipo.capitalize()} {id_obj} atualizado.")
                return
        print(f"{tipo.capitalize()} {id_obj} não encontrado.")
