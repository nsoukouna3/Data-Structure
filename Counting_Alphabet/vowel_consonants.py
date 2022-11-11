def counting_vowels_consonants(string):
    vowels=['a','o','u','i','e']
    vowels_counts=0
    consonant_counts=0
    
    for char in string:
        if char in vowels:
            vowels_counts+=1
        elif (char >="A" and char<="Z") or (char>="a" and char<="z"):
            consonant_counts+=1
    return( f"vowels: {vowels_counts}, consonats :{consonant_counts}")


def word_count(string):
    string=string.strip(" ")
    if string=="":
        return None
    count=0
    for i in range(len(string)):
        if string[i] ==" " and string[i-1]!=" ":
            count+=1
    return count+1


string="Data structures are ways to store data"
name=" "
print(counting_vowels_consonants(string))
print(word_count(string))