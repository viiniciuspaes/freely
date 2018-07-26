### Projeto de Banco de Dados (2018.1)
> (Python + SQL) <br>
>Bacharelado em Sistemas de Informação - UFRPE <br>

### Índice
  * [1) Objetivos]
  * [2) Instalação do ambiente e execução]
  * [3) Documentação]
  * [4) Equipe]
  * [5) Limitações e dúvidas]
  
### Objetivos

- [x] Procurar tweets de acordo com hashtags relacionadas a figuras públicas e candidatos das eleições de 2018;
- [x] Criar uma base de dados (SQL) com os tweets coletados;
- [X] Análise de sentimentos utilizando Naive Bayes sobre os textos dos tweets;
- [x] Construir consultas e visualizações gráficas através do bando de dados;  

### Instalação do ambiente e execução

* 1.1) Primeiramente é necessário ter instalado no seu sistema:

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

### Limitações e dúvidas

* 5.1) Da coleta de dados:
A extração dos dados pode ser pouco satisfatória. A API do Twitter, acessada através do Twepy, limita a coleta direta de tweets para somente sete dias após a coleta dos dados. Isto dificulta a coleta de dados históricos. Uma alternativa que auxilia nesta coleta é o Selenium, ferramenta de autamização para uso de web browsers. Este caminho facilita bastante na coleta, agora podendo realizar consultas histórias, mas deixa este processo mais lento, tendo em vista que cada busca no Twitter necessita de um navegador aberto.
* 5.1.1) Possível solução:
Usando Jupyter Notebook com vários notebooks rodando ao mesmo tempo

* 5.2) Da análise de sentimento:
Problemas com os percentuais e as métricas, acurácia, etc
Problemas de linguagem de pt/en

* 5.2.1) Possível solução:
 LinguaKit, lib em Perl, mas com os problemas encontrados se tornou na verdade uma barreira utilizar o LinguaKit
 
* 5.3) Do período e tempo de desenvolvimento:
Com mais tempo e um cronograma mais organizado a ideia do projeto poderia ser melhor analisada. Desde a escolha das ferramentas até a apresentação dos resultados, o tempo para realização de todas as etapas não é o suficiente para criar uma ferramenta realmente completa e que abranja diversos casos.

* 5.4) Demais limitações e possíveis dúvidas:
Levando em consideração a construção do projeto, desde sua concepção como ideia até o momento até o seu desenvolvimento atual diversas limitações foram encontradas. Limitações instrumentais ou de tempo, pontos que não foram abordados durante a construção e modelagem do projeto. Este projeto chega neste ponto apresentando limitações, que mesmo com o escopo reduzido ainda não sabemos ao certo até que ponto as limitações encontradas até o momento realmente afetam o uso geral do projeto como ferramenta.
Deste ponto nós, a equipe de desenvolvimento deixamos aberta a discussão e prosseguimento do projeto para sua continuidade ou não. Novos problemas, dúvidas, soluções e melhorias podem ser feitas e são encorajadas.

* 5.5) Contato sobre qualquer tema relacionado ao projeto:
[pbd2018[dot]1[at]gmail[dot]com](mailto:pbd2012.1@gmail.com)
