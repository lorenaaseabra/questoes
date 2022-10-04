# Faça uma aplicação que cadastre o nome primeiro do aluno e sua matricula, 
# em seguida peça as matérias que o aluno cursou e suas respectivas notas finais.
# APÓS O CADASTRO, sua aplicação deve permitir buscar um aluno pelo seu nome ou pela sua matrícula, 
# mostrando todos os seus dados cadastrados. (Lembre-se, um aluno pode ter o primeiro nome igual a de outro,
# neste caso TODOS os alunos com aquele nome devem ser apresentados.)

list_dict = []
while(True):
        alunos = {}
        nome = input('Digite o Nome (digite fim para encerrar): ')
        if nome != 'fim':
                matricula = input('Digite a matricula: ')
                materias = input('Digite as materias cursadas: ')
                notas = input('Digite as notas finais: ')
                alunos['nome'] = nome
                alunos['matricula'] = matricula
                alunos['materias'] = materias
                alunos['notas'] = notas
                list_dict.append(alunos)
        else:
                break

while(True):
        nome_Buscado = input('Digite o nome ou a matrícula que deseja buscar (digite fim para encerrar): ')
        for dicto in list_dict:
                if nome_Buscado == dicto['nome'] or nome_Buscado == dicto['matricula']:
                        print('-------------------------------------------')
                        print('Nome: '+dicto['nome'])
                        print('Matricula: '+dicto['matricula'])
                        print('Materias: '+dicto['materias'])
                        print('Notas: '+dicto['notas'])
                        print('-------------------------------------------')
        if nome_Buscado == 'fim':
                break