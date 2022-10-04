def validar_arquivo(nome):  
    try:
        a = open(nome, "r")
        a.close()
        return True
    except Exception as error:  
        print("arquivo nao encontrado!", error._class_)
        return False


def organizar_pesos(nome):  
    global lista_boas
    lista_boas = []
    global lista_neutras
    lista_neutras = []
    global lista_ruins
    lista_ruins = []
    file = open(nome, "r")
    for line in file.readlines():
        espaco = line.index(" ")
        if line[:espaco] == "Good":
            lista_boas = line[espaco:].split()
        if line[:espaco] == "Neutral":
            lista_neutras = line[espaco:].split()
        if line[:espaco] == "Bad":
            lista_ruins = line[espaco:].split()
    file.close()


index = 0
while True:
    nomespesos = input(
        "digite o nome do arquivo dos nomes e pesos: ")  
    resp = validar_arquivo(nomespesos)
    if resp:
        break

organizar_pesos(nomespesos)
while True:
    frase = input(
        "digite o nome do arquivo com as frases a serem analizadas: ")  
    resp = validar_arquivo(frase)
    if resp:
        break

file = open(frase, "r")
frases = []
texto = file.read().title()
textos = texto.split("\n")
for i in textos:
    c = i.replace(",", " ").replace(".", " ").split()
    frases.append(c)
file.close()
reconhecidas = []  
aprendidas = []  
arquivo = open(frase, "r")
arq = arquivo.read().title()
boa = neutra = ruim = 0
boas = []
neutras = []
ruins = []
reconhecidas_frase = []
for i in frases:
    for palavra in lista_boas:  
        if palavra in i:
            boa += i.count(palavra)
            if palavra.title() not in reconhecidas:
                reconhecidas.append(palavra)
    for palavra in lista_neutras:  
        if palavra.title() in i:
            neutra += i.count(palavra)
            if palavra.title() not in reconhecidas:
                reconhecidas.append(palavra)

    for palavra in lista_ruins:  
        if palavra.title() in i:
            ruim += arq.count(palavra)
            if palavra.title() not in reconhecidas:
                reconhecidas.append(palavra)
    reconhecidas_frase.append(reconhecidas)
    reconhecidas = []
    boas.append(boa)
    boa = 0
    neutras.append(neutra)
    neutra = 0
    ruins.append(ruim)
    ruim = 0
medias = []

aprendidas_frase = []
for i in frases:
    for palavra in i: 
        if palavra not in reconhecidas_frase[index]:
            if palavra not in aprendidas:
                aprendidas.append(palavra)
        try:
            numerador_texto = (boas[index] * 5) + (neutras[index] * 0) + (ruins[index] * -5)
            denominador_texto = (boas[index] + neutras[index] + ruins[index])
            media_texto = float(numerador_texto / denominador_texto)
        except ZeroDivisionError:
            media_texto = 0
    media_texto = f"{media_texto:.2f}"
    media_texto = float(media_texto)
    medias.append(media_texto)
    aprendidas_frase.append(aprendidas)
    aprendidas = []
    index += 1

index = 0

for i in range(len(frases)):
    if medias[i] > 0:  
        for palavra in aprendidas_frase[i]:
            if palavra not in lista_boas:
                lista_boas.append(palavra)
        joinboas = " ".join(lista_boas).replace(",", " ")
        joinneutras = " ".join(lista_neutras)
        joinruins = " ".join(lista_ruins)
        file = open(nomespesos, "w")
        file.write(f"Good {joinboas}\n")
        file.write(f"Neutral {joinneutras}\n")
        file.write(f"Bad {joinruins}")
        file.close()
    elif medias[i] == 0:
        for palavra in aprendidas_frase[i]:
            if palavra not in lista_neutras:
                lista_neutras.append(palavra)
        joinboas = " ".join(lista_boas)
        joinneutras = " ".join(lista_neutras).replace(",", " ")
        joinruins = " ".join(lista_ruins)
        file = open(nomespesos, "w")
        file.write(f"Good {joinboas}\n")
        file.write(f"Neutral {joinneutras}\n")
        file.write(f"Bad {joinruins}")
        file.close()
    elif medias[i] < 0:
        for palavra in aprendidas_frase[i]:
            if palavra not in lista_ruins:
                lista_ruins.append(palavra)
        joinboas = " ".join(lista_boas)
        joinneutras = " ".join(lista_neutras)
        joinruins = " ".join(lista_ruins).replace(",", " ")
        file = open(nomespesos, "w")
        file.write(f"Good {joinboas}\n")
        file.write(f"Neutral {joinneutras}\n")
        file.write(f"Bad {joinruins}")
        file.close()
junto_frase = []
junto_aprendidas = []
junto_reconhecidas = []
for i in frases:
    r = ";".join(i)
    junto_frase.append(r)

for i in aprendidas_frase:
    r = ";".join(i)
    junto_aprendidas.append(r)

for i in reconhecidas_frase:
    r = ';'.join(i)
    junto_reconhecidas.append(r)
a = open("resultado.csv", "w")
a.write("Frase lida, Palavras Reconhecidas, Peso da Frase, Palavras Aprendidas\n")
for i in range(len(frases)):
    a.write(f"{junto_frase[i]}, {junto_reconhecidas[i]}, {medias[i]}, {junto_aprendidas[i]}\n")
a.close()