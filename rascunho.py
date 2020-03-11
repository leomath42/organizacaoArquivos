from struct import *

with open("cep.dat", "r") as arq:
    total_bytes = arq.seek(0, 2)
    chunk = total_bytes // 20
    lines = chunk // 300
print(chunk)
struct_line = Struct("72s72s72s72s2s8s2s")
struct_chunk = Struct("300s"*lines)


def merge(list_1, list_2, left, right):
    #if left < right:
    aux = []
    print(list_1, list_2)
    if list_1 is not None and list_2 is not None:
        print(list_1, list_2)
        aux = list_1 + list_2
        return aux.sort()

    return aux
        # print(aux)
        # print(aux)
        # aux.sort()



def readChunk(file_name, chunk, struct_chunk):
    with open(file_name, 'r') as arq:
        str = arq.read(struct_chunk.size)
        str = bytes(str, 'latin_1')
        return struct_chunk.unpack(str)


def mergeSort(chunk_lines, left, right):
    mid = (left + right) // 2
    if left < right:
        list_1 = mergeSort(chunk_lines[left:mid], left, mid)
        list_2 = mergeSort(chunk_lines[mid+1:right], mid+1, right)
        return merge(list_1, list_2, left, right)
        #print(list_1, list_2)
        #chunk_lines = list_1.extend(list_2)
    #print(chunk_lines)

    return []

if __name__ == "__main__":
    teste = [3, 2, 7, 8, 9, 13, 1, 5, 4, 6]
    print(teste)
    teste = mergeSort(teste, 0, 10)
    print(teste)
    # with open("cep.dat", "r") as arq:
    #     for i in range(0, 1):
    #         chunk_lines = arq.read(struct_chunk.size)
    #         mergeSort(chunk_lines, 0, len(chunk_lines))
    #         with open("cep.dat{}".format(i+1), "w") as arq_aux:
    #             arq_aux.write(chunk_lines)

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
