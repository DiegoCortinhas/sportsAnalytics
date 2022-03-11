# SportsAnalytics - Otimização combinatória aplicada a composição de equipes esportivas

O presente código fonte foi desenvolvido por Diego Pereira Cortinhas e Diogo Alves da Silva, em trabalho de conclusão de curso no Bacharelado em Ciência da Computação do CEFET/RJ (Centro Federal de Educação Tecnológica Celso Suckow da Fonseca). Os respectivos perfis no Linkedin dos autores são: [https://www.linkedin.com/in/diegocortinhas/](https://www.linkedin.com/in/diegocortinhas/) e [https://www.linkedin.com/in/diogoalvespe/](https://www.linkedin.com/in/diogoalvespe/)

## 1 - Pré requisitos
Você precisará ter instalado em sua máquina o Python (versão 3 ou superior) e banco de dados MySQL (versão 8 ou superior). Estes programas podem ser encontrados, respectivamente, em: [https://www.python.org/downloads/](https://www.python.org/downloads/) e [https://www.mysql.com/downloads/](https://www.mysql.com/downloads/). 

**OBS: O código não foi testado em versões anteriores do Python e do MySQL, portanto não é garantido o funcionamento do programa em versões diferentes das citadas.**

## 2 - Carregando a Base de dados
Para executar o programa corretamente, é preciso ter a sua base de dados configurada. Para isso, faça o upload do arquivo ```base_cartolafc.sql``` na sua base

## 3 - Instalando dependências necessárias para executar o programa
Para execução do código fonte é preciso instalar algumas bibliotecas Python. Para isso, utilizando o gerenciador de pacotes PIP, com o seguinte comando: 

``` pip install -r requirements.txt ```

## 4 - Como executar o programa
Após instalação das dependências via PIP, execute o programa utilizando o comando:

``` python Optimizer.py ```

Para facilitar a análise dos resultados, é possível ainda salvar o output do programa em um arquivo TXT. Para isso, utilize o seguinte comando:

``` python Optimizer.py > NOME_ARQUIVO.txt ```

Um exemplo de output do programa pode ser visto abaixo: 

![Exemplo do Código fonte sendo executado](https://cdn.programadoresbrasil.com.br/wp-content/uploads/2022/03/ouput%20codigo%20tcc.PNG "Exemplo do Código fonte sendo executado")
