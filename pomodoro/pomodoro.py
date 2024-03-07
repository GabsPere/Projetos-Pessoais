# Código para criar um timer pomodoro com contador de vezes utilizado.

# importando módulos
import time
import os
import sys
# Declarando variável global
contador = 1

while contador <= 4:
    opcao = int(input('Você deseja iniciar o pomodoro?\n1-Sim 2-Não 3-Sair\n'))
    if opcao == 1:
        tempo = int(input('Quantos minutos?\n'))
        print(f"Pomodoro de número {contador} iniciado..")
        contagem = tempo*60
        time.sleep(contagem)
        os.system("beep -f 2000 -l 1500")
        contador += 1
    elif opcao == 2:
        print('Aguardando...')
    elif opcao == 3:
        print("Saindo do programa..")
        time.sleep(0.3)
        sys.exit()
    else:
        print("opção invalida")
os.system("beep -f 2000 -l 1500")
os.system("beep -f 2000 -l 1500")
print("Você realizou 4 pomodoros, faça uma pausa de 20 minutos (:")
