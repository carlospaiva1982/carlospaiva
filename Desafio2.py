import os
menu="""
##########################
   [s]- SACAR     
   [d]- DEPOSITAR 
   [e]- VISUALIZAR EXTRATO
   [u]- CRIAR USUÁRIO
   [c]- CONTAS
   [q]- SAIR
##########################
   """
saldo=0
LIMITE=500

list_extrato=[]
LISTA_VAZIA=[]
numero_saques=0
LIMITE_SAQUES=3
numero_conta=0
val=0
usuarios={}
AGENCIA="0001"
conta={}
numero_usuario=0
movimentos={}

def sacar(*,saldo,valor,list_extrato,LIMITE,numero_saques,LIMITE_SAQUES):
    
    print("Entre com o cliente a sacar o dinheiro ")
    cpf=input()
    if procurar_usuario(cpf)==True:
        listagem_conta_de_um_cliente(cpf)
        print("Ecolha uma das contas do cliente")
        conta_numero=input()
        if procurar_conta(conta_numero,cpf)==True:
            if saldo>= valor:
                if valor>=0:
                    if numero_saques<=LIMITE_SAQUES:
                       if valor<=LIMITE:
                          saldo -= valor                
                          numero_saques+=1
                          movimentos[conta_numero]=[conta_numero,valor,saldo]
                          list_extrato.append(str(valor))
                          return saldo, list_extrato
                 
                       else:
                            print("O limite máximo de tirada é R$ 500")
                    
                    else:
                          print("Tens permissão so para 3 retiradas")
                else:
                      print("Valores negativos não são permitidos")
            else:
                 print("Não será possível sacar o dinheiro por falta de saldo")
        else:
             os.system("cls")
             print("Conta não existe")
             print("entre com o valor a sacar")
             saida=input()    
             sacar(saldo=saldo,valor=int(saida),list_extrato=list_extrato,LIMITE=LIMITE,numero_saques=numero_saques,LIMITE_SAQUES=LIMITE_SAQUES)       
          
    else:
         os.system("cls")
         print("cliente não existe")
         print("entre com o valor a sacar")
         saida=input()
         sacar(saldo=saldo,valor=int(saida),list_extrato=list_extrato,LIMITE=LIMITE,numero_saques=numero_saques,LIMITE_SAQUES=LIMITE_SAQUES)       
          
    
def depositar(saldo,valor,list_extrato):
    print("Entre com o cliente a Depositar o dinheiro ")
    cpf=input()
    if procurar_usuario(cpf)==True:
        listagem_conta_de_um_cliente(cpf)
        print("Ecolha uma das contas do cliente")
        conta_numero=input()    
        if procurar_conta(numero_conta,cpf)==True:
            if int(valor)<=int(0):
                print("Entra com um valor posistivo")
            else:
                
                saldo += int(valor)
                list_extrato.append(str(valor))
                movimentos[conta_numero]=[conta_numero,valor,saldo]
                print(list_extrato)
                return saldo, list_extrato
        else:
             os.system("cls")
             print("conta não existe")
             depositar(saldo,valor,list_extrato)    
    else:
         os.system("cls")
         print("cliente não existe")
         depositar(saldo,valor,list_extrato)   
            
def extrato(saldo,/,*,list_extrato):
        print("Exebindo extrato")
        if list_extrato==LISTA_VAZIA:
            print("Não foram realizadas movimentações")
        else:
            print("\n################ EXTRATO ###################")
            for item in list_extrato:
                if int(item)>int(0):
                              iterar=float(item)
                              print(f"Movimentos de entrada no valor de R$ {iterar:.2f}")
                else:
                      iterar=float(item)
                      print(f"Movimentos de saida no valor de R$ {iterar:.2f}")

            print("O Saldo Atual: "+str(saldo))
            print("##############################################")
def criar_conta(agencia,numero_conta,cpf):
     
     if usuarios.get(cpf)!=None:    
         numero_conta+=1     
         conta[numero_conta]=[agencia,numero_conta,cpf]
     else:
          print("o usuario não existe")

