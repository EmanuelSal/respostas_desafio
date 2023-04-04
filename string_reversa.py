# STRING DE EXEMPLO
string = "target sistemas"

# PASSANDO PELA STRING DE TRÁS PARA FRENTE E CONCATENANDO, FORMANDO A STRING INVERTIDA AO FINAL DO LOOP

string_invertida = ""
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# SAIDA FINAL | IMPRESSAO
print(string_invertida)
