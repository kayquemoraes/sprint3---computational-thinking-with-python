# Dicionário que armazena informações dos usuários, incluindo seus nomes, senhas e saldos.
usuarios = {
    "nomes": [],   # Lista para armazenar os nomes dos usuários.
    "senhas": [],  # Lista para armazenar as senhas dos usuários.
    "saldo": []    # Lista para armazenar os saldos dos usuários.
}

# Dicionário que armazena informações sobre diferentes materiais recicláveis, seus códigos e preços.
materiais = {
    "material": ["plastico", "metal", "vidro", "papel"],  # Lista de tipos de materiais recicláveis.
    "codigo": [["000a", "000c", "0005"], ["000b", "0004"], ["0001", "0002"], ["000d", "0003"]],  # Códigos de barras dos materiais.
    "preco": [5, 10, 15, 20]  # Lista de preços associados a cada tipo de material.
}

# Função para validar a opção escolhida pelo usuário em um menu.
def validar_opcao(lista, frase):
    opcao = input(frase)
    while opcao not in lista:
        print("Digite uma opção válida.")
        opcao = input(frase)
    return opcao

# Função para imprimir os valores de um dicionário de forma recursiva.
def printa_dicionarios(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionarios(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return

# Função para registrar um novo usuário no sistema.
def registrar_usuario():
    while True:
        novo_usuario = input("Nome de usuário: ").lower()
        if novo_usuario in usuarios["nomes"]:
            print(f"{novo_usuario} já existe. Por favor, escolha outro.")
        else:
            nova_senha = input("Senha: ")
            usuarios["nomes"].append(novo_usuario)
            usuarios["senhas"].append(nova_senha)
            usuarios["saldo"].append(0)
            print("Registro bem-sucedido!")
            break
    return novo_usuario

# Função para permitir que um usuário faça login no sistema.
def login_usuario():
    while True:
        usuario = input("Nome de usuário: ").lower()
        senha = input("Senha: ")
        if usuario in usuarios["nomes"] and senha == usuarios["senhas"][usuarios["nomes"].index(usuario)]:
            print("Login bem-sucedido!")
            break
        else:
            print("Nome de usuário ou senha incorretos.")
            opcao = validar_opcao(['1','2'],"[1] Tentar novamente\n[2] Registrar-se\nDigite: ").lower()
            if opcao == "2":
                registrar_usuario()
    return usuario

# Função para permitir que um usuário deposite um resíduo na lixeira.
def depositar_residuo(usuario):
    residuo = input("\nDigite o código de barras do produto a ser descartado: ")
    contem = False
    for i in range(len(materiais["codigo"])):
        if residuo in materiais["codigo"][i]:
            contem = True

    if contem:
        for i in range(len(materiais["codigo"])):
            for j in range(len(materiais["codigo"][i])):
                if residuo == materiais["codigo"][i][j]:
                    qtd = int(input("Digite a quantidade deste resíduo: "))
                    material = materiais["material"][i]
                    if material not in cupom["residuos"].keys():
                        cupom["residuos"][material] = qtd
                    else:
                        cupom["residuos"][material] += qtd
                    cupom["valor total"] += qtd * materiais["preco"][i]
                    usuarios["saldo"][usuarios["nomes"].index(usuario)] += qtd * materiais["preco"][i]

        print("Resíduo depositado com sucesso!")
    else:
        print('''\nOps! Não encontramos esse produto na nossa base. 
Verifique se o código foi digitado corretamente, com 4 dígitos. 
Se sim, acesse a opção [2] para consultá-lo e tente novamente. ''')
    return

# Função para consultar se um produto está cadastrado na base de dados.
def consultar_produto():
    residuo = input("\nDigite o código de barras do produto a ser descartado: ")
    contem = False
    for i in range(len(materiais["codigo"])):
        if residuo in materiais["codigo"][i]:
            contem = True

    if contem:
        print("Esse produto já está cadastrado na nossa base!")
    else:
        print("Esse produto ainda não está cadastrado no nosso sistema. ")
        cadastrar = validar_opcao(['1', '2'], "Deseja cadastrar?\n[1] Sim\n[2] Não\nDigite: ")
        if cadastrar == '1':
            opcao = validar_opcao(['1','2','3','4'],"[1] Plástico\n[2] Metal\n[3] Vidro\n[4] Papel\nDigite a composição do produto:  ")
            opcao = int(opcao)
            cadastrar_produto(residuo, opcao)

# Função para cadastrar um novo produto na base de dados.
def cadastrar_produto(codigo, composicao):
    materiais["codigo"][composicao-1].append(codigo)
    print("Resíduo cadastrado com sucesso!")
    return

# Função para consultar o saldo de um usuário.
def consultar_saldo(usuario):
    print(f'Seu saldo é: {usuarios["saldo"][usuarios["nomes"].index(usuario)]}')

# Função para apresentar informações sobre a lixeira inteligente.
def conhecer_lixeira():
    print('''Você já imaginou poder ajudar o meio ambiente e ainda ser recompensado por isso? Pois agora isso é 
possível com a EcoSort! Para usá-la, é muito simples: basta aproximar o código de barras de uma embalagem cadastrada 
em nossa base e depositá-la que ela já será reciclada. E o melhor: você ganha prêmios por fazer sua parte!

A EcoSort é capaz de reconhecer qual material foi depositado para separá-lo e garantir que sejam descartados corretamente. 
Além disso, com o nosso sistema de recompensas, você acumulará pontos que poderão ser trocados por recompensas de nossos 
parceiros de acordo com a quantidade de itens depositados. Ou seja, quanto mais itens reciclar, mais créditos receberá
e mais recompensas poderá trocar!

Além disso, caso uma embalagem não esteja registrada no nosso sistema, basta cadastrá-la em nosso site para que nosso
time faça a validação e cadastre-a na base de dados. Dessa forma, todas as embalagens poderão ser descartadas por aqui.
Não é demais? 

E não para por aí! Com a lixeira inteligente, você ainda contribui para a construção de um futuro mais sustentável e
ajuda a preservar o meio ambiente para as próximas gerações. Então, o que está esperando? Faça parte desse movimento 
pela reciclagem e comece a ser recompensado por suas ações conscientes! ''')

# Solicitar ao usuário que escolha entre fazer login ou registrar uma nova conta.
while True:
    # Dicionário que armazena informações do cupom, incluindo o nome de usuário, resíduos depositados e o valor total acumulado.
    cupom = {
        "nome de usuario": "",  # Nome de usuário associado às atividades da sessão.
        "residuos": {},  # Dicionário para armazenar os resíduos depositados e suas quantidades.
        "valor total": 0  # Valor total acumulado com base nos resíduos depositados.
    }
    opcao = validar_opcao(['1','2'],"[1] Entrar\n[2] Registrar\nDigite: ")
    if opcao == '1':
        usuario = login_usuario()
    else:
        usuario = registrar_usuario()
    cupom["nome de usuario"] = usuario

    while True:
    # Loop principal que permite que o usuário realize várias atividades.
        atividade = validar_opcao(["1", "2", "3", "4", "5"], '''\nO que você quer fazer?
[1] Depositar um resíduo na lixeira
[2] Consultar ou cadastrar um produto
[3] Consultar seu saldo
[4] Conhecer nossa lixeira
[5] Encerrar sua sessão\nDigite: ''')

        if atividade == "1":
            depositar_residuo(usuario)

        elif atividade == "2":
            consultar_produto()

        elif atividade == "3":
            consultar_saldo(usuario)
        elif atividade == "4":
            conhecer_lixeira()
        else:
            print("\nObrigado por usar nossa lixeira!")
            printa_dicionarios(cupom)
            print("\n")
            break
