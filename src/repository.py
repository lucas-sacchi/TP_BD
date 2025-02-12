from database import get_connection

class Repositorio:
    def adicionar(self, tabela, dados):
        connection = get_connection()
        cursor = connection.cursor()
        
        colunas = ', '.join(dados.keys())
        valores = ', '.join(['%s'] * len(dados))
        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
        
        cursor.execute(sql, tuple(dados.values()))
        connection.commit()
        cursor.close()
        connection.close()

    def listar(self, tabela):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute(f"SELECT * FROM {tabela}")
        registros = cursor.fetchall()
        
        cursor.close()
        connection.close()
        return registros

    def remover(self, tabela, coluna_id, id_valor):
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute(f"DELETE FROM {tabela} WHERE {coluna_id} = %s", (id_valor,))
        connection.commit()
        
        cursor.close()
        connection.close()

    def atualizar(self, tabela, id_valor, **dados):
        """Atualiza um registro na tabela especificada."""
        connection = get_connection()
        cursor = connection.cursor()

        if not dados:
            print("Nenhum dado para atualizar.")
            return

        updates = ', '.join([f"{coluna} = %s" for coluna in dados.keys()])

        # Definição correta da chave primária
        chaves_primarias = {
            "clientes": "id_cliente",
            "carros": "id_carro",
            "agencias": "id_agencia",
            "funcionarios": "id_funcionario",
            "contratos": "id_contrato",
            "manutencoes": "id_manutencao"
        }

        coluna_id = chaves_primarias.get(tabela, f"id_{tabela[:-1]}")  # Usa o dicionário para definir a chave primária

        sql = f"UPDATE {tabela} SET {updates} WHERE {coluna_id} = %s"
        valores = tuple(dados.values()) + (id_valor,)

        cursor.execute(sql, valores)
        connection.commit()

        cursor.close()
        connection.close()
        print(f"Registro atualizado na tabela {tabela}.")

