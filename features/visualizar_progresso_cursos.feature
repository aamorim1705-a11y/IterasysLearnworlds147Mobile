Feature: Visualizar o progresso dos cursos

    Scenario: Visualizar o progresso dos cursos
        Given que acesso o site Iterasys Learnworlds
        When clico em Entrar
        And preencho os campos de login
        And clico no botão Entrar
        Then sou direcionado para página Home
        When acesso ao Perfil através do botao Visit profile
        And clico em Edit profile
        And clico no programa disponível Pro na secção Cursos e programas
        Then consigo visualizar o progresso dos cursos