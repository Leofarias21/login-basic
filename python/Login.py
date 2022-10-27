import getpass
usuario= input("Digite o usuário: ").upper()
senha=getpass.getpass("Digite a senha: ")

if usuario =="BITMED" and senha=="Fiap1222":
    print("Usuário logado")
else: 
    print("Usuário negado")