# coding: utf8
from flask import Flask
from flask_restful import Api, Resource, reqparse
import random,json,string

# Objeto da biblioteca Flask
app = Flask(__name__)

# array de objetos "jogo"
jogos = []

# função que checa as condições de vitória
def checaVitoria(tabuleiro): # significado dos returns: 0 - vitoria, 1 - continua, 2 - empate
  if tabuleiro["0"]["0"] == tabuleiro["1"]["1"] and tabuleiro["1"]["1"] == tabuleiro["2"]["2"] and tabuleiro["1"]["1"] != "0":
    return 0 
  if tabuleiro["2"]["0"] == tabuleiro["1"]["1"] and tabuleiro["1"]["1"] == tabuleiro["0"]["2"] and tabuleiro["1"]["1"] != "0":
    return 0

  for x in range(3):
    if tabuleiro[str(x)]["0"] == tabuleiro[str(x)]["1"] and tabuleiro[str(x)]["0"] == tabuleiro[str(x)]["2"] and tabuleiro[str(x)]["0"] != "0":
      return 0    
    elif tabuleiro["0"][str(x)] == tabuleiro["1"][str(x)] and tabuleiro["0"][str(x)] == tabuleiro["2"][str(x)] and tabuleiro["0"][str(x)] != "0":
      return 0
      
  for x in range(3):  
    if tabuleiro["0"][str(x)] == "0" or tabuleiro["1"][str(x)] == "0" or tabuleiro["2"][str(x)] == "0":
      return 1
  return 2

@app.route('/game') # função que cria o jogo novo e armazena no array de jogos local
def criaJogo():
  cod = ''.join(random.choice( string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(8))
  jogador = ["X","O"]
  primeiro = jogador[random.randint(0, 1)]
  jogo = {"id" : cod, "proximoPlayer" : primeiro, "tabuleiro" : {"0":{"0":"0","1":"0","2":"0"},"1":{"0":"0","1":"0","2":"0"},"2":{"0":"0","1":"0","2":"0"}}}
  jogos.append(jogo)

  jogo = {"id" : cod, "firstPlayer" : primeiro}
  return jogo

@app.route('/game/<string:idJogada>/<string:jogada>') # função que efetua a jogada de acordo com a url enviada
def movimenta(idJogada,jogada):
  jogador = jogada[0] # o primeiro parâmetro recebido é o jogador que está efetuando a jogada
  x = jogada[1] # o segundo é a posição x da jogada
  y = jogada[2] # o terceiro é a posição y da jogada

  # testes de retorno
  for jogo in jogos:
    if idJogada == jogo["id"]: # se o jogo requisitado for encontrado
      if jogador.upper() == jogo["proximoPlayer"]: # se é realmente a vez do jogador
        if jogo["tabuleiro"][x][y] == "0": # se a casa está livre
          jogo["tabuleiro"][x][y] = jogador
          if jogador.upper() == "X": 
            jogo["proximoPlayer"] = "O" # seta o próximo jogador para O
          else:
            jogo["proximoPlayer"] = "X" # seta o próximo jogador para X

          if checaVitoria(jogo["tabuleiro"]) == 0: # se a função retornar 0, o jogador atual ganhou
            return json.loads('{"msg":"Partida finalizada","winner":"'+jogador.upper()+'"}')
          elif checaVitoria(jogo["tabuleiro"]) == 1: # se a função retornar 1, o jogo continua, código 200 é retornado
            return "200"
          elif checaVitoria(jogo["tabuleiro"]) == 2: # se a função retorna 2, o jogo deu velha
            return json.loads('{"msg":"Partida finalizada","winner":"draw"}')
        else:
          return json.loads('{"msg" : "Casa ocupada"}')
      else:
        return json.loads('{"msg" : "Não é o turno do jogador"}')
  
  return json.loads('{"msg" : "Partida não encontrada"}')
  
if __name__ == '__main__':
    app.run(debug=True)

