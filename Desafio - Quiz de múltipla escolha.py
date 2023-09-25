print('''Analise as sentenças a seguir sobre as funções da água.

I. Composição dos seres vivos
II. Irrigação de plantações
III. Regulação do clima
IV. Equilíbrio e conservação da biodiversidade

Estão corretas as afirmativas:

a) I e III
b) II e IV
c) I, II e III
d) Todas as alternativas''')
resposta = input().lower()

if resposta == "a":
    print('Resposta incorreta :(')
elif resposta == "b":
    print('Resposta incorreta :(')
elif resposta == "c":
    print('Resposta incorreta :(')
elif resposta =="d":
    print(''' Alternativa correta!
I. Composição dos seres vivos. CORRETA. A água é um recurso indispensável aos seres vivos.
II. Irrigação de plantações. CORRETA. O uso da água na agricultura pela irrigação pode ser feito de diversas formas.
III. Regulação do clima. CORRETA. O clima pode variar de acordo com os vapores de água presentes na atmosfera.
IV. Equilíbrio e conservação da biodiversidade. CORRETA. A água é fonte de vida para os seres vivos.')''')
else:
    print('Você digitou uma alternativa inválida, tente outra vez...')