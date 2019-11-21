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

	#Aqui nos inputs eu transformei os valores em inteiro. A função que inverte a matriz recebe valores tipo float nas entradas
	#da matriz, mas na letra B não especificava qual era pra ser o tipo de valor entrado pelo usuário, então optei por ser inteiro.

	a= int(input("Digite o primeiro índice: "))
	b= int(input("Digite o segundo índice: "))
	c= int(input("Digite o terceiro índice: "))
	d= int(input("Digite o quarto índice: "))

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

#Como a questão não pedia a chamada da main, eu não cheguei a fazer, mas o programa roda direitinho com a chamada da main