import log
import tratamento_obd
import servidor
import sys
import getpass
import help

nome = "log.txt"
dado = log.Log(nome)
obd = tratamento_obd.Obd("COM4", 38400)
sever = servidor.Server()
helper = help.Help()

if len(sys.argv) < 2:
    print("nenhuma conta para login especificada")
    user = str(input("Insira seu login:"))
    senha = str(input('Password:'))
else:
    user = sys.argv[0]
    senha = sys.argv[1]
    print("tentando se conectar em %s", user)

user_id = sever.login(user, senha)
if not user_id:
    sys.exit("Falha ao tentar se conectar, verifique sua conexão com a internet")
elif user_id == True:
    sys.exit("Falha ao tentar se conectar, login ou senha invalida")

obd.configura_comm()

while 1:
    leitura = obd.getvalue()
    upload = sever.send(leitura[1], leitura[0])
    if not upload:
        leitura[0].append(helper.list2str(leitura, 1))
        dado.escreve(leitura[0])
    if upload:
        laitura = dado.ler()
        if laitura:
            if laitura[-1]:
                for i in range(len(laitura) - 1, 0, -1):
                    mask = helper.str2list(laitura[i][len(laitura) - 2])
                    laitura[i].pop(len(laitura) - 2)
                    upload = sever.send(mask, laitura[i])
                    if not upload:
                        break
                    else:
                        leitura[i].pop()
                if leitura[- 1]:
                    dado.limpa()
                else:
                    dado.limpa()
                    dado.escrevelinha(laitura)




