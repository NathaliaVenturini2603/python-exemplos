nota1 = int(input('Informe a nota do 1° bimestre (0-100): '))
nota2 = int(input('Informe a nota do 2° bimestre (0-100): '))
media = (nota1 + nota2) / 2 
if media >= 60: 
    print(f'Aprovado com a media: {media}')
else: 
    print(f'Reprovado com a media: {media}')