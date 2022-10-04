ranking_name = []
ranking_media = []
name = ' '

while (name !='SAIR'):
        salto_2 = []
        media = 0.0
        name = (input('Digite o seu nome,caso queira encerrar, digite SAIR: '))
        if (name != 'SAIR'):
                for i in range(5):
                        salto = float(input('Digite o valor dos saltos: '))
                        salto_2.append(salto)
                if (salto_2 [0] < salto_2 [1] and salto_2 [0] < salto_2 [2] and salto_2 [0] < salto_2 [3] and salto_2 [0] < salto_2[4]):
                        del salto_2 [0]
                elif (salto_2 [1] < salto_2 [0] and salto_2 [1] < salto_2 [2] and salto_2 [1] < salto_2 [3] and salto_2 [1] < salto_2[4]):
                        del salto_2 [1]
                elif (salto_2 [2] < salto_2 [1] and salto_2 [2] < salto_2 [0] and salto_2 [2] < salto_2 [3] and salto_2 [2] < salto_2[4]):
                        del salto_2 [2]
                elif (salto_2 [3] < salto_2 [1] and salto_2 [3] < salto_2 [2] and salto_2 [3] < salto_2 [0] and salto_2 [3] < salto_2[4]):
                        del salto_2 [3]
                else: 
                        del salto_2 [4]
                
                media = (salto_2[0] + salto_2[1] + salto_2[2] + salto_2[3])/4

                if((len(ranking_media) == 0) and (len(ranking_name) == 0)):
                        ranking_name.append(name)
                        ranking_media.append(media)
                else:
                        for i in range(len(ranking_media)):
                                if (ranking_media[i] < media):
                                        ranking_media.insert(i,media)
                                        ranking_name.insert(i,name)  
                                                              
for i in range(len(ranking_name)):
        print(i+1,"º lugar - ",ranking_name[i])
