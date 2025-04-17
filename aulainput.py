nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 6:
    print("Parabéns pela aprovação!")
elif 3 <= media <6:
    print("O aluno fará exame.") 
else:
    print("O aluno foi reprovado.")