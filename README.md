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
- [x] [MySQL](https://www.mysql.com/)
- [x] [XAMP](https://www.apachefriends.org/pt_br/index.html)
* 1.1.1) Após a instalação, verificar se o python foi corretamente instalado através do terminal, ou cmd, usando o do comando:
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
* 1.6) Com os requisitos instalados corretamente é necessário iniciar o MySQL pelo XAMP.

* 1.7) É necessário verificar no arquivo [db_helper.py](https://github.com/viiniciuspaes/freely/blob/master/database/db_helper.py), localizado na pasta database, as credênciais do banco de dados. O padrão utilizado é:
```
usuário = "root"
senha = ""
endereço = "localhost"
```
Caso queira alterar os valores acima é preciso modificar os valores entre aspas nas linhas 81, 82 e 83 do db_helper.py .

* 1.8) Por padrão, qualquer arquivo que está sendo utilizado no projeto está sendo encaminhado através do seu caminho relativo. No Windows pode ocorrer problemas com este uso, sendo ideal a passagem do caminho completo do arquivo da seguinte maneira:
```
driver = webdriver.Chrome(executable_path=r"C:\Users\user\Doc\PytonProjects\freely\controllers\chromedriver.exe")
```
Neste exemplo nós estamos referenciando um arquivo "chromedriver.exe" através do seu caminho completo. Lembrando sempre que no caso da barra invertida deve-se colocar a letra "r" antes do caminho, como no exemplo. É necessário verificar o caminho do arquivo a seguir para evitar erros:

-[x] ["chromedriver.exe" na linha 12 do miner.py, na pasta controllers](https://github.com/viiniciuspaes/freely/blob/master/controllers/miner.py)

* 1.6) Após isso, através do cmd/terminal, acesse a pasta onde o repositório foi salvo. Tendo cumprindo todos os passos e com as instalações dos requerimentos do passo 1.5 feitas corretamente, execute o seguinte comando no cmd ou terminal:
```
$ python app.py
``` 
* 1.7) Iniciando a API, com o banco conectado através do XAMP, agora pode-se acessar através do navegador o servidor do Flask, em local host, pelo endereço:
```
http://127.0.0.1:5000
```


### Documentação

Todos os documentos usados como referência durante o desenvolvimento do projeto estão disponíveis para acesso nos itens abaixo.

* [Documento de casos de uso](https://drive.google.com/open?id=1NjK3JTpw0MjimRbSNqUANL1y-j7juYI8)
* [Diagrama ER](https://drive.google.com/open?id=1nxWzu9YhKJBV49E34CKFyUv0M9RZIgsg)
* [Modelo lógico do BD](https://drive.google.com/open?id=1H8sDyxHKJmePFIiRZaIDT7AZJmGPhIbj)
* [Script SQL](https://drive.google.com/open?id=1N5iPoI7fup40Db_rS4G7J3tRTofpuc9l)

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

* 5.5) Da classificação de fontes e FakeNews:
Com o tempo decorrido e as pesquisas feitas o possível a ser entregue foi a classificação de fontes através de perfis no Twitter ou páginas compartilhas de maneira manual, isso levando em consideração pesquisas [encontrada](https://arxiv.org/pdf/1712.05999.pdf). Métodos de automação deste módulo não foram bem sucedido e descontinuados devido ao tempo de desenvolvimento não ser o suficiente para dar continuidade. Pesquisas também sobre APIs abertas que fizessem uma classificação de  notícias não tiveram um resultado satisfatório.

* 5.4) Demais limitações e possíveis dúvidas:
Levando em consideração a construção do projeto, desde sua concepção como ideia até o momento de seu desenvolvimento atual, diversas limitações foram encontradas: limitações instrumentais ou de tempo, pontos que não foram abordados durante a construção e modelagem do projeto e afins. Com um escopo reduzido a equipe não sabe ao certo até que ponto as limitações encontradas até o momento realmente afetam o uso geral do projeto como ferramenta. Deste ponto a equipe de desenvolvimento deixa aberta a discussão e prosseguimento do projeto para sua continuidade ou não. Novos problemas, soluções e melhorias podem ser feitas e são encorajadas.

### Trabalhos futuros

* 6.1) Usando notebooks para coleta(paralelização de tarefas):
No ponto 5.1 identificamos algumas limitações da coleta. Usando Jupyter Notebook poderíamos abrir várias intâncias, notebooks que realizariam consultas simultâneas virtualmente. Este método não pôde ser implementado por falta de conhecimento da ferramenta, as datas de entrega não permitiram uma maior exploração do Jupyter Notebook. Se a realização das tarefas pudesse ser feita paralelamente o processo todo seria agilizado.

* 6.2) LinguaKit(método de classificação de sentimento):
O LinguaKit é uma ferramenta de análise multilinguagem. É um projeto desenvolvido em Perl e tem repositório [público](https://github.com/citiususc/Linguakit). Através da documentação disponibilizada podemos realizar consultas e testar os seus módulos, um deles realiza análise de sentimentos. O LinguaKit já suporta português, facilitando assim a análise. Numa continuação do projeto seria ideal testar mais a base do LinguaKit e suas métricas, avaliando sua acurácia, melhorando assim o modelo para análise de sentimentos.

* 6.3) Botometer(ferramentas de reconhecimento de conhecimento):
O [Botometer](https://botometer.iuni.iu.edu/#!/) é um algoritmo de aprendizado de máquina que consegue classificar uma conta no Twitter como sendo uma pessoa real ou um bot. Com sua API sendo aberta pode-se ampliar a gama de busca de fakes no Twitter e também melhorar os módulos de automação para classificação da aplicação.

* 6.4) Classificação de FakeNews e reprodução de notícias:
A classificação literal de uma notícia falsa leva em consideração muitas variáveis. Quem compartilha, quais as fontes, em que plataformas são divulgadas, e várias coisas mais. Essas variáveis são difíceis de classificar automaticamente, mas já existem estudos, APIs e plataformas para o auxílio do reconhecimento de FakeNews, como exemplo o [Fato ou Fake](https://g1.globo.com/fato-ou-fake/), do G1. Uma possível melhoria, ou pesquisa para o futuro, seria uma catalogação de plataformas, ferramentas e afins. Com isto é possível visualizar melhor o que pode ser feito sobre classificação de FakeNews e o que pode-se usar nos dias atuais.

* 6.5) Matplotlib e Pandas(ciência de dados e visualização):
O [Matplotlib](https://matplotlib.org/) e o [Pandas](https://pandas.pydata.org/) são ferramentas muito boas para auxílio no tratamento de dados. Somando isso com estudo de dados e a visualização gráfica, o intuito disto seria aperfeiçoas as análises feitas através de demonstrações visuais de alta capacidade para o usuário.
