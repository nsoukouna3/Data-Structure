def finding_duplicate_string(string):
    new_dict={}
    List=[]
    for char in string:
        if char not in new_dict:
            new_dict[char]=1
        else:
            new_dict[char]+=1
    
    for letter in new_dict:
        if new_dict[letter]>1:
            List.append(letter)
    return List




string="finding lillipop"

print(finding_duplicate_string(string))
