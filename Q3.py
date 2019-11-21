#Questão 3

def main():

	retangulos=[]

	for cont in range(2):

		BLx= float(input("Entre com a coordenada X do BottomLeft: "))
		BLy= float(input("Entre com a coordenada Y do BottomLeft: "))
		TRx= float(input("Entre com a coordenada X do TopRight: "))
		TRy= float(input("Entre com a coordenada Y do TopRight: "))

		retangulo={"bottomLeft": (Blx, BLy),
				   "topRight": (TRx,TRy)
		}

		retangulos.append(retangulo.copy())

		size_x1= retangulos[0]["topRight"](0)-retangulos[0]["bottomLeft"](0)

		size_x2= retangulos[1]["topRight"](0)-retangulos[1]["bottomLeft"](0)

		BLx1= retangulos[0]["bottomLeft"](0)
		BLx2= retangulos[1]["bottomLeft"](0)
		TRx1= retangulos[0]["topRight"](0)
		TRx2= retangulos[1]["topRight"](0)

		if ((BLx1>BLx2 & (BLx1-BLx2)> size_x2) or (BLx2>BLx1 & (BLx2-BLx1)> size_x1)):

			colision= False

		else:
			colision= True

		if colision:

			print("Colisão detectada")

		else:

			print("Colisão não detectada")

#O erro dessa questão está no algoritmo: eu não contemplei todos os casos da colisão ser falsa, 
#então vão ter casos em que há colisão mas o programa não vai detectar