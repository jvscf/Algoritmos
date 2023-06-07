data = input("Digite a data no formato dd/mm/aaaa: ")
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]
nova_data = ano + mes + dia
print(nova_data)