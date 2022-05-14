def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f' Com {idade} não vota.'
    elif 16 <= idade < 18 or idade >65:
        return f'Com {idade} o voto é opcional.'
    elif idade >= 18:
        return f'Com {idade} é obrigatório votar.'


nasc = int(input('Digite o seu ano de nascimento: '))

print(voto(nasc))