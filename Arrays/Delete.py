def delete_element_at_index(array,index):
    array_length= len(array)-1
    if index<0 and index> array_length:
        return False
    
    for idx in range(index, array_length-1):
        array[idx]=array[idx+1]
    array_length=array_length - 1
    return array

arr=[1,2,3,4,5]

delete_element_at_index(arr, 0)
print(arr)