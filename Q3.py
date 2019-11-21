#Questão 3

def main():

	retangulos=[]

	for cont in range(2):

		BLx= float(input("Entre com a coordenada X do BottomLeft: "))
		BLy= float(input("Entre com a coordenada Y do BottomLeft: "))
		TRx= float(input("Entre com a coordenada X do TopRight: "))
		TRy= float(input("Entre com a coordenada Y do TopRight: "))

		retangulo={"bottomLeft": (BLx, BLy),
				   "topRight": (TRx,TRy)
		}

		retangulos.append(retangulo.copy())

	BLx1= retangulos[0]["bottomLeft"][0]
	BLx2= retangulos[1]["bottomLeft"][0]
	TRx1= retangulos[0]["topRight"][0]
	TRx2= retangulos[1]["topRight"][0]
	BLy1= retangulos[0]["bottomLeft"][1]
	BLy2= retangulos[1]["bottomLeft"][1]
	TRy1= retangulos[0]["topRight"][1]
	TRy2= retangulos[1]["topRight"][1]

	if ((TRx2>BLx1) & (TRy2>BLy1) & (TRx1>BLx2) & (TRy1>BLy2)):

		colision= True

	else:
		colision= False

	if colision:

		print("Colisão detectada")

	else:

		print("Colisão não detectada")

#Chamada da main
main()

