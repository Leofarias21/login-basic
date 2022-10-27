produto= ["texto", "texto", "texto"]

texto='ahagu'
def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    print(texto)
    return texto
texto = tratar_texto(texto)
for i in enumerate(produto):
    produto[i]= tratar_texto(texto)
    