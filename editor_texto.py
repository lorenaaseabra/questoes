lista_text = []
texto = input('Digite um texto: ')
lista_text.append(texto)

while(True):
        answer = input('qual seu próximo passo?\n (c - escrever;\n r - ler;\n u - modificar;\n d - deletar;\n S - SALVAR;\n O - ABRIR;\n E - SAIR)\n ')
        if (answer == 'c'): 
                #add frase
                frase = input('digite a frase:')
                lista_text.append(frase)

        elif(answer == 'r'):
                #ler frase
                textoRepl = ''
                for i in lista_text:
                        textoRepl += " "+i
                print(textoRepl)

        elif(answer == 'u'):
                #substitui uma string em uma determinada frase por outra
                #deve pedir ao usuario o index da frase e duas palavras, a que será buscada e a que irá substitu-lá
                index = int(input("Digite o index: "))
                word1 = input("Digite a palavra antiga: ")
                word2 = input("Digite a nova palavra: ")
                lista_text[index] = lista_text[index].replace(word1,word2)

        elif(answer == 'd'):
                #del frase que o usuario deve informar o index 
                index = int(input("Digite o index: "))
                del lista_text[index]

        elif(answer == 'S'):
                #SALVAR, pede ao usuário no nome do arquivo e salvar o arquivo no formato txt
                path = input('Digite o nome do arquivo que deseja criar:')
                file = open(path, 'w')
                file.write(lista_text)
                file.close()

        elif(answer =='O'):
                #ABRIR, abre um arquivo txt informado pelo usuário (sem apagar o seu conteúdo), nesse caso deve-se pedir o nome do arquivo a ser aberto;
                arq = input('Digite o nome do arquivo que deseja abrir')
                file = open(arq, 'r')
                file.close()

        elif(answer == 'E'):
                # SAIR, permite ao usuário finalizar a aplicação, caso o usuário não tenha salvo a aplicação 
                # deve perguntar se ele quer salvar o arquivo antes de sair, 
                # caso o usuário já tenha salvo a última alteração feita, a aplicação deve apenas sair.
        
        else:
                print('digite uma das opções válidas')

