# vetores
media_aluno = []
notas = []

# Função para encontrar a média das notas
def func_media(notas):
    return (sum(notas) / len(notas))

# Loop para inserir notas dos 10 alunos
for _ in range(10):
    nota_1 = float(input("Inserir nota 1:"))
    nota_2 = float(input("Inserir nota 2:"))
    nota_3 = float(input("Inserir nota 3:"))
    nota_4 = float(input("Inserir nota 4:"))

# Adicionar as notas em uma lista para acionar a função 
    notas.extend([nota_1, nota_2, nota_3, nota_4])

# Encontrar as medias atravez da função (func_media) e adicionar na lista media_aluno
    media_aluno.extend([func_media(notas)])

# Contabilizar o número de alunos com media igual ou superior a 7 dentro da lista.
alunos_aprovados = sum(media >= 7 for media in media_aluno)

# Imprimir o resultado
print(f"O número de alunos com a média igual ou maior que 7: ", alunos_aprovados)
    