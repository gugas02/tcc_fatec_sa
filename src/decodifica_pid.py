def decodifica_pid(str):
    pid = ''
    x = input('falha:')
    # verifica se o dtc possui o tamanho certo
    if len(x) == 16:
        # indica o 1 digito do dtc
        if x[0] == '0' and x[1] == '0':
            pid += 'P'
        elif x[0] == '0' and x[1] == '1':
            pid += 'C'
        elif x[0] == '1' and x[1] == '0':
            pid += 'B'
        else:
            pid += 'U'
        # indica o 2 digito do dtc
        if x[2] == '0' and x[3] == '0':
            pid += '0'
        elif x[2] == '0' and x[3] == '1':
            pid += '1'
        elif x[2] == '1' and x[3] == '0':
            pid += '2'
        elif x[2] == '1' and x[3] == '1':
            pid += '3'
# indica o 3 digito do dtc
        if x[4] == '0' and x[5] == '0' and x[6] == '0' and x[7] == '0':
            pid += '0'

        elif x[4] == '0' and x[5] == '0' and x[6] == '0' and x[7] == '1':
            pid += '1'

        elif x[4] == '0' and x[5] == '0' and x[6] == '1' and x[7] == '0':
            pid += '2'

        elif x[4] == '0' and x[5] == '0' and x[6] == '1' and x[7] == '1':
            pid += '3'

        elif x[4] == '0' and x[5] == '1' and x[6] == '0' and x[7] == '0':
            pid += '4'

        elif x[4] == '0' and x[5] == '1' and x[6] == '0' and x[7] == '1':
            pid += '5'

        elif x[4] == '0' and x[5] == '1' and x[6] == '1' and x[7] == '0':
            pid += '6'

        elif x[4] == '0' and x[5] == '1' and x[6] == '1' and x[7] == '1':
            pid += '7'

        elif x[4] == '1' and x[5] == '0' and x[6] == '0' and x[7] == '0':
            pid += '8'

        elif x[4] == '1' and x[5] == '0' and x[6] == '0' and x[7] == '1':
            pid += '9'

        elif x[4] == '1' and x[5] == '0' and x[6] == '1' and x[7] == '0':
            pid += 'A'

        elif x[4] == '1' and x[5] == '0' and x[6] == '1' and x[7] == '1':
            pid += 'B'

        elif x[4] == '1' and x[5] == '1' and x[6] == '0' and x[7] == '0':
            pid += 'C'

        elif x[4] == '1' and x[5] == '1' and x[6] == '0' and x[7] == '1':
            pid += 'D'

        elif x[4] == '1' and x[5] == '1' and x[6] == '1' and x[7] == '0':
            pid += 'E'

        elif x[4] == '1' and x[5] == '1' and x[6] == '1' and x[7] == '1':
            pid += 'F'

        # indica o 4 digito do dtc

        if x[8] == '0' and x[9] == '0' and x[10] == '0' and x[11] == '0':
            pid += '0'

        elif x[8] == '0' and x[9] == '0' and x[10] == '0' and x[11] == '1':
            pid += '1'

        elif x[8] == '0' and x[9] == '0' and x[10] == '1' and x[11] == '0':
            pid += '2'

        elif x[8] == '0' and x[9] == '0' and x[10] == '1' and x[11] == '1':
            pid += '3'

        elif x[8] == '0' and x[9] == '1' and x[10] == '0' and x[11] == '0':
            pid += '4'

        elif x[8] == '0' and x[9] == '1' and x[10] == '0' and x[11] == '1':
            pid += '5'

        elif x[8] == '0' and x[9] == '1' and x[10] == '1' and x[11] == '0':
            pid += '6'

        elif x[8] == '0' and x[9] == '1' and x[10] == '1' and x[11] == '1':
            pid += '7'

        elif x[8] == '1' and x[9] == '0' and x[10] == '0' and x[11] == '0':
            pid += '8'

        elif x[8] == '1' and x[9] == '0' and x[10] == '0' and x[11] == '1':
            pid += '9'

        elif x[8] == '1' and x[9] == '0' and x[10] == '1' and x[11] == '0':
            pid += 'A'

        elif x[8] == '1' and x[9] == '0' and x[10] == '1' and x[11] == '1':
            pid += 'B'

        elif x[8] == '1' and x[9] == '1' and x[10] == '0' and x[11] == '0':
            pid += 'C'

        elif x[8] == '1' and x[9] == '1' and x[10] == '0' and x[11] == '1':
            pid += 'D'

        elif x[8] == '1' and x[9] == '1' and x[10] == '1' and x[11] == '0':
            pid += 'E'

        elif x[8] == '1' and x[9] == '1' and x[10] == '1' and x[11] == '1':
            pid += 'F'

        # indica o 5 digito do dtc

        if x[12] == '0' and x[13] == '0' and x[14] == '0' and x[15] == '0':
            pid += '0'

        elif x[12] == '0' and x[13] == '0' and x[14] == '0' and x[15] == '1':
            pid += '1'

        elif x[12] == '0' and x[13] == '0' and x[14] == '1' and x[15] == '0':
            pid += '2'

        elif x[12] == '0' and x[13] == '0' and x[14] == '1' and x[15] == '1':
            pid += '3'

        elif x[12] == '0' and x[13] == '1' and x[14] == '0' and x[15] == '0':
            pid += '4'

        elif x[12] == '0' and x[13] == '1' and x[14] == '0' and x[15] == '1':
            pid += '5'

        elif x[12] == '0' and x[13] == '1' and x[14] == '1' and x[15] == '0':
            pid += '6'

        elif x[12] == '0' and x[13] == '1' and x[14] == '1' and x[15] == '1':
            pid += '7'

        elif x[12] == '1' and x[13] == '0' and x[14] == '0' and x[15] == '0':
            pid += '8'

        elif x[12] == '1' and x[13] == '0' and x[14] == '0' and x[15] == '1':
            pid += '9'

        elif x[12] == '1' and x[13] == '0' and x[14] == '1' and x[15] == '0':
            pid += 'A'

        elif x[12] == '1' and x[13] == '0' and x[14] == '1' and x[15] == '1':
            pid += 'B'

        elif x[12] == '1' and x[13] == '1' and x[14] == '0' and x[15] == '0':
            pid += 'C'

        elif x[12] == '1' and x[13] == '1' and x[14] == '0' and x[15] == '1':
            pid += 'D'

        elif x[12] == '1' and x[13] == '1' and x[14] == '1' and x[15] == '0':
            pid += 'E'

        elif x[12] == '1' and x[13] == '1' and x[14] == '1' and x[15] == '1':
            pid += 'F'

    return pid
