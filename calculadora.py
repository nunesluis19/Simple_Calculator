print("-------------------------")
print("   CALCULADORA SIMPLES       ")
print("-------------------------\n")

print("-------------------------")
print(" Lista de operadores")
print("+ = Adição")
print("- = Subtração")
print("* = Multiplicação")
print("/ = Divisão")
print("-------------------------")

operadores_validos = ["+", "-", "*", "/"] #Lista de operadores validos da calculadora

#Loop para garantir que o usuario insira um operador
while True:
    operador = input("Digite o operador desejado: ")
    if operador in operadores_validos:
        break  #Encerra caso o operador seja valido
    print("Digite um operador que esteja na lista de operadores")

numero1 = float(input("Digite o primeiro numero: ") or 0)   #Caso usuario não digite nenhum valor, o numero será 0

numero2 = float(input("Digite o segundo numero: ") or 0 )   #Caso usuario não digite nenhum valor, o numero será 0

# Condicional para cada operador
if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    resultado = numero1 / numero2 if numero2 != 0 else "Erro: divisão por zero!"  
   

print(f"o resultado da sua conta foi {resultado}")