# API Jogo Da Velha - Lucas Assunção Costa

**API criada para solução do desafio proposto pela DTI**

Conteúdo do Readme:
-Introdução
-Como Rodar
-Como foi feito

# Introdução

  Este projeto refere-se ao desafio proposto pela DTI Digital no dia 9/12/2019 como forma de avaliação da 2a fase do processo seletivo. O desafio consiste na criação de uma API (Interface de programação de aplicações) para um jogo da velha. O programa então deve receber argumentos via URL e retorná-los em forma de JSON's (JavaScript Object Notation).
  Para resolução do desafio foi utilizada a linguagem python na sua versão 3.7. A escolha da liguagem para a resolução se deve a sua portabilidade, permitindo não somente rodar a aplicação em diversos dispositivos, mas também abrir mão da necessidade do uso de um servidor e de um banco de dados para a execução do programa. Diversas bibliotecas foram usadas para a resolução do problema, entre elas *flask, flask_restful e json*.
 
# Como Rodar
 
 *Método simples*
 
 1) Baixe a pasta JogoDaVelhaAPI
 
 Windows
    2) baixe o ambiente python em seu computador por meio deste link: https://www.python.org/downloads/ , deixando a opção de adicionar python à variável de ambiente na instalação:
      
      ![alt text](https://datatofish.com/wp-content/uploads/2019/03/000_pyinstaller.png)
      
   2.1) Va ao diretório *JogoDaVelhaAPI/Dist/api* e abra o arquivo api.exe
 Linux
    2) Abra o diretório *JogoDaVelhaAPI/Dist/api* no terminal e rode o comando > ./api
 
 3) abra seu navegador de preferência, a url base da api é *127.0.0.1:5000*, porém esta por sí não gera retorno nenhum. As URL's com suas respectivas funções são listadas à seguir.
 
|     URL       |     Função    |
| ------------- | ------------- |
| 127.0.0.1:5000/game| Cria um novo jogo e retorna seu id e o primeiro jogador à jogar. |
| 127.0.0.1:5000/game/(id)/(objeto JSON) | dasd  |

``` python
  print(hello)
```
