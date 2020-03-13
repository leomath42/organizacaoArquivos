from struct import *
import random

with open("cep.dat", "r") as arq:
    total_bytes = arq.seek(0, 2)
    chunk = total_bytes // 20
    lines = chunk // 300
    total_lines = total_bytes / 300

print(total_bytes, chunk, total_lines, lines)
struct_line = Struct("72s72s72s72s2s8s2s")
struct_chunk = Struct("300s"*lines)


class Cep(object):
    def __init__(self, parse, line, order_by):
        self.row = parse.unpack(line)
        self.order_by = order_by

    def __gt__(self, cep):
        return self.row[self.order_by] > cep.row[self.order_by]

    def __lt__(self, cep):
        return self.row[self.order_by] < cep.row[self.order_by]

    def __eq__(self, cep):
        return self.row[self.order_by] == cep.row[self.order_by]

    def __str__(self):
        s = ''
        for i in self.row:
            s += i.decode(encoding='latin_1')
        return s


def parseCep(data, struct_chunk, struct_line):
    lista = []
    lines = struct_chunk.unpack(data)
    for line in lines:
        lista.append(Cep(struct_line, line, 5))  # "coluna 5 == cep"
    return lista

def readChunk(file_name, chunk, struct_chunk):
    with open(file_name, 'r') as arq:
        str = arq.read(struct_chunk.size)
        str = bytes(str, 'latin_1')
        return struct_chunk.unpack(str)


def merge(lista_left, lista_right):
    aux = []
    i = j = 0
    while i < len(lista_left) and j < len(lista_right):
        if lista_left[i] < lista_right[j]:
            aux.append(lista_left[i])
            i += 1
        else:
            aux.append(lista_right[j])
            j += 1

    while i < len(lista_left):
        aux.append(lista_left[i])
        i += 1
    while j < len(lista_right):
        aux.append(lista_right[j])
        j += 1
    #print(aux)
    return aux


def mergeSort(lista, left, right):
    mid = (left+right) // 2
    if len(lista) > 1:
        lista_left = lista[:mid]
        lista_right = lista[mid:]

        lista_left = mergeSort(lista_left, 0, len(lista_left))
        lista_right = mergeSort(lista_right, 0, len(lista_right))
        # print(chunk_lines)
        lista = merge(lista_left, lista_right)

    return lista


if __name__ == "__main__":
    teste = [3, 2, 7, 8, 9, 13, 1, 5, 4, 6]
    #print(struct_line.unpack(struct_chunk.unpack(chunk_lines)[0]))
    # lista = parseCep(chunk_lines)
    # for i in lista:
    #     print(i)
    # r = list(range(1, 10000000))
    # aux = []
    # for i in r:
    #     aux.append(random.choice(r))
    #
    # teste = aux
    # print(teste)
    # teste = mergeSort(teste, 0, 10)
    # print(teste)
    #mergedList = []
    # v = (struct_chunk.size//20)
    # struct_aux = Struct("300s"*v)
    # print(struct_chunk.size, struct_aux.size, v)
    sortedFiles = []
    with open("cep.dat", "r") as arq:
        for i in range(0, 20):
            if total_bytes > struct_chunk.size:
                chunk_lines = bytes(arq.read(struct_chunk.size), 'latin_1')  # struct_chunk.size
            else:
                chunk_lines = bytes(arq.read(total_bytes), 'latin_1')  # struct_chunk.size

            lista = parseCep(chunk_lines, struct_chunk, struct_line)

            lista = mergeSort(lista, 0, len(lista))
            #mergedList.append(lista)
            # print("-"*10+"\n")
            # for i in lista:
            #     print(i, sep=' ')
            arq_aux = open("cep.dat{}".format(i+1), "+w")
            sortedFiles.append(arq_aux)
            for i in lista:
                arq_aux.write(str(i))

            total_bytes -= struct_chunk.size

    # step to merged All sortedFiles in the output file:
    lines_aux = lines//10
    struct_aux = Struct("300s"*lines_aux)
    #print(struct_aux.size)
    toRead = struct_aux.size
    j = 0
    mergedFiles = []
    teste = open("teste.dat", "w")
    for arq in sortedFiles:
        arq.seek(0, 0)
        #print(len(bytes(arq.read(struct_aux.size), 'latin_1')))
        file = parseCep(bytes(arq.read(struct_aux.size), 'latin_1'), struct_aux, struct_line)
        mergedFiles = merge(mergedFiles, file)
        toRead -= struct_aux.size

    for i in mergedFiles:
        teste.write(str(i))
    #
    # teste.close()
        #if j == 2 : break
# print(struct_line.unpack(readChunk("cep.dat", chunk, struct_chunk)[34964]))
#
# chunk_lines = None
#
# if mid <= chunk/len(struct_line) < right - left:
#     chunk_lines = readChunk('cep.dat', chunk, struct_chunk)

#with open("cep.dat", "r") as arq:
    # arq.read(2)
    # lines = arq.seek(0, 2) #/  # bytes
    # print(lines/300)
    #str = bytes(arq.read(300*3496), 'latin_1')
    # print(str)
    # # str = arq.read(struc.size)
    # # str = arq.read(struc.size) #.encode()
    # # str = arq.read(struc.size).encode()
    # # print(len(bytes(str, 'latin_1')))
    # # print((bytes(str, 'latin_1')))
    # print(len(str))
    # print(str[0:300])
    # print(struc.unpack(str[2100:2400]))
    #mergeSort(arq, 0, total_bytes/300)  # 209792100
