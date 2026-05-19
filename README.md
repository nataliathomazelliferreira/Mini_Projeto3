# Mini Projeto 3 - Consumo de APIs

Projeto desenvolvido em Python para a matéria de Linguagem de Programação II.

O objetivo do projeto é demonstrar a comunicação entre dois sistemas:

- um servidor de API;
- um cliente que consome os dados dessa API.

Neste projeto, foi criada uma API chamada Word of the Day API. Ela disponibiliza palavras em inglês com tradução, exemplo de uso e nível de dificuldade. Além disso, o projeto possui um cliente em Python que acessa essa API e exibe os dados no terminal.

## Tema do projeto

Word of the Day API

A ideia do projeto é criar uma API simples para estudo de vocabulário em inglês.

Cada palavra cadastrada possui:

- id;
- palavra em inglês;
- tradução em português;
- exemplo de uso;
- nível de dificuldade.

## Tecnologias utilizadas

* Python
* FastAPI
* Uvicorn
* Requests

## O que cada tecnologia faz

### Python

Linguagem principal utilizada no projeto.

### FastAPI

Biblioteca usada para criar o servidor da API.

Com o FastAPI, foram criados os endpoints que retornam os dados em formato JSON.

### Uvicorn

Servidor usado para executar a aplicação FastAPI.

O FastAPI define as rotas, mas quem abre o servidor local para acesso pelo navegador é o Uvicorn.

### Requests

Biblioteca usada no cliente Python para consumir os dados da API.

O cliente usa Requests para acessar os endpoints do servidor.

## Estrutura do projeto

```text
Mini_Projeto3/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── client/
│   └── client.py
│
└── server/
    └── app/
        ├── __init__.py
        ├── data.py
        └── main.py
```

## Função de cada arquivo

### README.md

Arquivo de documentação do projeto.

Explica o objetivo do projeto, as tecnologias utilizadas, a estrutura de pastas e como executar o sistema.

### requirements.txt

Arquivo que lista as bibliotecas necessárias para executar o projeto.

Conteúdo esperado:

```txt
fastapi
uvicorn
requests
```

### .gitignore

Arquivo usado para impedir que arquivos desnecessários sejam enviados para o GitHub.

Exemplo de arquivos ignorados:

* ambiente virtual;
* arquivos temporários do Python;
* arquivos de cache.

### server/app/main.py

Arquivo principal do servidor.

Ele cria a aplicação FastAPI e define os endpoints da API.

Principais endpoints:

* `/`
* `/status`
* `/words`
* `/words/random`
* `/words/{word_id}`

### server/app/data.py

Arquivo onde ficam os dados utilizados pela API.

Neste projeto, ele armazena a lista de palavras em inglês.

### server/app/**init**.py

Arquivo que indica ao Python que a pasta `app` faz parte de um pacote Python.

Ele pode ficar vazio.

### client/client.py

Arquivo do cliente.

Ele consome os dados da API usando a biblioteca Requests.

O cliente permite:

* ver uma palavra aleatória;
* listar todas as palavras cadastradas;
* encerrar o programa.

## Endpoints da API

### Página inicial

```text
GET /
```

Exibe uma página web simples com uma palavra do dia.

Acesso pelo navegador:

```text
http://127.0.0.1:8000
```

### Verificar status da API

```text
GET /status
```

Retorna se a API está online.

Exemplo de resposta:

```json
{
  "status": "online"
}
```

### Listar todas as palavras

```text
GET /words
```

Retorna todas as palavras cadastradas na API.

Acesso pelo navegador:

```text
http://127.0.0.1:8000/words
```

### Buscar palavra aleatória

```text
GET /words/random
```

Retorna uma palavra aleatória.

Acesso pelo navegador:

```text
http://127.0.0.1:8000/words/random
```

### Buscar palavra por ID

```text
GET /words/{word_id}
```

Exemplo:

```text
http://127.0.0.1:8000/words/1
```

Se o ID existir, a API retorna a palavra correspondente.

Se o ID não existir, a API retorna erro 404.

## Como Executar

Para executar o projeto, siga o passo a passo abaixo.

## 1. Abrir o Prompt de Comando ou PowerShell

No Windows, pesquise por:

```text
Prompt de Comando
```

ou:

