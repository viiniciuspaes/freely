### Projeto de Banco de Dados (2018.1)
> (Python + SQL) <br>
>Bacharelado em Sistemas de Informação - UFRPE <br>

### Índice
  * [1) Objetivos](https://github.com/viiniciuspaes/freely/blob/master/README.md#objetivos)
  * [2) Instalação do ambiente e execução](https://github.com/viiniciuspaes/freely/blob/master/README.md#instala%C3%A7%C3%A3o-do-ambiente-e-execu%C3%A7%C3%A3o)
  * [3) Documentação](https://github.com/viiniciuspaes/freely/blob/master/README.md#documenta%C3%A7%C3%A3o)
  * [4) Equipe](https://github.com/viiniciuspaes/freely/blob/master/README.md#equipe)
  * [5) Limitações](https://github.com/viiniciuspaes/freely/blob/master/README.md#limita%C3%A7%C3%B5es)
  * [6) Trabalhos futuros](https://github.com/viiniciuspaes/freely/blob/master/README.md#trabalhos-futuros)
  
### Objetivos

- [x] Procurar tweets de acordo com hashtags relacionadas à figuras públicas e candidatos das eleições de 2018;
- [x] Criar uma base de dados (SQL) com os tweets coletados;
- [X] Análise de sentimentos utilizando Naive Bayes sobre os textos dos tweets;
- [x] Construir consultas e visualizações gráficas através do bando de dados;  

### Instalação do ambiente e execução

* 1.1) Primeiramente é necessário ter instalado no seu sistema os seguintes itens:

- [x] [Python 3.4 ou superior](https://www.python.org/downloads/)
- [x] [Google Chrome](https://www.google.com/chrome/)

* 1.1.1) Após a instalação verificar se o python foi corretamente instalado através do terminal, ou cmd, usando o do comando:
```
$ python -V
```

* 1.2) Instale o pip no seu sistema:

- [Windows](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows)
- [Linux](https://www.tecmint.com/install-pip-in-linux/)

* 1.2.1) Após instalar o pip, verificar se está corretamente instalado:
```
$ pip --version
``` 
* 1.3) Com o pip instalado clone o repositório do projeto no Github: https://github.com/viiniciuspaes/freely

* 1.4) Dentro do diretório onde o repositório foi clonado verifique a existência do arquivo "requirements.txt".

* 1.4.1) Caso este arquivo não seja encontrado verificar se o repositório foi baixado corretamente. Neste arquivo constam todas as bibliotecas utilizadas dentro do projeto, suas dependências e respectivas versões.

* 1.5) Dentro do diretório onde o repositório foi clonado, através do terminal ou cmd realize o comando:
```
$ pip install -r requirements.txt
``` 
* 1.5.1) Um Warning ocorrerá caso exista algum erro ou falha na instalação, verifique corretamente este processo. Caso seja necessário verifique também se ocorreu algum erro na instalação de uma biblioteca específica. Ela pode ser instalada pelo comando:
```
$ pip install <nome_da_biblioteca>
``` 

* 1.6) Após isso inicie a API dentro do repositório do projeto pelo terminal ou cmd com o comando:
```
$ python app.py
``` 
* 1.7) Iniciando a API todas as operaçõas definidas no sistema tem início: da extração dos dados e seus tratamentos até a análise de sentimentos. O intuito com essa estrutura é facilitar a utilização e a modularização do sistema.

### Documentação

Todos os documentos usados como referência durante o desenvolvimento do projeto estão disponíveis para acesso nos itens abaixo.

* [Documento de casos de uso](https://drive.google.com/open?id=1OEzvLkxBw_MOFRknqc1yCeZPg0tvCIMK)
* [Diagrama ER](https://drive.google.com/open?id=1OEzvLkxBw_MOFRknqc1yCeZPg0tvCIMK)
* [Modelo lógico do BD](https://drive.google.com/open?id=1OEzvLkxBw_MOFRknqc1yCeZPg0tvCIMK)
* [Script SQL](https://drive.google.com/open?id=1OEzvLkxBw_MOFRknqc1yCeZPg0tvCIMK)

### Equipe

- [Francisco Queiroga](https://github.com/chicoqueiroga)<br>
- [Luiz Carlos](https://github.com/xRuisux)<br>
- [Manoel Freitas](https://github.com/manoelfneto)<br>
- [Vinícius Paes](https://github.com/viiniciuspaes)<br>

### Limitações

* 5.1) Da coleta de dados:
A API do Twitter, acessada através do Twepy, limita a coleta direta de tweets para somente sete dias a partir da data da consulta realizada. Isto dificulta a coleta de dados históricos, as limitações sobre as datas foi um empecilho inicial. Uma alternativa de auxílio nesta coleta é o Selenium, ferramenta de autamização para uso em web browsers. Por meio do Selenium a coleta se torna, agora podendo realizar consultas histórias mas deixa a extração mais lenta, tendo em vista que cada busca no Twitter necessita do navegador aberto.

* 5.2) Da análise de sentimento:
O Scikit-Learn permite analisar métricas, como validação cruzada e de medição de acurácia do modelo. Foram eleitas algumas métricas e através delas percebe-se que o modelo precisa ser melhorado. Isto ocorre por diversos fatores, dos quais a equipe não conseguiu identificar ou explorar estas limitações. Levando em consideração também o primeiro contato com técnicas de análise de texto e análise de sentimento o modelo usado é simples e tenta ser o mais prático possível para um projeto realizado dentro de uma disciplina.
 
* 5.3) Período de desenvolvimento:
O tempo e um cronograma limitam também as possibilidades para finalização do projeto. Desde a escolha das ferramentas até a apresentação dos resultados, o tempo para realização de todas as etapas não foi o suficiente para criar uma ferramenta realmente completa e que abranjisse uma gama realmente grande de usos.

* 5.4) Demais limitações e possíveis dúvidas:
Levando em consideração a construção do projeto, desde sua concepção como ideia até o momento de seu desenvolvimento atual, diversas limitações foram encontradas: limitações instrumentais ou de tempo, pontos que não foram abordados durante a construção e modelagem do projeto e afins. Com um escopo reduzido a equipe não sabe ao certo até que ponto as limitações encontradas até o momento realmente afetam o uso geral do projeto como ferramenta. Deste ponto a equipe de desenvolvimento deixa aberta a discussão e prosseguimento do projeto para sua continuidade ou não. Novos problemas, soluções e melhorias podem ser feitas e são encorajadas.

### Trabalhos futuros

* 6.1) Usando notebooks para coleta:
No ponto 5.1 identificamos algumas limitações da coleta. Usando Jupyter Notebook poderíamos abrir várias intâncias, vários notebooks que realizariam consultas simultâneas virtualmente. Este método não pôde ser implementado por falta de conhecimento da ferramenta, as datas de entrega não permitiram uma maior exploração do Jupyter Notebook.

* 6.2) LinguaKit:
O LinguaKit é uma ferramenta de análise multilinguagem. É um projeto desenvolvido em Perl e tem repositório [público](https://github.com/citiususc/Linguakit). Através da documentação disponibilizada podemos realizar consultas e testar os seus módulos, um deles realiza análise de sentimentos. O LinguaKit já suporta português, facilitando assim a análise. Numa continuação do projeto seria ideal testar mais a base do LinguaKit e suas métricas, avaliando sua acurácia, melhorando assim o modelo para análise de sentimentos.
