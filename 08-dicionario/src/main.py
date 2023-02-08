estudantes = {}

qtd_alunos = int(input("\nQuantos alunos? "))

for i in range(1, qtd_alunos+1):
    boletim = []
    nome = input(f"\nInsira o nome do aluno {i}: ")

    for j in range(1):
        media = float(input(f"Informe a média do aluno {i}: "))
        boletim.append(media)

    estudantes[nome] = boletim

print(estudantes.items())

for nome, boletim in estudantes.items():
    if boletim[0] >= 7:
        status = "aprovado"
    else:
        status = "reprovado"

    boletim.append(status)

    print(
        "\n", end=""
        f"Aluno {nome} foi {status}."
    )

print("\n", end="")
print(f"\n{estudantes}")
