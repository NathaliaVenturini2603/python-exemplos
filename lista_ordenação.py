mport random 
alunos=['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana']
print(f"Lista: {alunos}")
#Embaralhar lista 
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
#Ordena a lista Crescente
alunos.sort()
print(f"Lista crescente: {alunos}")
#Ordena a lista Decrescente 
alunos.sort(reverse=True)
print(f"Lista Decrescente: {alunos}")
