# Variavel_OBD

import time
import serial

resposta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ser = serial.Serial("COM4", 38400, timeout=1)

def configura_comm():
    if ser.isOpen():
        ser.close()
    ser.open()
    if ser.isOpen():
        print("Porta Serial Aberta!")
    else:
        print("Falha ao abrir a porta!")
    exit()
    print("Enviando comandos:")
    ser.write(b'ATZ\r')
    time.sleep(0.2)
    ser.flush()
    ser.write(b'ATH0\r')
    time.sleep(0.2)
    resposta = ser.read(1024)
    ser.flush()
    ser.write(b'ATSP0\r')
    time.sleep(0.2)
    resposta1 = ser.read(1024)
    return [resposta,resposta1]


def ect():
    aux = []
    result = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'0105\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            if value_read != 'NO DATA':
                value = [value_read[(len(value_read) - 2)::1]]
                break
        if value[i] != 'NO DATA':
            value[i] = int(value[i])
            value[i] = value[i] - 40
            aux.append(value[i])
    if len(value) != 0:
        for i in range(len(value)):
            result += value[i]
        result = result/len(value)
        resposta[0] = 1
        print('Temperatura do Fluido de Arrefecimento: %d °C', result)
        return result
    else:
        resposta[0] = 0


def turbo():
    aux = []
    result = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'016F\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            if value_read != 'NO DATA':
                value = [value_read[(len(value_read) - 6)::1]]
                break
        if value[i] != 'NO DATA':
            value[i] = int(value[i])
            aux.append(value[i])
    if len(value) != 0:
        for i in range(len(value)):
            result += value[i]
        result = result/len(value)
        resposta[1] = 1
        print('Pressão do turbo: %d kPa', result)
        return result
    else:
        resposta[1] = 0


def sensor_map():
    aux = []
    result = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'010B\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            if value_read != 'NO DATA':
                value = [value_read[(len(value_read) - 2)::1]]
                break
        if value[i] != 'NO DATA':
            value[i] = int(value[i])
            aux.append(value[i])
    if len(value) != 0:
        for i in range(len(value)):
            result += value[i]
        result = result/len(value)
        resposta[2] = 1
        print('Pressão no coletor de admissão: %d kPa', result)
        return result
    else:
        resposta[2] = 0


def eat():
    aux = []
    result = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'010F\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            if value_read != 'NO DATA':
                value = [value_read[(len(value_read) - 2)::1]]
                break
        if value[i] != 'NO DATA':
            value[i] = int(value[i])
            value[i] = value[i] - 40
            aux.append(value[i])
    if len(value) != 0:
        for i in range(len(value)):
            result += value[i]
        result = result/len(value)
        resposta[3] = 1
        print('Temperatura do ar na admissão: %d °C', result)
        return result
    else:
        resposta[3] = 0


def ip():
    aux = []
    result = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'010E\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            if value_read != 'NO DATA':
                value = [value_read[(len(value_read) - 2)::1]]
                break
        if value[i] != 'NO DATA':
            value[i] = int(value[i])
            value[i] = (value[i]/2) - 64
            aux.append(value[i])
    if len(value) != 0:
        for i in range(len(value)):
            result += value[i]
        result = result/len(value)
        resposta[4] = 1
        print('Ponto de ignição: %d °APMS', result)
        return result
    else:
        resposta[4] = 0


def maf():
    aux = []
    result = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'0110\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            if value_read != 'NO DATA':
                value = [value_read[(len(value_read) - 4)::1]]
                break
        if value[i] != 'NO DATA':
            value[i] = int(value[i])
            value[i] = value[i] / 100
            aux.append(value[i])
    if len(value) != 0:
        for i in range(len(value)):
            result += value[i]
        result = result/len(value)
        resposta[5] = 1
        print('O fluxo de ar no coletor de admissão é de: %d g/s', result)
        return result
    else:
        resposta[5] = 0


def nvl_comb():
    aux = []
    result = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'012F\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            if value_read != 'NO DATA':
                value = [value_read[(len(value_read) - 2)::1]]
                break
        if value[i] != 'NO DATA':
            value[i] = int(value[i])
            value[i] = 0.3921 * value[i]
            aux.append(value[i])
    if len(value) != 0:
        for i in range(len(value)):
            result += value[i]
        result = result/len(value)
        resposta[6] = 1
        print('nivel de combustivel: %d %', result)
        return result
    else:
        resposta[6] = 0


def eot():
    aux = []
    result = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'015C\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            if value_read != 'NO DATA':
                value = [value_read[(len(value_read) - 2)::1]]
                break
        if value[i] != 'NO DATA':
            value[i] = int(value[i])
            value[i] = value[i] - 40
            aux.append(value[i])
    if len(value) != 0:
        for i in range(len(value)):
            result += value[i]
        result = result/len(value)
        resposta[7] = 1
        print('Temperatura do óleo do motor: %d °C', result)
        return result
    else:
        resposta[7] = 0


def re():
    aux = []
    result = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'0106\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            if value_read != 'NO DATA':
                value = [value_read[(len(value_read) - 2)::1]]
                break
        if value[i] != 'NO DATA':
            value[i] = int(value[i])
            value[i] = (0.78125 * value[i]) - 100
            aux.append(value[i])
    if len(value) != 0:
        for i in range(len(value)):
            result += value[i]
        result = result/len(value)
        resposta[8] = 1
        print('Relação estequiométrica: %d °C', result)
        return result
    else:
        resposta[8] = 0


def cr():
    aux = []
    aux1 = []
    result = 0
    result1 = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'015D\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            ser.write(b'010D\r')
            time.sleep(0.2)
            value_read1 = ser.read(1024)
            if value_read != 'NO DATA' and value_read1 != 'NO DATA':
                value = [value_read[(len(value_read) - 4)::1]]
                value1 = [value_read1[(len(value_read1) - 2)::1]]
                break
        if value[i] != 'NO DATA' and value1[i] != 'NO DATA':
            value[i] = int(value[i])
            value1[i] = int(value1[i])
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
        resposta[9] = 1
        print('Veleocidade instantânea: %d Km/h', result1)
        result2 = result/result1
        return result2
    else:
        resposta[9] = 0


def re():
    aux = []
    result = 0
    for i in range(10):
        for j in range(10):
            ser.flush()
            ser.write(b'03\r')
            time.sleep(0.2)
            value_read = ser.read(1024)
            if value_read != 'NO DATA':
                value = [value_read[(len(value_read) - 12)::1]]
                break
        if value[i] != 'NO DATA':
            value[i] = bin(int(value[i]))
            value[i] = (0.78125 * value[i]) - 100
            aux.append(value[i])
    if len(value) != 0:
        for i in range(len(value)):
            result += value[i]
        result = result/len(value)
        resposta[8] = 1
        print('Relação estequiométrica: %d °C', result)
        return result
    else:
        resposta[8] = 0