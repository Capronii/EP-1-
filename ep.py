import random 

def Pass_line_Come_out (soma_dos_dados):
    if soma_dos_dados == 7 or soma_dos_dados == 11:
        return 'Vitória direta'
    if soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:
        return 'Perda direta'
    if soma_dos_dados == 4 or soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 8 or soma_dos_dados == 9 or soma_dos_dados == 10:
        return 'Mudou de fase'


def Pass_line_Point (soma_dos_dados, point):
    if soma_dos_dados == point:
        return 'Ganhou point'
    elif soma_dos_dados == 7:
        return 'Perdeu point'
    else:
        return 'Volta'


def Field (soma_dos_dados):
    if soma_dos_dados==5 or soma_dos_dados==6 or soma_dos_dados==7 or soma_dos_dados==8:
        return 'perde'
    if soma_dos_dados==3 or soma_dos_dados==4 or soma_dos_dados==9 or soma_dos_dados==10 or soma_dos_dados==11:
        return 'Vito'
    if soma_dos_dados==2:
        return 'dois'
    if soma_dos_dados==12:
        return 'doze'
    

def Anycraps (soma_dos_dados):
    if soma_dos_dados==2 or soma_dos_dados==3 or soma_dos_dados==12:
        return 'craps1'
    else:
        return 'craps2'

def Twelve(soma_dos_dados):
    if soma_dos_dados==12:
        return 'twelve1'
    else:
        return 'twelve2'

#Início do jogo

din = 100
print('\n\033[1;34m''Bem Vindo ao Craps!''\033[0;0m')
print('Você tem {} fichas para apostar.'.format(din))

regra = input('\n\033[1;90mVocê deseja saber as regras? (sim/nao) \033[1;90m')
if regra == 'sim':
    print('''\033[1;90m
      Pode-se escolher entre 4 tipos de aposta:

      1- Pass line bet:
      Durante a primeira fase ("Come Out") dessa opção de aposta se a soma dos dados lançados for igual a 7 ou 11, o jogador ganha o que apostou. Se for igual a 2, 3 ou 12 o jogador perde o que apostou.
      Caso a soma dos dados der 4, 5, 6, 8, 9 ou 10 o jogador muda para a fase "Point". O dado é lançado novamente e sua soma tem que ser igual a soma inicial (número "Point") ou a 7, caso contrário o dado é jogado novamente.
      Se a soma for 7, o jogador perde o que apostou e se for igual ao número point o jogador ganha. Durante essa fase do jogo, enquanto os dados são lançados novamente, o jogador tem a opção de apostar nas outras opções de aposta. (Field, Any Craps e Twelve)
      
      2- Field: 
      Esse tipo de aposta consiste em se a soma dos dados lançados for igual a 5, 6, 7 ou 8, o jogador perde a aposta. Se a soma for 3, 4, 9, 10 ou 11, o jogador vence. Caso a soma for igual a 2, o jogador ganha o dobro de sua aposta. Além disso, caso a soma for igual a 12, o jogador ganha o triplo do que apostou
      
      3- Any Craps:
      Nesse tipo de aposta apenas as somas iguais a 2, 3 ou 12 te fazem vencer e o jogador ganha sete vezes o valor apostado. Caso contrário a aposta é perdida

      4- Twelve:
      Nesta opção a única soma que te leva a vencer é 12 e o jogador ganha 30 vezes o valor apostado.\033[1;90m\n''')


