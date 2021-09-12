  # [Miridam] - Projeto de controle de equipamentos
## para que serve esse projeto?

Esse projeto surgiu como minha proposta de melhoria para controle de equipamentos na empresa onde trabalho. Usamos bastante excel(nada contra quem usa excel para controle de alguma coisa), mas preciso de um sistema mais especifico onde eu possa cadastrar departamentos, equipamentos, IP's etc... 

E sim, o projeto é bem simples, pois a necessidade é simples.  Porém pretendo fazer várias novas funcionaldidas. Mas por enquanto as funcionalidades que tem são essas:
## Funcionalidades
- Cadastro de Equipamentos
- Atribuição de IP (IPv4 e IPv6) para cada equipamento
- Cadastro de Departamentos
- Gerar PDF 

## Desenvolvimento

O que está sendo usado pra desenvolver? essas são as bibliotecas e frameworks que estou usando para desenvolver esse projeto.
- [Django] - versão 3.2.6
- [Python] - Versão 3.9
- [Bootstrap] - Versão 5,0.
- [Coverage] - Para ajudar na analise do que precisa ser testado.
- [Python-Decouple] - Biblioteca para desacoplamento de variáveis de ambientes


## Run Project
Para rodar o projeto no seu computador faça o clone do projeto e instale as bilbiotecas.
- Dentro do projeto crie um ambiente virtual 

```sh
python -m venv venv 
venv\Scripts\activate
```

- Instale as dependências

```sh
pip install -r requirements. txt
```
- Configure as variaveis de amebiente com o python-decouple

```sh
https://github.com/henriquebastos/python-decouple
```

