import random
comida = ['coxinha', 'queijo', 'frango', 'panqueca', 'açaí', 'arroz', 'feijão', 'cookie', 'sushi', 'bolo', 'cuscuz', 'empadão', 'farofa', 'risotto']
palavra = random.choice(comida)
tentativas = 10
largura = 60
enchemento = '━'
riscokkkk = ['_'] * len(palavra)

print(f' Olá, seja bem vindo ao jogo da forca  (￣▽￣)ノ  '.center(largura, enchemento))
print(f' Regras '.center(largura, enchemento))
print(f'O computador ira escolher uma palavra aliatoria sobre o tema, o qual é comida.'.center(largura))
print(f'O jogador devera tentar advinhar qual foi a "comida" escolhida.'.center(largura))
print(f'Voçe tem 10 tentativas para acertar, caso nao consiga voçe perde (︶︹︺).'.center(largura))
print(f' Boa sorte (＾_＾）'.center(largura, enchemento))

for tentativa in range(tentativas):

    letra = input(f" Digite uma letra: ")
    print(f" Tentativas: {tentativa + 1}")

    if letra in palavra:
        print(f'A letra que você colocou tem na palavra')
        for item in range(len(palavra)):
            if letra == palavra[item]:
                riscokkkk[item] = letra
    else:
        print(f" A letra que você colocou não tem na palavra")

    print(" ".join(riscokkkk))

    if '_' not in riscokkkk:
        break

if '_' in riscokkkk:
    print(" Voçe perdeu ;-; na proxima voçe consegue!")
else:
    print(" VOÇE ACERTOU ヽ(^。^)丿 PARABÉNSSS!!")

print(f"A palavra era {palavra}")
