raio = float(input("informe o raio:"))
altura = float(input("informe a altura:"))
area=2*3.14*raio*(altura+raio)
print ("area: ", area)
litros= area/3.0
latas = litros /5.0
print ("latas necessarias: ", latas)
custo = latas*50
print ("custo total:", custo)
