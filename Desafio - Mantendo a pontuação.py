print('''Qual a primeira letra do alfabeto?
a - B
b-  D
c - A
d - C
''')
resposta=input()
score=0
ponto= score + 1

if  resposta == "a" :
    print(f' Parabéns, você acertou! Sua pontuação é: {ponto}')
    
elif resposta == "c":
    print(f' Resposta incorreta! Sua pontuação é: {score}')
else:
    print( f' Resposta incorreta! Sua pontuação é: {score}')