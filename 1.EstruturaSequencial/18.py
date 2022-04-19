# 18 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

t = float(input('TAMANHO DO ARQUIVO (EM MB): '))
v = float(input('VELOCIDADE DA CONEXÃO (EM Mbps): '))


tamanhoBits = t * 1024 * 1024 * 8
tempoSegundos = tamanhoBits / (v * 1024 * 1024)
tempoMinutos = tempoSegundos / 60

print(f'TEMPO DE DOWNLOAD: {tempoMinutos:.2f} MIN')