import random 

def Pass_line(aposta1,dado):
    if dado ==7 or dado==11:
        return 'a'
    if dado==2 or dado==3 or dado==12:
        return 'b'

    if dado==4 or dado==5 or dado==6 or dado==8 or dado==9 or dado==10:
        dado3=random.randint(1,6)
        dado4=random.randint(1,6)
        dado2=dado3+dado4
        print('Você mudou de fase')
        while dado2!=7 or dado2!=dado:
            dado3=random.randint(1,6)
            print('Dado1:',dado3)
            dado4=random.randint(1,6)
            print('Dado2:',dado4)
            dado2=dado3+dado4
            print('Soma:',dado2)
            if dado2==7:
                return 'c'
                break
            if dado2==dado:
                return 'd'
                break

def Field(aposta2,dado):
    if dado==5 or dado==6 or dado==7 or dado==8:
        return 'perde'
    if dado==3 or dado==4 or dado==9 or dado==10 or dado==12:
        return 'Vito'
    if dado==2:
        return 'dois'
    if dado==12:
        return 'doze'

def Anycraps(aposta3,dado):
    if dado==2 or dado==3 or dado==12:
        return 'craps1'
    else:
        return 'craps2'

def Twelve(aposta4,dado):
    if dado==12:
        return 'twelve1'
    else:
        return 'twelve2'
    
def aposta_valida1(aposta1,din,):
    if aposta1>=din and aposta1==0:
        return False
    else:
        return True
        
def aposta_valida2(aposta2,din):
    if aposta2>=din and aposta2==0:
        return False
    else:
        return True

def aposta_valida3(aposta3,din):
    if aposta3>=din and aposta3==0:
        return False
    else:
        return True 

def aposta_valida4(aposta4,din):
    if aposta4>=din and aposta4==0:
        return False
    else:
        return True



#inicio
din=100
print('bem vindo ao Craps')
'''Criar print com as regras depois'''
while din>0:

    '''continuar=input('Você que continuar a jogar?')'''

    
    aposta1=int(input("Quanto quer apostar no Pass Line Bet?  "))
    aposta2=int(input('Quanto quer apostar no Field?  '))
    aposta3=int(input('Quanto quer apostar no Anycraps?  '))
    aposta4=int(input('Quanto quer apostar no Twelve?  '))


    

    if aposta_valida1(aposta1,din)==False or aposta_valida2(aposta2,din)==False or aposta_valida3(aposta3,din)==False or aposta_valida4(aposta4,din)==False:
        print('erro aposta maior que saldo')
        break
        
    else:
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        print('Dado 1:',dado1)
        print('Dado 2:',dado2)
        dado=int(dado1)+int(dado2)
        print('Soma dos dados:',dado)
        resultado=Pass_line(aposta1,dado)
        result_Field=Field(aposta2,dado)
        result_Any=Anycraps(aposta3,dado)
        result_Twelve=Twelve(aposta4,dado)

        if resultado=='a':
            print('Vitória Direta!')
            din=din+2*aposta1
            
        if resultado=='b':
            print('CRAPS,Perdeu')
            din=din-aposta1
            
        if resultado=='c':
            print('Perdeu no Point')
            din=din-aposta1
            
        if resultado=='d':
            print('Vitória no Point')
            din=din+2*aposta1
            
        if result_Field=='perde':
            print('Perdeu no Field')
            din=din-aposta2
        
        if result_Field=='Vito':
            print('Ganhou no Field')
            din=din+aposta2
            
        if result_Field=='dois':
            print('Ganhou em dobro no Field')
            din=din+(aposta2*2)
            
            
        if result_Field=='doze':
            print('Ganhou o triplo no Field!!')
            din=din+(aposta2*3)
            
        if result_Any=='craps1':
            print('Ganhou no any craps')
            din=din+(aposta3*7)
        
        if result_Any=='craps2':
            print('Perdeu no any craps')
            din=din-aposta3
            
        if result_Twelve=='twelve1':
            print('Ganhou no Twelve')
            din=din+(aposta4*30)
            
        if result_Twelve=='twelve2':
            print('Perdeu no Twelve')
            din=din-aposta4
            
    print('Apos a rodada você ainda tem {}'.format(din))
