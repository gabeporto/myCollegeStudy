
usuarios = []


def moduloPrincipal():
    i = 0
    Opcao = 0
    while Opcao != 9:
        print("")
        print("BANCO DE DADOS DO INCLUSIONBANK")
        print("###############################")
        print("Opção 1 - Adicionar usuário")
        print("Opção 2 - Pesquisar usuário")
        print("Opção 3 - Listar todos os usuários")
        print("Opção 4 - Alterar dados de um usuário")
        print("Opção 5 - Listar idade média dos usuários")
        print("Opção 6 - Listar salário dos usuários")
        print("Opção 7 - Média do salário dos usuários")
        print("Opção 8 - Deletar usuário")
        print("Opção 9 - Sair do programa")
        print("")
        Opcao = int(input("Opção escolhida: "))
        if Opcao == 1:
            adicionarUsuario(usuarios)
        elif Opcao == 2:
            pesquisarUsuario(usuarios)
        elif Opcao == 3:
            listarUsuários(usuarios)
        elif Opcao == 4:
            alterarDadosUsuario(usuarios)
        elif Opcao == 5:
            idadeMediaUsuarios(usuarios)
        elif Opcao == 6:
            listarSalarioUsuarios(usuarios)
        elif Opcao == 7:
            mediaSalarioUsuarios(usuarios)
        elif Opcao == 8:
            deletarUsuario(usuarios)
        elif Opcao == 9:
            print("Finalizando aplicação...")



def adicionarUsuario(usuarios):
    i = len(usuarios)
    usuarios.append({"Nome": "", "CPF": "", "Idade": "", "Sexo": "", "Salario": ""})
    print("Opção 1 - Adicionar usuário")
    print("===========================")
    usuarios[i]["Nome"] = input("Nome: ")
    usuarios[i]["CPF"] = int(input("CPF: "))
    usuarios[i]["Idade"] = int(input("Idade: "))
    usuarios[i]["Sexo"] = input("Sexo: ")
    usuarios[i]["Salario"] = int(input("Salario: "))



def pesquisarUsuario(usuarios):
    i = 0
    Tam = len(usuarios)
    print("Opção 2 - Pesquisar usuário")
    print("============================")
    pesquisaUsuario = input("Nome do usuário: ")
    while i < Tam and pesquisaUsuario != usuarios[i]["Nome"]:
        i += 1
    print("Nome: ", usuarios[i]["Nome"])
    print("CPF: ", usuarios[i]["CPF"])
    print("Idade: ", usuarios[i]["Idade"])
    print("Sexo: ", usuarios[i]["Sexo"])
    print("Salário: ", usuarios[i]["Salario"])



def listarUsuários(usuarios):
    i = 0
    Tam = len(usuarios)
    print("Opção 3 - Listar todos os usuários")
    print("==================================")
    while i < Tam:
        print("Nome: ", usuarios[i]["Nome"])
        print("CPF: ", usuarios[i]["CPF"])
        print("Idade: ", usuarios[i]["Idade"])
        print("Sexo: ", usuarios[i]["Sexo"])
        print("Salário: ", usuarios[i]["Salario"])
        print("")
        i += 1



def alterarDadosUsuario(usuarios):
    i = 0
    Tam = len(usuarios)
    print("Opção 4 - Alterar dados do usuário")
    print("==================================")
    usuario = input("Nome do usuário: ")
    print("")
    print("Qual informação deseja alterar?")
    print("(1) - Nome")
    print("(2) - CPF")
    print("(3) - Idade")
    print("(4) - Sexo")
    print("(5) - Salário")
    alterar = int(input("Opção: "))
    while i < Tam and usuarios[i]["Nome"] != usuario:
        i += i

    if alterar == 1:
        usuarios[i]["Nome"] = input("Novo nome: ")
    elif alterar == 2:
        usuarios[i]["CPF"] = int(input("Novo CPF: "))
    elif alterar == 3:
        usuarios[i]["Idade"] = int(input("Nova Idade: "))
    elif alterar == 4:
        usuarios[i]["Sexo"] = input("Novo Sexo: ")
    elif alterar == 5:
        usuarios[i]["Salario"] = int(input("Novo Salário: "))



def idadeMediaUsuarios(usuarios):
    soma = 0
    i = 0
    Tam = len(usuarios)
    print("Opção 5 - Idade média dos usuários")
    print("==================================")
    while i < Tam:
        soma = usuarios[i]["Idade"] + soma
        i += 1
    media = soma / Tam
    print("Média = ", media)



def listarSalarioUsuarios(usuarios):
    i = 0
    Tam = len(usuarios)
    print("Opção 6 - Listar salário dos usuários")
    print("==================================")
    while i < Tam:
        print("Nome: ", usuarios[i]["Nome"])
        print("Salário: ", usuarios[i]["Salario"])
        print("")
        i += 1



def mediaSalarioUsuarios(usuarios):
    i = 0
    Tam = len(usuarios)
    soma = 0
    print("Opção 7 - Média do salário dos usuários")
    print("==================================")
    while i < Tam:
        soma = usuarios[i]["Salario"] + soma
        i += 1
    media = soma / Tam
    print("Média: ", media)



def deletarUsuario(usuarios):
    i = 0
    Tam = len(usuarios)
    print("Opção 8 - Deletar usuário")
    print("==================================")
    deletar = input("Nome do usuário à ser deletado: ")
    while i < Tam and deletar != usuarios[i]["Nome"]:
        i += 1
    del(usuarios[i])
    print("O contato foi excluído com sucesso!")



moduloPrincipal()
