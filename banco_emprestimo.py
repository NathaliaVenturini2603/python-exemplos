print(f'programa de emprestimo f"Responda: (0-Não ou 1-Sim)')
nome_negativado=int(input("Possui nome negativado?: "))
if nome_negativado == 1:
    print('Não pode realizar empréstimo')
else: 
    carteira_assinada=int(input('Possui carteira assinada?: '))
    if carteira_assinada == 0:
        print('Não pode realizar empréstimo')
    else: 
        casa_própria=int(input('Possui casa própria?: '))
        if casa_própria == 0:
            print('Não pode realizar empréstimo')
        else:
            print('Conceder empréstimo')