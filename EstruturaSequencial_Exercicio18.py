# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb = float(input('Informe o tamanho da arquivo em Megabit: '))
mbps = float(input(('Informa a velocidade de sua interne em mbps: ')))
tempo = (mb/(mbps/8))/60
print(tempo)
