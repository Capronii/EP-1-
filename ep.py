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
print('\n\033[1;34m''Bem Vindo ao Craps''\033[0;0m')
print('Você tem {} fichas para apostar'.format(din))
regra=input('\033[1;90mVocê deseja saber as regras?(sim/nao)   \033[1;90m')
if regra=='sim':
    print('''\033[1;90m
      Pode-se escolher entre 4 tipos de aposta:
      1-Pass line bet:
      A primeira fase dessa opção de aposta consiste em 
      se a soma dos dados for igual a 7 ou 11 o jogador ganha o que apostou.
      se for 2, 3 ou 12 o jogador perde o que apostou.
      Caso a soma dos dados der 4, 5, 6, 8, 9 ou 10 o jogador muda para a fase Point,
      o dado é jogado novamente e sua soma tem que ser igual a soma inicial ou 7 caso contrario o dado é jogado novamente
      caso seja 7 você perde o que apostou e se for igual a primeira soma de dados você vence
      Durante essa fase do jogo enquando os dado são jogados novamente você pode apostas nos outros tipos de aposta.
      2-Field: 
      Esse tipo de aposta consiste em se o dado cair no 5, 6, 7 ou 8 o jogador perde a aposta.
      se cair no 3, 4, 9, 10 ou 11 o jogador vence 
      caso a soma seja 2 o jogador vence dobrando a aposta inicial e caso seja 12 o jogador vence triplicando a aposta inicial
      3-Any Craps:
      nesse tipo de aposta apenas as somas iguais a 2, 3 ou 12 te fazem vencer multiplicando a aposta 7 vezez!!
      caso contrário a aposta é perdida
      4-Twelve:
      Nesta opção a unica soma que te leva a vencer é 12 e multiplica a aposta inicial em 30 vezes.\033[1;90m''')



while din > 0:
    fase = 'Come out'
    print('\033[1;34m''Você está na fase {}''\033[0;0m'.format(fase))

    sair = input('\n\033[34m''Você quer sair do jogo?(sim/nao): ''\033[0;0m')
    if sair == 'sim':
        print('Obrigado por jogar você terminou com {0}'.format(din))
        break

    

    while True:
        aposta1 = int(input('\n\033[34m'"Quanto você quer apostar no Pass Line Bet? "'\033[0;0m'))
        if (aposta1 <= din):
            din -= aposta1
            break
        else:
            print('\033[31m''Erro: o valor da aposta no Pass Line Bet é maior do que a quantidade das suas fichas. Aposte outro valor.''\033[0;0m')

    while True:
        while True:
            print('Você ainda tem {} ficha(s) para apostar'.format(din))
            aposta2 = int(input('\n\033[34m'"Quanto você quer apostar no Field? "'\033[0;0m'))
            if (aposta2 <= din):
                din -= aposta2
                break
            else:
                print('\033[31m''Erro: o valor da aposta no Field é maior do que a quantidade das suas fichas. Aposte outro valor.''\033[0;0m')

        while True:
            print('Você ainda tem {} ficha(s) para apostar'.format(din))
            aposta3 = int(input('\n\033[34m'"Quanto você quer apostar no Any Craps? "'\033[0;0m'))
            if (aposta3 <= din):
                din -= aposta3
                break
            else:
                print('\n\033[31m''Erro: o valor da aposta no Any Craps é maior do que a quantidade das suas fichas. Aposte outro valor.''\033[0;0m')

        while True:
            print('Você ainda tem {} ficha(s) para apostar'.format(din))
            aposta4 = int(input('\n\033[34m'"Quanto você quer apostar no Twelve? "'\033[0;0m'))
            if (aposta4 <= din):
                din -= aposta4
                break
            else:
                print('\n\033[31m''Erro: o valor da aposta no Twelve é maior do que a quantidade das suas fichas. Aposte outro valor.''\033[0;0m')
        
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)

        print('\nDado 1:',dado1)
        print('Dado 2:',dado2)

        soma_dos_dados = dado1 + dado2
        print('Soma dos dados:',soma_dos_dados)

        if fase == 'Come out':
            resultado_Pass = Pass_line_Come_out (soma_dos_dados)
            point = soma_dos_dados
            if resultado_Pass == 'Vitória direta' and aposta1>0:
                print('\n\033[32m''Parabéns! Você ganhou no Pass Line Bet na fase Come Out''\033[0;0m')
                din = din + 2*aposta1
            elif resultado_Pass == 'Perda direta' and aposta1>0:
                print('\n\033[31m''Você perdeu no Pass Line Bet na fase Come Out''\033[0;0m')
            else:
                if aposta1 > 0:
                    fase = 'Point'
                    print('\n\033[1;34m''Você mudou para a fase {}''\033[1;0m'.format(fase))
                    print('\n\033[1;34m''Seu número point é {}''\033[1;0m'.format(point))
        else:
            resultado_Pass_line_Point = Pass_line_Point(soma_dos_dados, point)
            if resultado_Pass_line_Point == 'Ganhou point' and aposta1>0:
                print('\n\033[32m''Parabéns! Você ganhou no Pass Line Bet na fase Point''\033[0;0m')
                din = din + 2*aposta1
                fase = 'Come out'
            elif resultado_Pass_line_Point == 'Perdeu point' and aposta1>0:
                print('\n\033[31m''Você perdeu no Pass Line Bet na fase Point''\033[0;0m')
                fase = 'Come out'

        result_Field = Field (soma_dos_dados)
        if result_Field == 'perde' and aposta2>0:
            print('\n\033[31m''Você perdeu no Field''\033[0;0m')
            
        elif result_Field == 'Vito' and aposta2>0:
            print('\n\033[32m''Parabéns! Você ganhou no Field''\033[0;0m')
            din = din + 2*aposta2
                
        elif result_Field == 'dois' and aposta2>0:
            print('\n\033[32m''Você ganhou em dobro no Field''\033[0;0m')
            din = din + (aposta2*3)
                
        else:
            if aposta2>0:
                print('\n\033[32m''Você ganhou o triplo no Field!!''\033[0;0m')
                din = din + (aposta2*4)

        result_Any = Anycraps (soma_dos_dados)     
        if result_Any == 'craps1' and aposta3>0:
            print('\n\033[32m''Você ganhou no Any Craps''\033[0;0m')
            din = din + (aposta3*8)
            
        else:
            if aposta3>0:
                print('\n\033[31m''Você perdeu no Any Craps''\033[0;0m')

        result_Twelve = Twelve (soma_dos_dados)
        if result_Twelve == 'twelve1' and aposta4>0:
            print('\n\033[32m''Você ganhou no Twelve''\033[0;0m')
            din = din + (aposta4*31)
                
        else:
            if aposta4>0:
                print('\n\033[31m''Você perdeu no Twelve''\033[0;0m\n')
        
        if fase == 'Come out':
            break
