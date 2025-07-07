print("ola mundo")

#ENTRADA DE DADOS 
nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))
nota3 = float(input("insira a terceira nota: "))
nota4 = float(input("insira a quarta nota: "))

#PROCESSAMENTO DOS DADOS 
notafinal = (nota1 + nota2 + nota3 + nota4) / 4

#SIADA
print("A nota final é: ", notafinal)

if notafinal < 60:
    print("O aluno esta reprovado! ")
elif(notafinal < 70):
    print("O resultado foi mediano!") 
elif(notafinal < 80):
    print("O resultado foi bom!") 
elif(notafinal < 90):
    print("O resultado exelente!")
else:
    print(" Você vai para havard! ")              