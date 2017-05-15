class Log(object):

    name = ""


    def __init__(self, nome_do_arqivo):
        self.name = nome_do_arqivo
        arquivo = open(self.name, 'a')
        arquivo.close()

    def escreve(self, data):
        arquivo = open(self.name, 'a')
        arquivo.writelines(Log.formata(data))
        arquivo.write("\n")
        arquivo.close()

    def escrevelinha(self, data):
        arquivo = open(self.name, 'a')
        arquivo.writelines(Log.formata(data))
        arquivo.close()

    @staticmethod
    def formata(dado):
        for i in range(len(dado)):
            dado[i] += ","
        return dado

    @staticmethod
    def arruma(dado):
        dado2 = []
        for i in range(len(dado)):
            dado2.append(dado[i].split(","))
        return dado2

    def ler(self):
        arquivo = open(self.name, 'r')
        leitura = arquivo.readlines()
        leitura = Log.arruma(leitura)
        arquivo.close()
        return leitura

    def len(self):
        arquivo = open(self.name, 'r')
        leitura = arquivo.readlines()
        return len(leitura)

    def limpa(self):
        arquivo = open(self.name, 'w')
        arquivo.close()