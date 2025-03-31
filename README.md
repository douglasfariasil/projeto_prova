# Classificador de Alunos

Este script Python classifica alunos com base em suas médias e permite verificar a situação de um aluno específico.

## Funcionalidades

* Armazena nomes e médias de alunos em um dicionário.
* Classifica os alunos em três categorias: aprovados, recuperação e reprovados.
* Solicita ao usuário o nome de um aluno para verificar sua situação.
* Exibe a situação do aluno (aprovado, em recuperação ou reprovado).

## Como usar

1.  Clone este repositório.
2.  Execute o script `main.py`.
3.  Quando solicitado, digite o nome do aluno que você deseja verificar.


Dicionário de Alunos:

Cria um dicionário chamado alunos para armazenar o nome de cada aluno como chave e sua respectiva média como valor.
Listas para Resultados:

Inicializa três listas vazias: aprovados, recuperacao e reprovados. Essas listas serão usadas para guardar os nomes dos alunos em cada categoria.
Classificação dos Alunos:

Utiliza um loop for para iterar sobre os itens (nome e média) do dicionário alunos.
Dentro do loop, verifica a média de cada aluno:
Se a média for maior que 7, o nome do aluno é adicionado à lista aprovados.
Se a média estiver entre 5 (inclusive) e 7 (exclusive), o nome do aluno é adicionado à lista recuperacao.
Caso contrário (média menor que 5), o nome do aluno é adicionado à lista reprovados.
Solicitação de Nome ao Usuário:

A função input() é usada para pedir ao usuário que digite o nome do aluno que ele deseja verificar. O nome digitado é armazenado na variável nome_aluno.
Verificação da Situação do Aluno:

Uma série de condicionais if, elif e else verifica em qual das listas (aprovados, recuperação ou reprovados) o nome_aluno se encontra.
Dependendo da lista em que o aluno está, uma mensagem informando a sua situação (aprovado, em recuperação ou reprovado) é impressa na tela.
Se o nome do aluno não for encontrado em nenhuma das listas, uma mensagem informando que o aluno não foi encontrado é exibida.
