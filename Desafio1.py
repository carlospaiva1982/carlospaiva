menu="""
##########################
   [s]- SACAR     
   [d]- DEPOSITAR 
   [e]- VISUALIZAR EXTRATO
   [q]- SAIR
##########################
   """
saldo=0
limete=500
extrato=""
list_extrato=[]
LISTA_VAZIA=[]
numero_saques=0
LIMITE_SAQUES=3

def sacar(val):
    global saldo, numero_saques
    if saldo>= val:
        if val>=0:
            if numero_saques<=LIMITE_SAQUES:
               if val<=500:
                  saldo -= val
                  numero_saques+=1
                  list_extrato.append("-"+str(val))
                 
               else:
                    print("O limite máximo de tirada é R$ 500")
            else:
                  print("Tens permissão so para 3 retiradas")
        else:
              print("Valores negativos não são permitidos")
    else:
         print("Não será possível sacar o dinheiro por falta de saldo")
def depositar(val):
    global saldo
    if int(val)<=int(0):
        print("Entra com um valor posistivo")
    else:
        saldo += int(val)
        list_extrato.append(val)
       
while True:
    opcao=input(menu)
   
    if opcao=="d":
        print("entre com o valor a depositar")
        entrada=input()
        depositar(entrada)        
        continue
    elif opcao=="s":
        print("entre com o valor a sacar")
        saida=input()
        c=sacar(int(saida))       
          
        continue
    elif opcao=="e":
        print("Exebindo extrato")
        if list_extrato==LISTA_VAZIA:
            print("Não foram realizadas movimentações")
        else:
            for item in list_extrato:
                if int(item)>int(0):
                              iterar=float(item)
                              print(f"Movimentos de entrada no valor de R$ {iterar:.2f}")
                else:
                      iterar=float(item)
                      print(f"Movimentos de saida no valor de R$ {iterar:.2f}")

            print("O Saldo Atual: "+str(saldo))
        continue
    elif opcao=="q":
        print("Saindo")
    break
else:
    print("opção inválida, entre com uma nova opção")