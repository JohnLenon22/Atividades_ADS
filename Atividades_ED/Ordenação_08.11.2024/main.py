
def bubble_sort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                #ou
                # lista[j], lista[j+1] = lista[j+1] ,lista[j]
    
    print("Crescente-->",lista)

def bubble_sort_reverse(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] < lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                #ou
                # lista[j], lista[j+1] = lista[j+1] ,lista[j]

    print("Decrescente-->",lista)


def Selection_Sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        if lista[min_index]<lista[i]:
            aux=lista[i]
            lista[i]=lista[min_index]
            lista[min_index] = aux
    
    print(lista)

def Insertion_sort(lista):
    for i in range(len(lista)):
        item=lista[i]
        j-=1
        while j>=0 and item<lista[j]:
            lista[j+1]=lista[j]
            j-=1
        lista[j+1]=item
    print(lista)

def Merge_Sort(lista):
    size=len(lista)
    if size>1:
        meio=size//2
        esquerda=lista[:meio]
        direita=lista[meio:]
    
        Merge_Sort(esquerda)
        Merge_Sort(direita)

        i=j=k=0

        while i<len(esquerda) and j<len(direita):
            if esquerda[i] < direita[j]:
                lista[k]=esquerda[i]
                i+=1
            else:
                lista[k]=direita[j]
                j+=1
            k+=1
        while i<len(esquerda):
            lista[k]=esquerda[i]
            i+=1
            k+=1
        while j<len(direita):
            lista[k]=direita[j]
            j+=1
            k+=1
    print(lista)


lista=[9,7,5,2,10,4,1,6,3,0] 
Merge_Sort(lista) 





