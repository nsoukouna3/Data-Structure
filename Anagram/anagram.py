
def finding_anagram(name1, name2):
    left=dict()
    right=dict()
    if len(name1)!= len(name2):
        return False
    for char in name1:
        if char not in left:
            left[char]=1
        else:
            left[char]+=1
    
    for letter in name2:
        if letter not in right:
            right[letter]=1
        else:
            right[letter]+=1
    return left==  right
       

n1="decimal"
n2= "medical"

print(finding_anagram(n1,n2))