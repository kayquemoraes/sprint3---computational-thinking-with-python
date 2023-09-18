# EcoSort - Sistema de Reciclagem Inteligente

## Descrição do Projeto

O EcoSort é um sistema de reciclagem inteligente que permite aos usuários depositar resíduos recicláveis em uma lixeira especial. O sistema reconhece os materiais recicláveis com base em códigos de barras e recompensa os usuários com pontos que podem ser trocados por prêmios. Além disso, os usuários podem consultar seu saldo, cadastrar novos produtos no sistema e aprender mais sobre o funcionamento da lixeira inteligente.

## Como Usar o EcoSort

Para utilizar o EcoSort, siga os passos abaixo:

### 1. Iniciar o Programa

Execute o código Python do EcoSort em seu ambiente de desenvolvimento favorito. O programa será iniciado e apresentará um menu com as seguintes opções:

- Entrar
- Registrar

Digite "1" para entrar no sistema se já tiver uma conta ou "2" para registrar uma nova conta.

### 2. Login ou Registro

#### Se você escolher "Entrar (1)":

- Digite seu nome de usuário e senha quando solicitado.
- Se as informações estiverem corretas, você fará login com sucesso.
- Caso contrário, o sistema informará que as credenciais estão incorretas e você poderá tentar novamente ou registrar uma nova conta.

#### Se você escolher "Registrar (2)":

- Digite um nome de usuário e senha para criar uma nova conta.
- O sistema verificará se o nome de usuário já existe. Se sim, você será solicitado a escolher outro nome de usuário.
- Após o registro bem-sucedido, você fará login automaticamente.

### 3. Menu Principal

Após o login ou registro, você será redirecionado para o menu principal com as seguintes opções:

- Depositar um resíduo na lixeira
- Consultar ou cadastrar um produto
- Consultar seu saldo
- Conhecer nossa lixeira
- Encerrar sua sessão

Digite o número correspondente à opção que deseja executar.

### 4. Depositar um Resíduo na Lixeira

- Escolha a opção "Depositar um resíduo na lixeira" no menu.
- Digite o código de barras do produto a ser descartado.
- O sistema verificará se o código de barras corresponde a um produto cadastrado.
- Digite a quantidade do resíduo a ser depositado.
- O sistema calculará o valor total dos resíduos depositados com base nos preços dos materiais.
- Os pontos serão adicionados ao seu saldo.

### 5. Consultar ou Cadastrar um Produto

- Escolha a opção "Consultar ou cadastrar um produto" no menu.
- Digite o código de barras do produto que deseja consultar.
- O sistema verificará se o produto está cadastrado. Se não estiver, você poderá cadastrá-lo.

### 6. Consultar Seu Saldo

- Escolha a opção "Consultar seu saldo" no menu.
- Seu saldo atual de pontos será exibido.

### 7. Conhecer Nossa Lixeira

- Escolha a opção "Conhecer nossa lixeira" no menu.
- Você receberá informações sobre o funcionamento da lixeira inteligente e como você pode ajudar o meio ambiente enquanto ganha recompensas.

### 8. Encerrar Sua Sessão

- Escolha a opção "Encerrar sua sessão" no menu.
- Sua sessão será encerrada e você será desconectado do sistema.

## Exemplo de Execução

Aqui está um exemplo simulado de como o EcoSort pode ser usado:

```python
[1] Entrar
[2] Registrar
Digite: 2

Nome de usuário: novo_usuario
Senha: nova_senha
Registro bem-sucedido!

[1] Depositar um resíduo na lixeira
[2] Consultar ou cadastrar um produto
[3] Consultar seu saldo
[4] Conhecer nossa lixeira
[5] Encerrar sua sessão
Digite: 1

Digite o código de barras do produto a ser descartado: 000a
Digite a quantidade deste resíduo: 3
Resíduo depositado com sucesso!

[1] Depositar um resíduo na lixeira
[2] Consultar ou cadastrar um produto
[3] Consultar seu saldo
[4] Conhecer nossa lixeira
[5] Encerrar sua sessão
Digite: 3

Seu saldo é: 15

[1] Depositar um resíduo na lixeira
[2] Consultar ou cadastrar um produto
[3] Consultar seu saldo
[4] Conhecer nossa lixeira
[5] Encerrar sua sessão
Digite: 5

Obrigado por usar nossa lixeira!
nome de usuario : novo_usuario
plastico: 3
valor total : 15

```


## Contribuição

Sinta-se à vontade para contribuir com melhorias neste projeto. Você pode adicionar recursos adicionais, aprimorar a interface do usuário ou fazer correções de bugs.

Esperamos que o EcoSort seja útil para promover a reciclagem e a conscientização ambiental. Faça a sua parte e seja recompensado por suas ações sustentáveis!
