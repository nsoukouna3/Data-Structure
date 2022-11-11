def changing_uppercase_to_lowercase(string):
    new_string=""
    for i in range(len(string)):
        new_string+= chr(ord(string[i])+32)
    return new_string


def toggle_string(name):
    new_name=""
    for char in name:
        if ord(char)>= 65 and ord(char)<=90:
            new_name+= chr(ord(char)+32)
        elif char >='a' and char <='z':
            new_name+= chr(ord(char)-32)
    return new_name

last= "SOUKOUNA"
first="nAma"

print(changing_uppercase_to_lowercase(last))
print(toggle_string(first))