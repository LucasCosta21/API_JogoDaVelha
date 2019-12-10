# API Jogo Da Velha - Lucas Assunção Costa

**API criada para solução do desafio proposto pela DTI**

Conteúdo do Readme:

-Introdução

-Como Rodar

-Funcionamento da biblioteca flasks

# Introdução

  Este projeto refere-se ao desafio proposto pela DTI Digital no dia 9/12/2019 como forma de avaliação da 2a fase do processo seletivo. O desafio consiste na criação de uma API (Interface de programação de aplicações) para um jogo da velha. O programa então deve receber argumentos via URL e retorná-los em forma de JSON's (JavaScript Object Notation).
  Para resolução do desafio foi utilizada a linguagem python na sua versão 3.7. A escolha da liguagem para a resolução se deve a sua portabilidade, permitindo não somente rodar a aplicação em diversos dispositivos, mas também abrir mão da necessidade do uso de um servidor e de um banco de dados para a execução do programa. Diversas bibliotecas foram usadas para a resolução do problema, entre elas *flask, flask_restful e json*.
 
# Como Rodar

 1) Baixe o arquivo JogoDaVelhaAPI
 
 1.1) *somente no windows*, baixe o ambiente python em seu computador por meio deste link: https://www.python.org/downloads/ , deixando a opção de adicionar python à variável de ambiente na instalação:
      
   ![Caixa para ser selecionada](https://datatofish.com/wp-content/uploads/2019/03/000_pyinstaller.png)
       
 2) Abra o diretório "/api" (disponivel aqui no git) no terminal (linux ou windows) e rode o seguinte comando > pip install flask flask_restful
 
 3) Ainda no diretório "api", no terminal rode o seguinte comando > python ./api.py
 
 4) abra seu navegador de preferência, a url base da api é *127.0.0.1:5000*, porém esta por sí não gera retorno nenhum. As URL's com suas respectivas funções são listadas à seguir.
 
|     URL       |     Função    |
| ------------- | ------------- |
| 127.0.0.1:5000/game| Cria um novo jogo e retorna seu id e o primeiro jogador à jogar. |
| 127.0.0.1:5000/game/(id)/(objeto JSON) | faz uma jogada em forma de um (objeto JSON) no jogo com o id|

  Na segunda URL temos como segundo parâmetro um objeto JSON (sem espaços em branco), tal objeto tem o formato:
  ```json
  {"jogador":"letra do jogador(X ou O)","x":"posição x da jogada","y":"posição y da jogada"}
  ```
  Exemplo prático:
  ```json
  {"jogador":"O","x":"2","y":"1"}
  ```
  
  Esta forma de realizar a jogada atribui dinamicidade à API.
  
# Funcionamento da biblioteca flasks

  A biblioteca flasks permite atribuir as rotas da nossa aplicação à funções definidas no código, sua sintaxe é a seguinte

``` python
@app.route('/rota') # rota na url
def funcaoExemplo(): # funcao que será chamada
  return "Olá Mundo"
```
exemplo usado no código:
``` python
@app.route('/game')
def criaJogo():
    cod = ''.join(random.choice( string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(8))
    jogador = ["X","O"]
    primeiro = jogador[random.randint(0, 1)]
    jogo = {"id" : cod, "proximoPlayer" : primeiro, "tabuleiro" : {"0":{"0":"0","1":"0","2":"0"},"1":{"0":"0","1":"0","2":"0"},"2":{"0":"0","1":"0","2":"0"}}}
    jogos.append(jogo)

    jogo = {"id" : cod, "firstPlayer" : primeiro}
    return jogo
```

  Quando os módulos do flask estiverem ativados portanto, a rota "/rota" exibirá "Olá Mundo" na tela.
