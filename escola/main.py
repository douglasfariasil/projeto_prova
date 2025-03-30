# Aprovação ou reprovação na prova da escola.
# Lista de alunos e suas respectivas médias

alunos = {
    "Douglas": 9,
    "Fernanda": 10,
    "João": 6,
    "Mamuela": 8,
    "Miguel": 8,
    "Cintia": 9,
    "Maria": 5,
    "Regina": 4,
    "Pedro": 5,
    "Renata": 3,
    "Felipe": 2,
    "Raquel": 3,
    "Natalhia": 7
}

# Listas para armazenar os alunos aprovados, em recuperação e reprovados

aprovados = []
recuperacao = []
reprovados = []

# Classifica os alunos com base em suas médias

for nome, media in alunos.items():
    if media > 7:
        aprovados.append(nome)
    elif 5 <= media < 7:
        recuperacao.append(nome)
    else:
        reprovados.append(nome)

# Solicita que o usuario adicione o nome para verificar a situação.

nome_aluno = input("Digite o nome do aluno para verficar a situação: ")

# Verifica em qual lista o aluno se encontra

if nome_aluno in aprovados:
    print(f"{nome_aluno} está aprovado(a).")
elif nome_aluno in recuperacao:
    print(f"{nome_aluno} está em recupetação.")
elif nome_aluno in reprovados:
    print(f"{nome_aluno} está reprovado(a).")
else:
    print(f"{nome_aluno} não encotrado(a) na lista de aluno.")

