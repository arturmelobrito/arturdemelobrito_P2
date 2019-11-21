#Questão 2

#Letra A
def inversa(matriz):

	determ= matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0]

	if (determ==0):
		return None

	aux= matriz[0][0]

	matriz[0][0]= matriz[1][1]/determ
	matriz[1][1]= aux/determ
	matriz[0][1]= -matriz[0][1]/determ
	matriz[1][0]= -matriz[1][0]/determ

	return matriz

#Letra B
def main():

	#Na correção, mudei as entradas do usuário para float

	a= float(input("Digite o primeiro índice: "))
	b= float(input("Digite o segundo índice: "))
	c= float(input("Digite o terceiro índice: "))
	d= float(input("Digite o quarto índice: "))

	matriz=[[a,b],[c,d]]

	for cont1 in range(2):
		for cont2 in range(2):

			print(matriz[cont1][cont2], end="\t")

		print("\n")

	matriz= inversa(matriz)

	for cont1 in range(2):
		for cont2 in range(2):

			print(matriz[cont1][cont2], end="\t")

		print("\n") 

#Chamada da mainn
main()