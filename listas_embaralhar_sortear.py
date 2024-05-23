import random 
alunos=['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana']
print(f"Lista: {alunos}")
#Embaralhar lista 
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
#Escolha um aluno aleatoriamente 
aluno_sorteado = random.choice(alunos)
print(f"Aluno sorteado: {aluno_sorteado}")