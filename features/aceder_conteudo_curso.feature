Feature: Aceder ao conteúdo do curso

    Scenario: Aceder ao conteúdo do curso com matrícula ativa
        Given que acesso o site Iterasys Learnworlds
        When clico em Entrar
        And preencho os campos de login
        And clico no botão Entrar
        Then sou direcionado para página Home
        When acesso ao Perfil através do botao Visit profile
        And clico em Edit profile
        And clico em Pro na secção Cursos e programas
        Then sou direcionado para página dos Cursos
        And posso aceder ao conteúdo dos cursos