while din > 0:
    fase = 'Come out'
    print('\n\033[1;34m''Você está na fase {}.''\033[0;0m'.format(fase))

    sair = input('\n\033[34m''Você quer sair do jogo?(sim/nao): ''\033[0;0m')
    if sair == 'sim':
        break

    while True:
        aposta1 = int(input('\n\033[34m'"Quanto você quer apostar no Pass Line Bet? "'\033[0;0m'))
        if aposta1 <= din and aposta1 >= 0:
            din -= aposta1
            break
        elif aposta1 < 0:
            print('\033[31m''Erro: o valor da aposta não é um número inteiro positivo, aposte novamente.''\033[0;0m')
        else:
            print('\033[31m''Erro: o valor da aposta no Pass Line Bet é maior do que a quantidade das suas fichas. Aposte outro valor.''\033[0;0m')

    while True: 

        while True:
            
            print('Você ainda tem {} ficha(s) para apostar.'.format(din))
            aposta2 = int(input('\n\033[34m'"Quanto você quer apostar no Field? "'\033[0;0m'))
            if aposta2 <= din and aposta2 >= 0:
                din -= aposta2
                break
            elif aposta2 < 0:
                print('\033[31m''Erro: o valor da aposta não é um número inteiro positivo, aposte novamente.''\033[0;0m')
            else:
                print('\033[31m''Erro: o valor da aposta no Field é maior do que a quantidade das suas fichas. Aposte outro valor.''\033[0;0m')

        while True:
            print('Você ainda tem {} ficha(s) para apostar'.format(din))
            aposta3 = int(input('\n\033[34m'"Quanto você quer apostar no Any Craps? "'\033[0;0m'))
            if aposta3 <= din and aposta3 >= 0:
                din -= aposta3
                break
            elif aposta3 < 0:
                print('\033[31m''Erro: o valor da aposta não é um número inteiro positivo, aposte novamente.''\033[0;0m')
            else:
                print('\n\033[31m''Erro: o valor da aposta no Any Craps é maior do que a quantidade das suas fichas. Aposte outro valor.''\033[0;0m')

        while True:
            print('Você ainda tem {} ficha(s) para apostar'.format(din))
            aposta4 = int(input('\n\033[34m'"Quanto você quer apostar no Twelve? "'\033[0;0m'))
            if aposta4 <= din and aposta4 >= 0:
                din -= aposta4
                break
            elif aposta4 < 0:
                print('\033[31m''Erro: o valor da aposta não é um número inteiro positivo, aposte novamente.''\033[0;0m')
            else:
                print('\n\033[31m''Erro: o valor da aposta no Twelve é maior do que a quantidade das suas fichas. Aposte outro valor.''\033[0;0m')
        
        
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)

        print('\nDado 1:',dado1)
        print('Dado 2:',dado2)

        soma_dos_dados = dado1 + dado2
        print('Soma dos dados: {}\n'.format(soma_dos_dados))

        if fase == 'Come out':
            resultado_Pass = Pass_line_Come_out (soma_dos_dados)
            point = soma_dos_dados
            if resultado_Pass == 'Vitória direta' and aposta1>0:
                print('\033[32m''Parabéns! Você ganhou no Pass Line Bet na fase Come Out!''\033[0;0m')
                din = din + 2*aposta1
            elif resultado_Pass == 'Perda direta' and aposta1>0:
                print('\033[31m''Você perdeu no Pass Line Bet na fase Come Out.''\033[0;0m')
            else:
                if aposta1 > 0:
                    fase = 'Point'
                    print('Você mudou para a fase Point.')

        else:
            resultado_Pass_line_Point = Pass_line_Point(soma_dos_dados, point)
            if resultado_Pass_line_Point == 'Ganhou point' and aposta1>0:
                print('\033[32m''Parabéns! Você ganhou no Pass Line Bet na fase Point!''\033[0;0m')
                din = din + 2*aposta1
                fase = 'Come out'
            elif resultado_Pass_line_Point == 'Perdeu point' and aposta1>0:
                print('\033[31m''Você perdeu no Pass Line Bet na fase Point.''\033[0;0m')
                fase = 'Come out'

        result_Field = Field (soma_dos_dados)
        if result_Field == 'perde' and aposta2>0:
            print('\033[31m''Você perdeu no Field.''\033[0;0m')
            
        elif result_Field == 'Vito' and aposta2>0:
            print('\033[32m''Parabéns! Você ganhou no Field!''\033[0;0m')
            din = din + 2*aposta2
                
        elif result_Field == 'dois' and aposta2>0:
            print('\033[32m''Parabéns! Você ganhou em dobro no Field!''\033[0;0m')
            din = din + (aposta2*3)
                
        else:
            if aposta2>0:
                print('\033[32m''Parabéns! Você ganhou o triplo do que apostou no Field!!''\033[0;0m')
                din = din + (aposta2*4)

        result_Any = Anycraps (soma_dos_dados)     
        if result_Any == 'craps1' and aposta3>0:
            print('\033[32m''Parabéns! Você ganhou sete vezes o que apostou no Any Craps!''\033[0;0m')
            din = din + (aposta3*8)
            
        else:
            if aposta3>0:
                print('\033[31m''Você perdeu no Any Craps.''\033[0;0m')

        result_Twelve = Twelve (soma_dos_dados)
        if result_Twelve == 'twelve1' and aposta4>0:
            print('\033[32m''Parabéns! Você ganhou doze vezes o que apostou no Twelve.''\033[0;0m')
            din = din + (aposta4*31)
                
        else:
            if aposta4>0:
                print('\033[31m''Você perdeu no Twelve.''\033[0;0m\n')
        
        if fase == 'Come out':
            break

        if fase == 'Point':
            print('\033[1;34m''Você está na fase {}.''\033[0;0m'.format(fase))
            print('\033[0;34m''Seu número point é {}.''\033[0;0m'.format(point))

    if din != 0:        
        print('\n\033[34m''Após a rodada você ainda tem {} fichas.''\033[0;0m'.format(din))

print ('O jogo acabou com {} ficha(s).\n'.format(din))
