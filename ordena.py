def mergeSort(arq, left, right):
	mid = (left + right) // 2
	
	if mid > 0:
	    mergeSort(arq, left, mid)
	    mergeSort(arq, mid+1, right)
	
	print(mid)


with open("cep.dat", "r") as arq:
	#arq.read(2)
	lines = arq.seek(0, 2) / 2 # bytes	
	
	mergeSort(arq, 0, lines)
