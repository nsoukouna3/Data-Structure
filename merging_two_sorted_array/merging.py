def merging_two_array(array1,array2):
    i=0
    j=0
    k=0
    result= [0 for _ in range(len(array1)+ len(array2))]
    while i< len(array1) and j<len(array2):
        if array1[i]<array2[j]:
            result[k]=array1[i]
            i+=1
            k+=1
        elif array1[i]>array2[j]:
            result[k]= array2[j]
            j+=1
            k+=1
        else:
            result[k]= array1[i]
            i+=1
            k+=1
    while i <len(array1):
        result[k]= array1[i]
        i+=1
        k+=1
    while j<len(array2):
        result[k]= array2[j]
        j+=1
        k+=1
    return result

array1=[2,4,6,7,9]
array2=[1,3,4,4,5,8,10,12]


print(merging_two_array(array1, array2))
    