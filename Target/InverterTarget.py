string_invertida = ""

string = input("Digite uma string para inverter: ")

for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

print(f"String invertida: {string_invertida}")