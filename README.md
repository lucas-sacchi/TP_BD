# TP_BD
# README - Sistema de Gestão de Locadora de Carros

## Índice
1. [Descrição do Projeto](#descricao-do-projeto)
2. [Pré-requisitos](#pre-requisitos)
3. [Instalação e Configuração](#instalacao-e-configuracao)
4. [Configuração do Banco de Dados](#configuracao-do-banco-de-dados)
5. [Execução do Sistema](#execucao-do-sistema)
6. [Funcionalidades](#funcionalidades)
7. [Estrutura do Projeto](#estrutura-do-projeto)
8. [Problemas Comuns e Soluções](#problemas-comuns-e-solucoes)

---

## 1. Descrição do Projeto <a name="descricao-do-projeto"></a>
Este projeto é um sistema de gestão para uma locadora de carros. Ele permite gerenciar clientes, carros, agências, funcionários, contratos de aluguel e manutenções.
O sistema interage com um banco de dados MySQL e oferece funcionalidades CRUD para cada entidade.

## 2. Pré-requisitos <a name="pre-requisitos"></a>
Antes de rodar o projeto, certifique-se de ter os seguintes requisitos instalados:

- Python 3.8+
- MySQL Server
- MySQL Workbench (opcional, para visualização do banco de dados)
- Pip (gerenciador de pacotes do Python)

## 3. Instalação e Configuração <a name="instalacao-e-configuracao"></a>

### 3.1 Clonar o Repositório
Se o projeto estiver em um repositório Git, clone-o:
```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

### 3.2 Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate    # Para Windows
```

### 3.3 Instalar Dependências
Execute o seguinte comando para instalar todas as dependências necessárias:
```bash
pip install -r requirements.txt
```

## 4. Configuração do Banco de Dados <a name="configuracao-do-banco-de-dados"></a>

### 4.1 Configurar as Credenciais do Banco de Dados
As credenciais do banco de dados estão armazenadas no arquivo `.env`. Certifique-se de configurá-lo corretamente:

#### Arquivo `.env`:
```
DB_USER=root
DB_PASSWORD=trabalhobd
DB_HOST=localhost
DB_NAME=locadora6
```
Caso o banco de dados esteja rodando em um servidor diferente, modifique `DB_HOST` para o IP correto.

### 4.2 Criar o Banco de Dados
O sistema já verifica e cria o banco de dados automaticamente. Caso queira criá-lo manualmente, acesse o MySQL e execute:
```sql
CREATE DATABASE IF NOT EXISTS locadora6;
```

### 4.3 Conectar ao MySQL Workbench (Opcional)
Caso deseje visualizar e manipular o banco de dados via MySQL Workbench:
1. Abra o MySQL Workbench.
2. Clique em "New Connection" e insira:
   - Hostname: `localhost`
   - Username: `root`
   - Password: `admin` (ou sua senha configurada)
3. Clique em "Test Connection".

Se a conexão for bem-sucedida, o banco `locadora6` aparecerá na lista de schemas.

## 5. Execução do Sistema <a name="execucao-do-sistema"></a>
Para rodar o sistema, basta executar o seguinte comando na raiz do projeto:
```bash
python main.py
```

Ao iniciar, o sistema:
1. Criará o banco de dados (se ainda não existir).
2. Criará as tabelas necessárias.
3. Populá o banco com dados de exemplo.
4. Abrirá o menu interativo para gerenciamento dos registros.

## 6. Funcionalidades <a name="funcionalidades"></a>
O sistema apresenta um menu interativo com as seguintes opções:

- **Cadastrar**: Cliente, Carro, Agência, Funcionário, Contrato, Manutenção.
- **Listar**: Clientes, Carros, Agências, Funcionários, Contratos, Manutenções.
- **Atualizar**: Clientes, Carros, Agências, Funcionários, Contratos, Manutenções.
- **Remover**: Clientes, Carros, Agências, Funcionários, Contratos, Manutenções.
- **Sair**: Fecha o programa.

## 7. Estrutura do Projeto <a name="estrutura-do-projeto"></a>
A estrutura do projeto está organizada da seguinte maneira:
```
├── database.py      # Configuração do banco de dados
├── main.py          # Arquivo principal do sistema
├── models.py        # Definição das classes ORM
├── repository.py    # Classe de repositório para acesso ao banco
├── popula_bd.py     # Popula o banco de dados com dados iniciais
├── requirements.txt # Lista de dependências do projeto
```

## 8. Problemas Comuns e Soluções <a name="problemas-comuns-e-solucoes"></a>

### 8.1 Erro ao Conectar ao Banco de Dados
- **Causa**: Credenciais incorretas no `.env` ou MySQL não iniciado.
- **Solução**: Verifique se o MySQL está rodando e se as credenciais no `.env` estão corretas.

### 8.2 `ModuleNotFoundError: No module named 'mysql'`
- **Causa**: Dependências não instaladas.
- **Solução**: Execute `pip install -r requirements.txt`.

### 8.3 `sqlalchemy.exc.OperationalError: (mysql.connector.errors.ProgrammingError) (1049, "Unknown database 'locadora6'")`
- **Causa**: O banco de dados não foi criado.
- **Solução**: Rode `python main.py` novamente para criar o banco automaticamente.

---
### Agora você está pronto para rodar o sistema! 🚀


