#Bibliotecas usadas
import time
import random

#Estética
print('{:=^40}'.format('Desafio 37'))
print('{:80}'.format(40 * '='))
#Interação
apr = input('')
nome = input('Olaaaa!!!!! Eu me camo ASCE, como é seu nome ?  ').strip().upper()
if nome == 'LUIS' or 'LUÍS':
    print('Iaew cara, suavidade ?')
elif nome == 'Karol':
    print('Fala guria')
else:
    print('É um prazer em te conhecer!!!!')
#Lista de fases
estoubem = [ #Frases felizes
'Se você está bem, eu estou bem!',
'Que sua felicidade contagie a todos como me contageou ;D',
'Eu estou feliz por você está feliz.',
'Que bom que você esta bem!'
]

estoumal = [ #Frases de encorajamento
"Não desista, você é capaz de tudo!",
"Cada desafio é uma oportunidade para crescer.",
 "Acredite em você, pois você tem muito potencial!",
 "Continue lutando, o sucesso está perto!"
]
emoção = input('Você está bem? ').strip().upper()

# Enquanto a entrada não for 'SIM' ou 'NÃO', pede novamente
while emoção not in ['SIM', 'NÃO']:
    emoção = input('Eu sou meio binário, vai ter que escolher entre SIM e NÃO :D : ').strip().upper()
if emoção == 'SIM':
 frase =print(random.choice(estoubem))
else:
    frase = print(random.choice(estoumal))
time.sleep(3)
pergunta = input('Aprendi uma nova utilidade, agora eu consigo te ajudar a converter\na base numérica dos números. Quer ver ?: ').strip().upper()

# Enquanto a entrada não for 'SIM' ou 'NÃO', pede novamente
while pergunta not in ['SIM', 'NÃO', 'QUERO']:
    pergunta = input('Eu sou meio binário, vai ter que escolher entre SIM e NÃO :D : ').strip().upper()
time.sleep(2)
if pergunta == 'SIM':
    print('Vamos nessa!!!!')
elif pergunta == 'QUERO':
     print('Vamos nessa!!!!!')
else:
    print('Ok, outro dia então...')
    exit()  

time.sleep(2)
#Entrada e processamento de dados
es = input('[1] Converter para BINÁRIO\n[2] Converter para OCTAL\n[3] Converter para HEXADECIMAL\n\n')
time.sleep(2)
while True:
    try:
        nu = int(input('Digite um número inteiro : '))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print('Isso não parece uma opção válida, tente novamente!')
if '1':
    print('O numéro {} convertido para binário é {}'.format(nu,bin(nu).lstrip('0ob')))
elif '2':
    print('O número {} convertido para octal é {}'.format(nu,oct(nu).lstrip('0ob')))

else:
    print('O número {} convertido para hexadecimal é {}'.format(nu,hex(nu).lstrip('0ob')))
time.sleep(2)
#Despedida
print('Espero ter sido util a você {}, até a próxima :D'.format(nome))
print('{:80}'.format(40 * '='))
print('{:80}'.format(40 * '='))
