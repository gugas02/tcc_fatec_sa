class Decodifica(object):
    def __init__(self, cod):
        self.pid = ''
        self.tipo = ""
        self.tamanho = ""
        self.index = ""
        self.x = cod
        self.get_tipo(self.x[:4])
        self.get_tamanho(self.x)



# decodifica o pid e recebe apenas 8 bits correspondentes ao pid,
# ou seja, a mensagem deve ser cortada antes desse metodo ser utilizado
    def get_pid(self, a):
        b = a[:2]
        if b == "00":
            self.pid += 'P'
        elif b == "01":
            self.pid += 'C'
        elif b == "10":
            self.pid += 'B'
        elif b == "11":
            self.pid += 'U'
        # segundo caractere dtc
        pid = self.pid + str(int(a[2:4], 2))
        # terceiro caractere dtc
        b = hex(int(a[4:8], 2))
        b = b[2:]
        pid = pid + b
        # quarto caractere dtc
        b = hex(int(a[8:12], 2))
        b = b[2:]
        pid = pid + b
        # quinto caractere dtc
        b = hex(int(a[12:16], 2))
        b = b[2:]
        pid = pid + b
        return pid

# verifica o tipo da mensagem, apenas 4 bits correspondentes ao pid,
# ou seja, a mensagem deve ser cortada antes desse metodo ser chamado
    def get_tipo(self, bits):
        if bits == "0000":
            self.tipo = "single frame"

        elif bits == "0001":
            self.tipo = "first frame"

        elif bits == "0010":
            self.tipo = "consecutive frame"

        elif bits == "0011":
            self.tipo = "flow frame"

# verifica o tamanho da mensagem, recebe toda a mensagem
    def get_tamanho(self, bits):
        if self.tipo == "single frame":
            self.tamanho = str(int(bits[4:8], 2))
        if self.tipo == "first frame":
            self.tamanho = str(int(bits[4:16], 2))
