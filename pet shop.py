usuario_admin = []
usuario = []
pets = []
while True:
    login = False
    if len(usuario_admin) == 0:
        print('nao ha registros de usuarios')
        nomeUsuario = input('crie um login: ') 
        nomeUsuario.lower
        senha = input('crie uma senha: ')
        usuario_admin.append([nomeUsuario,senha,'A'])
        login = True
        
    else:
        nomeUsuario = input('confirme usuario: ')
        senha = input('confirme a senha: ')
        for i in range(len(usuario_admin)):
            if nomeUsuario == usuario_admin[i][0]:
                if senha == usuario_admin[i][1]:
                    print('usuario autenticado')
                    login = True
            while True:
                import time
                print('CADASTROS')
                print("1. cadastrar")
                print("2. pets")
                print("3. serviços")
                print("4. consultar")
                print("5.voltar")
                    
                opcoes = input('escolha uma das opcoes de "1" a "4": ')
                
                if (opcoes == "1"):
                    nome = input('digite seu nome: ')
                    telefone = input('digite seu telefone: ')
                    email = input('digite seu email: ')
                    cep = input('digite seu cep: ')
                    usuario.append([nome,telefone,email,cep]) #lista de usuarios cadastrados
                    print('Novo Usuario Registrado!')
                elif (opcoes == "2"):
                    id_pet = input('id do pet')
                    cpf_dono = input('digite o cpf do dono')
                    nome_pet = input('digite o nome do pet')
                    escolha_C = input('categoria')
                    data = input('data de aniversario do pet')

                    pets.append([id_pet,cpf_dono,nome_pet,escolha_C,data]) #lista dos pets
                
                elif (opcoes == "3"):
                    id_pet = input('digite o ID do pet: ')
                    for i in range (len(pets)):   
                        if id_pet == pets[i][0]:
                            print(pets[i][0])
                            if (pets):
                                print('ESCOLHA UM DOS NOSSOS SERVICOS!!')
                                print('''
                                    1. Banho
                                    2. Tosa
                                    3. Servico completo
                                    4. vacinação
                                    5.voltar para o menu
                                    ''')
                                servicos = input('escolha um dos servicos a cima: ')
                                escolha_servico = {"banho":"banho custa 35R$",
                                                    "Tosa":"Tosa custa 40R$",
                                                    "Servico Completo":"Servico Completo custa 60R$"}
                                
                                s1 = escolha_servico.get("banho")
                                s2 = escolha_servico.get("Tosa")
                                s3 = escolha_servico.get("Servico Completo")
                                s4 = escolha_servico.get("vacinação")
                                if servicos == "1":
                                    print(s1)
                                    pets.append([s1])
                                
                                if servicos == "2":
                                    print(s2)
                                    pets.append([s2])
                                
                                if servicos == "3":
                                    print(s3)
                                    pets.append([s3])
                                
                                if servicos == "4":
                                    print(s4)
                                    pets.append([s4])
                                     
                                if servicos == "5":
                                    break        
                                    

                elif (opcoes == "4"):
                    
                    print(usuario)
                    print("id do pet","cpf do dono","nome do pet","categoria","aniversario")
                    print(pets)
                    
                    print('''
                    id servico
                    id pet
                    data de (atendimento/agendamento/consulta/conclusao)
                    ''')
        if login:
            break            
        
