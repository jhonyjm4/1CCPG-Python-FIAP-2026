idade = int(input('Insira a sua Idade: '))

if idade < 16:
    print('Você não pode votar!')
elif 16 <= idade < 18 or idade >= 70:
    print('O seu voto é opicional!')
else:
    print('Você tem a obrigação de votar!')
