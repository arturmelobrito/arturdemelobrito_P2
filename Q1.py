#Questão 1 Original- Aqui eu coloquei a main(letra E) e cada definição de função: respectivamente, são as letras A, B, C e D.

#Letra A
def data(date):

	lista_date= date.split("/")

	dict_data={ "ANO": int(lista_date[0]),
				"MES": int(lista_date[1]),
				"DIA": int(lista_date[2])
	}

	return dict_data

#Letra B
def ativo(atv):

	if (atv[-1]== "\n"):
		#Mais um erro aqui: tentei alterar uma string.
		lista_atv= list(atv)
		lista_atv.pop()
		atv=str(lista_atv)

	if (atv== "SIM"):
		return True

	else:
		return False

#Letra C
def listring(m_string):
	
	list_m_string= m_string.split(":")

	return list_m_string

#Letra D
def arq_list(arq):

	arq.seek(0,0)

	lista_arq= arq.readlines()

	return lista_arq

#Letra E
def main():

	arq= open("cadastro.txt","r")

	pacientes=[]
	lista_arq= arq_list(arq)

	for paciente in lista_arq:

		m_paciente={ "CPF": listring(paciente)[0],
					 "NOME": listring(paciente)[1],
					 "DATA_DE_NASCIMENTO": data(listring(paciente)[2]),
					 "DATA_DO_CADASTRO": data(listring(paciente)[3]),
					 "ATIVO": ativo(listring(paciente)[4])
		}
		
		pacientes.append(m_paciente)

	print(pacientes)

#Chamada da main
main()