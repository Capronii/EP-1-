import random 
din=100
print('bem vindo ao Craps')
'''Criar print com as regras depois'''
aposta1=int(input("Quanto quer apostar no Pass Line Bet?  "))
aposta2=int(input('Quanto quer apostar no Field?  '))
aposta3=int(input('Quanto quer apostar no Anycraps?  '))
aposta4=int(input('Quanto quer apostar no Twelve?  '))

def Pass_line(aposta1,dado):
    aposta1=int(input("Quanto quer apostar no Pass Line Bet"))
    if dado ==7 or dado==11:
        return 'a'
    if dado==2 or dado==3 or dado==12:
        return 'b'

    if dado==4 or dado==5 or dado==6 or dado==8 or dado==9 or dado==10:
        print('Você mudou de fase')
        def segundo_giro(dado2,aposta1):
            dado3=random.randint(1,6)
            dado4=random.randint(1,6)
            dado2=dado3+dado4
            while dado2!=7 or dado2!=aposta1:
                if dado==7:
                    return 'c'
                if dado==aposta1:
                    return 'd'


def Field(aposta2,dado):
    if dado==5 or dado==6 or dado==7 or dado==8:
        print('Perdeu')
        din=din-aposta2
    if dado==3 or dado==4 or dado==9 or dado==10 or dado==12:
        print('Ganhou')
        din=din+aposta
    if dado==2:
        print('Ganhou em dobro')
        din=din+(aposta2*2)
    if dado==12:
        print('Ganhou o triplo!!')
        din=din+(aposta2*3)

def Anycraps(aposta3,dado):
    if dado==2 or dado==3 or dado==12:
        print('Ganhou')
        din=din+(aposta3*7)
    else:
        print('perdeu')
        din=din-aposta3

def Twelve(aposta4,dado):
    if dado==12:
        print('Ganhou')
        din=din+(aposta4*30)
    else:
        print('perdeu')
        din=din-aposta4
    
def aposta_valida1(din,aposta1):
    if aposta1<=din and aposta1!=0:
        return True
    else:
        return False
        

def aposta_valida2(aposta2,din):
    if aposta2<=din and aposta2!=0:
        return True
    else:
        return False

def aposta_valida3(aposta3,din):
    if aposta3<=din and aposta3!=0:
        return True
    else:
        return False

def aposta_valida4(aposta4,din):
    if aposta4<=din and aposta4!=0:
        return True
    else:
        return False


     


def jogo():
    
    while aposta_valida1(aposta1,din)==False or aposta_valida2(din,aposta2)==False or apostar_valida3(din,aposta3)==False or apostar_valida4(din,aposta4)==False:
        print('erro aposta maior que saldo')

        

    while aposta_valida1(din,aposta1)==True or aposta_valida2(din,aposta2)==True or apostar_valida3(din,aposta3)==True or apostar_valida4(din,aposta4)==True:
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        print('Dado 1:',dado1)
        print('Dado 2:'.dado2)
        dado=int(dado1)+int(dado2)
        print('Soma dos dados:',dado)

        if Pass_line(dado,aposta1)=='a':
            print('Vitória!')
            din=din+aposta1
        if Pass_line(dado,aposta1)=='b':
            print('CRAPS,Perdeu')
            din=din-aposta1
        if Pass_line(dado,aposta1)=='c':
            print('Vitória')
            din=din+aposta1
        if Pass_line(dado,aposta1)=='d':
            print('Perdeu')
        


    return jogo
    
print(jogo)
