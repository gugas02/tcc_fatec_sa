# Variavel_OBD

import time
import serial
import decodifica_pid


class Obd(object):

    def __init__(self, porta, baudrate):
        self.porta = porta
        self.baud = baudrate
        self.resposta = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.ser = serial.Serial(self.porta, self.baud, timeout=1)

    def configura_comm(self):
        if self.ser.isOpen():
            self.ser.close()
        self.ser.open()
        if self.ser.isOpen():
            print("Porta Serial Aberta!")
        else:
            print("Falha ao abrir a porta!")
            exit()
        print("Enviando comandos:")
        self.ser.write(b'ATZ\r')
        time.sleep(0.2)
        self.ser.flush()
        self.ser.write(b'ATH0\r')
        time.sleep(0.2)
        read = self.ser.read(1024)
        self.ser.flush()
        self.ser.write(b'ATSP0\r')
        time.sleep(0.2)
        read1 = self.ser.read(1024)
        return [read, read1]

    def ect(self):
        aux = []
        result = 0
        value = []
        for i in range(10):
            for j in range(10):
                self.ser.flush()
                self.ser.write(b'0105\r')
                time.sleep(3)
                value_read = str(self.ser.read(1024))
                if value_read != 'NO DATA':
                    value_read = value_read.replace(" ", "")
                    b = value_read.find("\\r\\r")
                    a = (value_read.find('41')) + 4
                    value.append(value_read[a:b])
                    break
            if value[i] != 'ODATA' or 'EARCHING...\\rUNABLETOCONNECT' :
                value[i] = int(value[i],16)
                value[i] = value[i] - 40
                aux.append(value[i])
        if len(value) != 0:
            for i in range(len(value)):
                result += value[i]
            result = result/len(value)
            self.resposta[1] = 1
            print('Temperatura do Fluido de Arrefecimento: %f °C', result)
            return result
        else:
            self.resposta[1] = 0

    def turbo(self):
        aux = []
        result = 0
        value= []
        for i in range(10):
            for j in range(10):
                self.ser.flush()
                self.ser.write(b'016F\r')
                time.sleep(0.2)
                value_read = str(self.ser.read(1024))
                if value_read != 'NO DATA':
                    value_read = value_read.replace(" ", "")
                    b = value_read.find("\\r\\r")
                    a = (value_read.find('41')) + 4
                    value.append(value_read[a:b])
                    break
            if value[i] != 'ODATA':
                value[i] = int(value[i],16)
                aux.append(value[i])
        if len(value) != 0:
            for i in range(len(value)):
                result += value[i]
            result = result/len(value)
            self.resposta[2] = 1
            print('Pressão do turbo: %d kPa', result)
            return result
        else:
            self.resposta[2] = 0

    def sensor_map(self):
        aux = []
        result = 0
        value=[]
        for i in range(10):
            for j in range(10):
                self.ser.flush()
                self.ser.write(b'010B\r')
                time.sleep(0.2)
                value_read = str(self.ser.read(1024))
                if value_read != 'NO DATA':
                    value_read = value_read.replace(" ", "")
                    b = value_read.find("\\r\\r")
                    a = (value_read.find('41')) + 4
                    value.append(value_read[a:b])
                    break
            if value[i] != 'ODATA':
                value[i] = int(value[i],16)
                aux.append(value[i])
        if len(value) != 0:
            for i in range(len(value)):
                result += value[i]
            result = result/len(value)
            self.resposta[3] = 1
            print('Pressão no coletor de admissão: %d kPa', result)
            return result
        else:
            self.resposta[3] = 0

    def eat(self):
        aux = []
        result = 0
        value=[]
        for i in range(10):
            for j in range(10):
                self.ser.flush()
                self.ser.write(b'010F\r')
                time.sleep(0.2)
                value_read = str(self.ser.read(1024))
                if value_read != 'NO DATA':
                    value_read = value_read.replace(" ", "")
                    b = value_read.find("\\r\\r")
                    a = (value_read.find('41')) + 4
                    value.append(value_read[a:b])
                    break
            if value[i] != 'ODATA':
                value[i] = int(value[i],16)
                value[i] = value[i] - 40
                aux.append(value[i])
        if len(value) != 0:
            for i in range(len(value)):
                result += value[i]
            result = result/len(value)
            self.resposta[4] = 1
            print('Temperatura do ar na admissão: %d °C', result)
            return result
        else:
            self.resposta[4] = 0

    def ip(self):
        aux = []
        result = 0
        value=[]
        for i in range(10):
            for j in range(10):
                self.ser.flush()
                self.ser.write(b'010E\r')
                time.sleep(0.2)
                value_read = str(self.ser.read(1024))
                if value_read != 'NO DATA':
                    value_read = value_read.replace(" ", "")
                    b = value_read.find("\\r\\r")
                    a = (value_read.find('41')) + 4
                    value.append(value_read[a:b])
                    break
            if value[i] != 'ODATA':
                value[i] = int(value[i],16)
                value[i] = (value[i]/2) - 64
                aux.append(value[i])
        if len(value) != 0:
            for i in range(len(value)):
                result += value[i]
            result = result/len(value)
            self.resposta[5] = 1
            print('Ponto de ignição: %d °APMS', result)
            return result
        else:
            self.resposta[5] = 0

    def maf(self):
        aux = []
        result = 0
        value=[]
        for i in range(10):
            for j in range(10):
                self.ser.flush()
                self.ser.write(b'0110\r')
                time.sleep(0.2)
                value_read = str(self.ser.read(1024))
                if value_read != 'NO DATA':
                    value_read = value_read.replace(" ", "")
                    b = value_read.find("\\r\\r")
                    a = (value_read.find('41')) + 4
                    value.append(value_read[a:b])
                    break
            if value[i] != 'ODATA':
                value[i] = int(value[i],16)
                value[i] = value[i] / 100
                aux.append(value[i])
        if len(value) != 0:
            for i in range(len(value)):
                result += value[i]
            result = result/len(value)
            self.resposta[6] = 1
            print('O fluxo de ar no coletor de admissão é de: %d g/s', result)
            return result
        else:
            self.resposta[6] = 0

    def nvl_comb(self):
        aux = []
        result = 0
        value=[]
        for i in range(10):
            for j in range(10):
                self.ser.flush()
                self.ser.write(b'012F\r')
                time.sleep(0.2)
                value_read = str(self.ser.read(1024))
                if value_read != 'NO DATA':
                    value_read = value_read.replace(" ", "")
                    b = value_read.find("\\r\\r")
                    a = (value_read.find('41')) + 4
                    value.append(value_read[a:b])
                    break
            if value[i] != 'ODATA':
                value[i] = int(value[i],16)
                value[i] = 0.3921 * value[i]
                aux.append(value[i])
        if len(value) != 0:
            for i in range(len(value)):
                result += value[i]
            result = result/len(value)
            self.resposta[7] = 1
            print('nivel de combustivel: %d %', result)
            return result
        else:
            self.resposta[7] = 0

    def eot(self):
        aux = []
        result = 0
        value =[]
        for i in range(10):
            for j in range(10):
                self.ser.flush()
                self.ser.write(b'015C\r')
                time.sleep(0.2)
                value_read = str(self.ser.read(1024))
                if value_read != 'ODATA':
                    value_read = value_read.replace(" ", "")
                    b = value_read.find("\\r\\r")
                    a = (value_read.find('41')) + 4
                    value.append(value_read[a:b])
                    break
            if value[i] != 'NO DATA':
                value[i] = int(value[i],16)
                value[i] = value[i] - 40
                aux.append(value[i])
        if len(value) != 0:
            for i in range(len(value)):
                result += value[i]
            result = result/len(value)
            self.resposta[8] = 1
            print('Temperatura do óleo do motor: %d °C', result)
            return result
        else:
            self.resposta[8] = 0

    def re(self):
        aux = []
        result = 0
        value =[]
        for i in range(10):
            for j in range(10):
                self.ser.flush()
                self.ser.write(b'0106\r')
                time.sleep(0.2)
                value_read = str(self.ser.read(1024))
                if value_read != 'NO DATA':
                    value_read = value_read.replace(" ", "")
                    b = value_read.find("\\r\\r")
                    a = (value_read.find('41')) + 4
                    value.append(value_read[a:b])
                    break
            if value[i] != 'ODATA':
                value[i] = int(value[i],16)
                value[i] = (0.78125 * value[i]) - 100
                aux.append(value[i])
        if len(value) != 0:
            for i in range(len(value)):
                result += int(value[i])
            result = result/len(value)
            self.resposta[9] = 1
            print('Relação estequiométrica: %d °C', result)
            return result
        else:
            self.resposta[9] = 0

    def cr(self):
        aux = []
        aux1 = []
        result = 0
        result1 = 0
        value = []
        value1 = []
        for i in range(10):
            for j in range(10):
                self.ser.flush()
                self.ser.write(b'015E\r')
                time.sleep(0.2)
                value_read = str(self.ser.read(1024))
                self.ser.flush()
                self.ser.write(b'010D\r')
                time.sleep(0.2)
                value_read1 = str(self.ser.read(1024))
                if value_read != 'NO DATA' and value_read1 != 'NO DATA':
                    value_read = value_read.replace(" ", "")
                    b = value_read.find("\\r\\r")
                    a = (value_read.find('41')) + 4
                    value.append(value_read[a:b])
                    value_read1 = value_read1.replace(" ", "")
                    b = value_read1.find("\\r\\r")
                    a = (value_read1.find('41')) + 4
                    value1.append(value_read[a:b])
                    break
            if value[i] != 'ODATA' and value1[i] != 'NO DATA':
                value[i] = int(value[i],16)
                value1[i] = int(value1[i],16)
                value[i] = (value[i]/128) - 210
                aux.append(value[i])
                aux1.append(value1[i])
        if len(value) != 0 and len(value1) != 0:
            for i in range(len(value)):
                result += value[i]
            result = result/len(value)
            print('Taxa de combustivel gasto: %d L/h', result)
            for i in range(len(value1)):
                result1 += value1[i]
            result1 = result1 / len(value1)
            self.resposta[10] = 1
            print('Veleocidade instantânea: %d Km/h', result1)
            result2 = result/result1
            return result2
        else:
            self.resposta[10] = 0

    def dtc(self):
        result = 0
        self.ser.flush()
        self.ser.write(b'03\r')
        time.sleep(0.2)
        value_read = str(self.ser.read(1024))
        if value_read != 'NO DATA':
            value_read = value_read.replace(" ", "")
            b = value_read.find("\\r\\r")
            a = (value_read.find('43')) + 2
            value = value_read[a:b]
            aux = len(value)
            if value == "00":
                self.resposta[11] = 0
                print('Sem dtc')
                return
            value = str(bin(int(value,16)))[2:]
            if aux == int(len(value)/4):
                value = decodifica_pid.Decodifica(value)
                self.resposta[11] = 1
                return value
            else:
                aux = aux - (len(value) / 4)
                if aux == 1:
                    aux = len(value) % 4
                    if aux == 3:
                        value = "0"+ value
                    elif aux == 2:
                        value = "00" + value
                    elif aux == 1:
                        value = "000" + value
                    else:
                        value = "0000" + value
                if aux == 2:
                    aux = len(value) % 4
                    if aux == 3:
                        value = "00000" + value
                    elif aux == 2:
                        value = "000000" + value
                    elif aux == 1:
                        value = "0000000" + value
                    else:
                        value = "00000000" + value
                value = decodifica_pid.Decodifica(value)
                self.resposta[11] = 1
                print('DTC: %d °C', value)
            return value



    def getvalue(self):
        sensors = [
            str(self.ect()),
            #str(self.turbo()),
            str(self.sensor_map()),
            str(self.eat()),
            str(self.ip()),
            #str(self.maf()),
            #str(self.nvl_comb()),
            #str(self.eot()),
            #str(self.re()),
            #str(self.cr()),
            str(self.dtc())
        ]
        for i in range(len(sensors)):
            if sensors[i] is None:
                sensors.pop(i)

        return [sensors, self.resposta]












