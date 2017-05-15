class Help:
    @staticmethod
    def list2str(lista, index):
        string = "".join(str(x) for x in lista[index])
        return string

    @staticmethod
    def str2list(string):
        lista = []
        for i in range(len(string)):
            lista.append(string[i])
        return lista