```text
cmd
```

Também pode usar o PowerShell ou o terminal integrado do Visual Studio Code.

## 2. Escolher onde o projeto será salvo

Entre na pasta onde deseja salvar o projeto.

Exemplo:

```bash
cd Desktop
```

ou:

```bash
cd Documents
```

Também é possível digitar:

```bash
cd 
```

com um espaço depois do `cd` e apertar a tecla Tab para o terminal mostrar as pastas disponíveis.

Continue apertando Tab até encontrar a pasta desejada.

Quando a pasta correta aparecer, pressione Enter.

## 3. Clonar o repositório

Depois de entrar na pasta escolhida, clone o repositório:

```bash
git clone https://github.com/nataliathomazelliferreira/Mini_Projeto3.git
```

## 4. Entrar na pasta do projeto

Após clonar, entre na pasta do projeto:

```bash
cd Mini_Projeto3
```

## 5. Criar o ambiente virtual

Crie um ambiente virtual Python:

```bash
python -m venv .venv
```

Caso o comando acima não funcione, tente:

```bash
py -m venv .venv
```

## 6. Ativar o ambiente virtual

No Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

No Prompt de Comando:

```bash
.venv\Scripts\activate
```

Quando o ambiente virtual estiver ativo, aparecerá algo parecido com:

```text
(.venv)
```

antes do caminho do terminal.

## 7. Instalar as dependências

Com o ambiente virtual ativo, instale as bibliotecas do projeto:

```bash
pip install -r requirements.txt
```

Esse comando instala:

* FastAPI;
* Uvicorn;
* Requests.

## 8. Rodar o servidor da API

Com o terminal dentro da pasta do projeto, execute:

```bash
python -m uvicorn server.app.main:app --reload
```

Se tudo estiver correto, aparecerá uma mensagem parecida com:

```text
Uvicorn running on http://127.0.0.1:8000
```

Isso significa que o servidor está rodando.

## 9. Acessar a página web

Com o servidor ligado, abra o navegador e acesse:

```text
http://127.0.0.1:8000
```

Essa página mostra a Word of the Day em formato visual.

## 10. Acessar a documentação automática da API

O FastAPI gera uma documentação automática.

Acesse:

```text
http://127.0.0.1:8000/docs
```

Nessa página, é possível testar os endpoints da API.

## 11. Rodar o cliente

Para rodar o cliente, mantenha o servidor ligado.

Abra outro terminal dentro da pasta do projeto.

Ative o ambiente virtual novamente:

```bash
.venv\Scripts\Activate.ps1
```

Depois execute:

```bash
python client/client.py
```

Caso o comando acima não funcione, tente:

```bash
py client/client.py
```

O cliente exibirá um menu no terminal:

```text
Word of the Day Client
1 - Ver palavra do dia
2 - Listar todas as palavras
0 - Sair
```

Digite uma opção e pressione Enter.

## Resumo dos comandos

```bash
cd Desktop
git clone https://github.com/nataliathomazelliferreira/Mini_Projeto3.git
cd Mini_Projeto3
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn server.app.main:app --reload
```

Em outro terminal, para executar o cliente:

```bash
cd Desktop
cd Mini_Projeto3
.venv\Scripts\Activate.ps1
python client/client.py
```

Caso necessário:

```bash
py client/client.py
```

## Observação importante

O arquivo `server/app/main.py` não deve ser executado diretamente.

Não use:

```bash
python server/app/main.py
```

O servidor deve ser iniciado com:

```bash
python -m uvicorn server.app.main:app --reload
```

## Funcionalidades implementadas

* Criação de servidor API com FastAPI
* Criação de cliente em Python consumindo a API
* Retorno de dados em JSON
* Página web simples para visualização da palavra do dia
* Endpoint para listar todas as palavras
* Endpoint para retornar palavra aleatória
* Endpoint para buscar palavra por ID
* Organização em pastas separando servidor, cliente e dados

## Sobre o consumo de API

O consumo da API acontece no arquivo:

```text
client/client.py
```

O cliente usa a biblioteca Requests para acessar os endpoints do servidor.

Exemplo:

```python
response = requests.get(f"{api_url}/words/random")
```

Esse comando envia uma requisição GET para a API e recebe os dados retornados pelo servidor.
