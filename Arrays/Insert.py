def insert_element_array(array,index, value):
    if index<0 and index>len(array)-1:
        return False
    for idx in range(len(array)):
        if idx== index:
            array[index]= value
            return True
        
arr=[2,3,4]
insert_element_array(arr, 0, 5)
print(arr)