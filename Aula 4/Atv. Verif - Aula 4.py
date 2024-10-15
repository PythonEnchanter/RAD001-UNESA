import re

#Adiciona alunos ao arquivo
def insereAluno(nome, email, curso):

    #w+ exclui os dados do arquivo caso ele já exista
    try:
        arq = open("CadastroAlunos.txt", "a+")
    except:
        arq = open("CadastroAlunos.txt", "w+")
        arq.seek(0, 2)
    
    arq.write(f"{nome.upper()};{email.lower()};{curso}\n\n")
    print(f"Aluno {nome} cadastrado\n")

    arq.close()

#Insere as notas dos alunos
def adicionarNota(nome):

    with open("CadastroAlunos.txt", "r+") as arq:
        lines = arq.readlines()
        student = False
        
        for i in range(len(lines)):

            '''procura o nome do aluno em cada linha do arquivo e
               compara com o primeiro elemento [repetir em cada
               função que use um aluno]'''
            if nome.lower() == lines[i].split(";")[0].lower():
                student = True

                grades = []
                while True:
                    u_input = input("Nota a ser inserida (pressione enter para terminar): ")
                    if u_input == '':
                        break
                    else:
                        grades.append(u_input)

                lines[i] += ";".join(map(str, grades)) + ";"
                print("Notas adicionadas\n")
                break
        
        if student == False: print("ESTUDANTE NÃO CADASTRADO\n")

        arq.seek(0)
        arq.writelines(lines)
        arq.truncate()

#Mostra as notas já inseridas
def lerNotas(nome):
    arq = open("CadastroAlunos.txt", "r")
    student = False

    lines = arq.readlines()
    for i in range(len(lines)):
        #print(nome.lower() + " " + lines[i].split(";")[0].lower()); debug

        if nome.lower() == lines[i].split(";")[0].lower():
            student = True

            if len(lines[i+1]) == 0:
                print("Sem notas registradas\n")
                break
            
            print(f"Notas: {lines[i+1]}");
            break
        
    if not student: print("ESTUDANTE NÃO CADASTRADO")

    arq.close()

#trata entradas com número
def remNumInput(**dados):
    info = []
    
    for key, value in dados.items():
        value = re.sub(r"\d", '', value)
        info.append(value)

    return str(info[0])

while True:
    functions = [1, 2, 3, 4]
    print("Comandos:\n1 - Cadastrar aluno\n2 - Adicionar notas\n3 - Conferir notas\n4 - Terminar")
    u_input = int(input("Digite um comando: "));

    match u_input:
        case 1:
            aluno = []
            cnt = 0
            
            print("Insira os dados do aluno [nome, e-mail, curso]: ")
            while True:
                u_input = input("Próxima info: ")
                if(cnt == 0 or cnt == 2): u_input = remNumInput(entrada=u_input)
                
                if u_input == '' and cnt == 3:
                    break
                else:
                    if u_input == '':
                        print("Entrada vazia\n");
                        continue
                    cnt += 1
                    aluno.append(u_input)

            insereAluno(aluno[0], aluno[1], aluno[2])
        case 2:
            aluno = input("Insira nome do aluno: ")
            aluno = remNumInput(entrada=aluno)
            
            if(len(aluno)==0):
                print("Entrada vazia\n");
                break
            adicionarNota(aluno)
        case 3:
            aluno = input("Insira nome do aluno: ")
            aluno = remNumInput(entrada=aluno)

            if(len(aluno)==0):
                print("Entrada vazia\n");
                break
            lerNotas(aluno)
        case 4:
            quit()
        case _:
            print("Comando inválido. Por favor, tente novamente.")