def listagem_conta():
     lusuario=list(usuarios.items())
     lconta=list(conta.items())    
     i=len(lusuario)
     j=len(lconta)
     for numero in range(i):
        for numero1 in range(j):
                if lusuario[numero][1][2]==lconta[numero1][1][2]:
                    print("Cliente ",lusuario[numero][1][0]," Data nasc ",lusuario[numero][1][1],
                          " Cpf ",lusuario[numero][1][2], " Endereço",lusuario[numero][1][3]," Conta Numero ",str(lconta[numero1][1][1])," Agencia ",str(lconta[numero1][1][0]))
    
    
def listagem_conta_de_um_cliente(cpf):
     for chave in conta:
          print(chave, conta[chave])
     

def procurar_usuario(cpf):
       if  usuarios.get(cpf)==None:
            return False
       else:
            return True
       
def procurar_conta(numeroconta, cpf):
       if conta.get(numeroconta)==None and usuarios.get(cpf)==None:
           
              
               return False
       
       else:
                 return True


     

def adicionar_usuario(nome, data_nasc, cpf, endereco):     
     if usuarios.get(cpf)==None:
         usuarios[cpf]=[nome,data_nasc,cpf,endereco]
     else:
          print("Existe Usuário com mesmo Cpf")
          return

def lista_usuarios():
     i=len(usuarios)
     lusuario=list(usuarios.items())
     print("\n################### Lista de Cliente ####################")
     for numero in range(i):
         print("Cliente ",lusuario[numero][1][0]," Data nasc ",lusuario[numero][1][1]," Cpf ",lusuario[numero][1][2],
                " Endereço ",lusuario[numero][1][3])

def menus():
     while True:
        opcao=input(menu)
        global saldo, list_extrato
   
        if opcao=="d":
           os.system("cls")
           print("entre com o valor a depositar")
           entrada=input()
           saldo, list_extrato =depositar(saldo,entrada,list_extrato)        
           continue
        elif opcao=="s":
            os.system("cls")
            print("entre com o valor a sacar")
            saida=input()       
            saldo,list_extrato=sacar(saldo=saldo,valor=int(saida),list_extrato=list_extrato,LIMITE=LIMITE,numero_saques=numero_saques,LIMITE_SAQUES=LIMITE_SAQUES)       
          
            continue
        elif opcao=="e":
            os.system("cls")
            extrato(saldo,list_extrato=list_extrato)
            continue

        elif opcao=="u":
          os.system("cls")
          
          usual="""
          ###############################
          # c - REGISTAR USUÁRIO
          # l - LISTAR USUÁRIO
          # v - VOLTAR AO MENU   
              """
         
          while True:
               discar=input( usual)
               os.system("cls")
               if(discar=="c"):
                   print("Nome: ")
                   nome=input()
                   print("Data Nascimento:", "formato dd-mm-aaaa")
                   data_nasc=input()
                   print("Cpf:" ,"carateres em Numeros")
                   cpf=input()
                   print("Endereço:" , "com o formato logradouro, nro - bairro - cidade/sigla do estado")
                   endereco=input()    
                   adicionar_usuario(nome, data_nasc, cpf, endereco) 
                   

               elif(discar=="l"):
                   os.system("cls")
                   lista_usuarios()

               elif(discar=="v"):
                   os.system("cls")
                   menus()
                  

          continue
        elif opcao=="c":
          os.system("cls")
          usual="""
          ###############################
          # c - REGISTAR CONTA
          # l - LISTAR CONTA
          # v - VOLTAR AO MENU   
              """
         
          while True:
                
                discar=input( usual)
                os.system("cls")
                if discar=="c":
                    os.system("cls")
                     
                    print("Criar conta")
                    lista_usuarios()
                    print("inseri o numero de cpf do usuario para o registo da conta")
                    cpf=input()
                    criar_conta(AGENCIA,numero_conta,cpf)
                elif discar=="l":
                     os.system("cls")
                     listagem_conta()

                elif discar=="v":
                     os.system("cls")
                     menus()



          continue
        elif opcao=="q":
            print("Saindo")
        break
     else:
         print("opção inválida, entre com uma nova opção")
     
menus()   
