# coding: utf8
from flask import Flask
from flask_restful import Api, Resource, reqparse
import random,json,string

app = Flask(__name__)

# array de objetos "jogo"
jogos = []

def checaVitoria(tabuleiro): # 0 - vitoria, 1 - continua, 2 - empate
    for x in range(3):
      if tabuleiro[str(x)]["0"] == tabuleiro[str(x)]["1"] and tabuleiro[str(x)]["0"] == tabuleiro[str(x)]["2"]:
        return 0    
      elif tabuleiro["0"][str(x)] == tabuleiro["1"][str(x)] and tabuleiro["0"][str(x)] == tabuleiro["2"][str(x)]:
        return 0

    if tabuleiro["0"]["0"] == tabuleiro["1"]["1"] and tabuleiro["1"]["1"] == tabuleiro["2"]["2"]:
      return 0 
    if tabuleiro["2"]["0"] == tabuleiro["1"]["1"] and tabuleiro["1"]["1"] == tabuleiro["0"]["2"]:
      return 0
    else:
      for y in range(3):
        if tabuleiro[0][str(y)] == "0" or tabuleiro[1][str(y)] == "0" or tabuleiro[2][str(y)] == "0":
          return 1
      return 2

@app.route('/game')
def criaJogo():
    cod = ''.join(random.choice( string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(8))
    jogador = ["X","O"]
    primeiro = jogador[random.randint(0, 1)]
    jogo = {"id" : cod, "proximoPlayer" : primeiro, "tabuleiro" : {"0":{"0":"0","1":"0","2":"0"},"1":{"0":"0","1":"0","2":"0"},"2":{"0":"0","1":"0","2":"0"}}}
    jogos.append(jogo)

    jogo = {"id" : cod, "firstPlayer" : primeiro}
    return jogo

@app.route('/game/<string:idJogada>/<string:gameJson>')
def movimenta(idJogada,gameJson):
  jogada = json.loads(gameJson)
  jogador = jogada["jogador"]
  x = jogada["x"]
  y = jogada["y"]

  for jogo in jogos:
    if idJogada == jogo["id"]:
      if jogador.upper() == jogo["proximoPlayer"]:
        if jogo["tabuleiro"][x][y] == "0":
          jogo["tabuleiro"][x][y] = jogador
          if jogador.upper() == "X":
            jogo["proximoPlayer"] = "O"
          else:
            jogo["proximoPlayer"] = "X"

          if checaVitoria(jogo["tabuleiro"]) == 0:
            return json.loads('{"msg":"Partida finalizada","winner":"'+jogador.upper()+'"}')
          elif checaVitoria(jogo["tabuleiro"]) == 1:
            return "200"
          elif checaVitoria(jogo["tabuleiro"]) == 2:
            return json.loads('{"msg":"Partida finalizada","winner":"draw"}')
        else:
          return json.loads('{"msg" : "Casa ocupada"}')
      else:
        return json.loads('{"msg" : "Não é o turno do jogador"}')
  
  return json.loads('{"msg" : "Partida não encontrada"}')
  
if __name__ == '__main__':
    app.run(debug=True)

