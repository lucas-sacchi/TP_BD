from database import SessionLocal
from models import Cliente, Carro, Agencia, Funcionario, Contrato, Manutencao

class Repositorio:
    def __init__(self):
        self.db = SessionLocal()

    def adicionar(self, objeto):
        """Adiciona um objeto ao banco de dados."""
    #    try:
        self.db.add(objeto)
        self.db.commit()
        self.db.refresh(objeto)

            # Verifique se o objeto foi realmente adicionado
 #           added_objeto = self.db.query(objeto.__class__).filter_by(id=objeto.id).first()
  #          if added_objeto:
   #             print(f"{objeto.__class__.__name__} adicionado com sucesso!")
     #       else:
      #          print(f"Erro ao adicionar {objeto.__class__.__name__}")
       # except Exception as e:
        #    self.db.rollback()
         #   print(f"Erro ao adicionar {objeto.__class__.__name__}: {e}")
          #  raise

    def listar(self, tipo):
        """Lista objetos do banco de dados."""
        modelo = {
            "cliente": Cliente,
            "carro": Carro,
            "agencia": Agencia,
            "funcionario": Funcionario,
            "contrato": Contrato,
            "manutencao": Manutencao
        }.get(tipo)

        if modelo:
            try:
                objetos = self.db.query(modelo).all()
                if objetos:
                    print(f"Listando {len(objetos)} {tipo}s")
                    for obj in objetos:
                        print(obj)
                else:
                    print(f"Nenhum {tipo} encontrado.")
                return objetos
            except Exception as e:
                print(f"Erro ao listar {tipo}: {e}")
                raise
        else:
            print("Tipo inválido.")
            return []

    def remover(self, tipo, id_obj):
        """Remove um objeto do banco de dados."""
        modelo = {
            "cliente": Cliente,
            "carro": Carro,
            "agencia": Agencia,
            "funcionario": Funcionario,
            "contrato": Contrato,
            "manutencao": Manutencao
        }.get(tipo)

        if modelo:
            try:
                # Aqui, utilizamos a chave correta para a tabela
                objeto = self.db.query(modelo).filter_by(**{f"id_{tipo}": id_obj}).first()
                if objeto:
                    self.db.delete(objeto)
                    self.db.commit()
                    print(f"{tipo.capitalize()} {id_obj} removido com sucesso.")
                else:
                    print(f"{tipo.capitalize()} {id_obj} não encontrado.")
            except Exception as e:
                self.db.rollback()
                print(f"Erro ao remover {tipo}: {e}")
                raise
        else:
            print("Tipo inválido.")

    def atualizar(self, tipo, id_obj, **kwargs):
        """Atualiza atributos de um objeto no banco de dados."""
        modelo = {
            "cliente": Cliente,
            "carro": Carro,
            "agencia": Agencia,
            "funcionario": Funcionario,
            "contrato": Contrato,
            "manutencao": Manutencao
        }.get(tipo)

        if modelo:
            try:
                # Aqui, utilizamos a chave correta para a tabela
                objeto = self.db.query(modelo).filter_by(**{f"id_{tipo}": id_obj}).first()
                if objeto:
                    for key, value in kwargs.items():
                        setattr(objeto, key, value)
                    self.db.commit()
                    print(f"{tipo.capitalize()} {id_obj} atualizado com sucesso.")
                else:
                    print(f"{tipo.capitalize()} {id_obj} não encontrado.")
            except Exception as e:
                self.db.rollback()
                print(f"Erro ao atualizar {tipo}: {e}")
                raise
        else:
            print("Tipo inválido.")
