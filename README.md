Meu CRUD em Python com MySQL

Essa é uma aplicação CRUD (Create, Read, Update, Delete) desenvolvido em Python utilizando o banco de dados MySQL.
O sistema permite autenticar usuários e, dependendo do tipo (admin ou comum), acessar menus diferentes para manipular os dados.

No menu administrador, é possível:

  °Inserir usuários

  °Consultar tabelas de usuários e administradores

  °Excluir registros

  °Voltar para a tela de login ou encerrar o programa.

No menu usuário, é possível:

  °Inserir novos registros

  °Consultar as tabelas

  °Voltar para autenticação ou encerrar o programa

A autenticação é feita consultando o banco de dados, garantindo que apenas usuários cadastrados possam acessar o sistema.
Com isso, consegui estruturar um CRUD completo em Python, conectado ao MySQL, com separação de responsabilidades entre módulos (auth, admin, usuario, db e main).
