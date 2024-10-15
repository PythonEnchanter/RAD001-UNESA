#O txt é salvo na mesma pasta em que está o arquivo .py

with open("crescente.txt", "w") as file:
    for i in range(100):
        file.write(f"{i+1}\n")

#X------------------- Exec 2 --------------------------X

#Adds new student to the file
def insereAluno(nome, email):
    try:
        arq = open("CadastroAlunos.txt", "a+")
    except:
        arq = open("CadastroAlunos.txt", "w+")
        arq.seek(0, 2)
    
    arq.write(f"{nome.upper()};{email.lower()}\n\n")
    print(f"Aluno {nome} cadastrado\n")

    arq.close()

#adds grades to students
def adicionarNota(nome):

    with open("CadastroAlunos.txt", "r+") as arq:
        lines = arq.readlines()
        student = False
        
        for i in range(len(lines)):
            if nome.lower() in lines[i].lower():
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
        
        # If the student is not found, print an error
        if student == False: print("ESTUDANTE NÃO CADASTRADO\n")

        arq.seek(0)
        arq.writelines(lines)
        arq.truncate()

def lerNotas(nome):
    arq = open("CadastroAlunos.txt", "r")
    student = False

    lines = arq.readlines()
    for i in range(len(lines)):
        #print(nome.lower() + " " + lines[i].split(";")[0].lower());
        
        if nome.lower() == lines[i].split(";")[0].lower():
            student = True

            if len(lines[i+1]) == 0:
                print("Sem notas registradas\n")
                break
            
            print(f"Notas: {lines[i+1]}");
            break
        
    if not student: print("Estudante não cadastrado")

    arq.close()

while True:
    functions = [1, 2, 3, 4]
    print("Comandos:\n1 - Cadastrar aluno\n2 - Adicionar notas\n3 - Conferir notas\n4 - Terminar")
    u_input = int(input("Digite um comando: "));

    match u_input:
        case 1:
            aluno = input("Insira nome e e-mail do aluno (separados por espaço): ").rsplit(maxsplit=1)
            insereAluno(aluno[0], aluno[1])
        case 2:
            aluno = input("Insira nome do aluno: ")
            adicionarNota(aluno)
        case 3:
            aluno = input("Insira nome do aluno: ")
            lerNotas(aluno)
        case 4:
            quit()
        case _:
            print("Comando inválido. Por favor, tente novamente.")
