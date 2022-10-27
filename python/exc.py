from site.python.main import * 
minhaLista=[]
print("preenchendo...")
preencherInventario(minhaLista)
print("Exibindo...")
exibirInventario(minhaLista)

print("Pesquisando...")
localizaPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista, 20)

print("Exvluindo")
print(excluirPorSerial(minhaLista)) 
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)