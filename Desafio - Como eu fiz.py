print('''Qual a primeira letra do alfabeto?
a - B
b-  D
c -  A
d - C
''')
resposta=input()
score=0
ponto= score + 1

if  resposta == "a" :
    print(f' Acertou! , Sua pontuação é: {ponto}')

else:
    print( f' Errou! tente novamnete, Sua pontuação é: {score}')
    