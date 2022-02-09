nome = ["admin"]
login = ["admin"]
senha = ["admin"]
Opcao = 0 


def MenuPrincipal():
    Opcao = 0 
    while Opcao != 5:
        print("")
        print("====== MENU DE OPÇÕES ======")
        print("Opção 1 - Fazer Cadastro")
        print("Opção 2 - Lista de Usuários")
        print("Opção 3 - Editar Usuário")
        print("Opção 4 - Deletar Usuário")
        print("Opção 5 - Sair")
        Opcao = int(input("Opção escolhida: "))
        print("")
        if Opcao == 1:
            Cadastro(nome, login, senha)
        elif Opcao == 2:
            ListarUsuarios(nome, login, senha)
        elif Opcao == 3:
            EditarUsuario(nome, login, senha)
        elif Opcao == 4:
            DeletarUsuario(nome, login, senha)
        elif Opcao == 5:
            print("Finalizando...")



def fazerLogin(loginUser, senhaUser, login, senha):

    if loginUser in login and senhaUser in senha:
        print("")
        print("Usuário autorizado!")
        print("")
        return True
  
    else:
        print("")
        print("Login ou senha inválido!")
        print("")
        return False



def Cadastro(nome, login, senha):
    print("")
    loginUser = input("Por favor insira o seu login: ")
    senhaUser = input("Por favor insira a sua senha: ")
    print("")
    created = False
    nameCreated = False

    if fazerLogin(loginUser, senhaUser, login, senha):
        while created == False:
            while nameCreated == False:
                newName = input("Nome do usuário a ser adicionado: ")
                if newName in nome:
                    print("O nome de usuário já está em uso! Escolha outro.")
                else:
                    nome.append(newName)
                    nameCreated = True

            newLogin = input("Novo login do usuário: ")
            login.append(newLogin)

            newSenha = input("Nova senha do usuário: ")
            senha.append(newSenha)
            print("Usuário criado com sucesso!")
            created = True



def ListarUsuarios(nome, login, senha):
    loginUser = input("Por favor insira o seu login: ")
    senhaUser = input("Por favor insira a sua senha: ")

    if fazerLogin(loginUser, senhaUser, login, senha):
        print("")
        print("Listar usuário específico ou todos os usuários?")
        print("(1) - Usuario Específico")
        print("(2) - Todos os usuários")
        resposta = int(input("Opção: "))

        if resposta == 1:
            searchUser = input("Nome do usuário: ")
            index = nome.index(searchUser)
            print("Login do usuário:", login[index])
            print("Senha do usuário:", senha[index])
            
        elif resposta == 2:
            print("Nome do usuário:", nome)
            print("Login do usuário:", login)
            print("Senha do usuário:", senha)



def EditarUsuario(nome, login, senha):

    print("")
    nameUser = input("Nome do Usuário a ser alterado: ")
    print("")
    
    if nameUser in nome:
        index = nome.index(nameUser)
        print("")
        print("Qual informação deseja alterar?")
        print("(1) - Nome")
        print("(2) - Login")
        print("(3) - Senha")
        Opcao = int(input("Opção Escolhida: "))

        if Opcao == 1:
            newName = input("Novo nome: ")
            nome[index] = newName
            print("Nome alterado com sucesso!")

        elif Opcao == 2:
            newLogin = input("Novo login: ")
            login[index] = newLogin
            print("Login alterado com sucesso!")

        elif Opcao == 3:
            newSenha = input("Nova senha: ")
            senha[index] = newSenha
            print("Senha alterado com sucesso!")
            
    else:
        print("O usuário não está cadastrado.")


def DeletarUsuario(nome, login, senha):
    print("")
    userToBeDeleted = input("Nome do usuário a ser deletado: ")
    print("")
    index = nome.index(userToBeDeleted)

    if userToBeDeleted in nome:
        del(nome[index])
        del(login[index])
        del(senha[index])
        print("Usuário deletado com sucesso!")

    else:
        print("Esse usuário não existe.")


MenuPrincipal()
    