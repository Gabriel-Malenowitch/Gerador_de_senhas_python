from random import randint, sample

def gerar_senha(senha):
  def lafor(n, vap):
    global senha
    for i in range(vap):
      senha += n[randint(0, len(n)-1)] 

  lafor(alfabeto, numero_de_letras)
  lafor(numeros, numero_de_numeros)
  lafor(sinais, numero_de_simbolos)

senha    = ""; senha_final = ""
alfabeto = "abcdefghijklmnopqrstuvwxyz"
numeros  = "123456789"
sinais   = "+=_-!@#$%¨&*()~^´`/"

numero_de_simbolos = int(input("Digite o número de simbolos que deseja: "))
numero_de_letras   = int(input("Digite o número de letras que deseja: "))
numero_de_numeros  = int(input("Digite o número de números que deseja: "))

while len(senha) < (numero_de_letras + numero_de_numeros + numero_de_simbolos):
  gerar_senha(senha)

print("".join(sample(senha, len(senha))))
