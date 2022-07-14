from re import A, X
import sqlite3
from stat_keeper.stat_keeper import StatKeeper
from stat_keeper.player import Player


if __name__ == "__main__":
    # We initiate a connection to setup the database
    # in case it does not exist
    init_stat_keeper = StatKeeper()
    init_stat_keeper.setup()
    # We start the workflow to read all PDFs in the PDF folder and 
    # add the info to the database in case the file was not scanned already
    stat_keeper = StatKeeper()
    stat_keeper.run()


#COMO ORDENAR LAS FILAS
# '''
#     Podemos ordenar las filas por cualquier celda.
#     Si queremos que sea de forma ascendente es el default, si queremos
#     descendente hay que escribir DESC.
# '''
conn = sqlite3.connect('stat_keeper.db')
c = conn.cursor()
c.execute("SELECT NAME, NUMBER, TEAM, TFG FROM PLAYER_STATS ORDER BY TFG DESC") #Tiros Libres / 3 puntos
#c.execute("SELECT NAME, NUMBER, TEAM, ST, ST_PER_GAME FROM PLAYER_STATS ORDER BY ST DESC")
items = c.fetchmany(10) #lista de queries

csv_rows = []
for item in items: #item es cada query de la lista de queries.
    # nombre = item[0]
    # numero = item[1]
    # equipo = item[2]
    #print(item[3]) #todos los decimales.
    #print(type(item[3]))
    tot_ft = item[3].split('/') #tiros libres
    ft = tot_ft[0] #tiros libres
    #print(tot_ft)
    #print(ft)
    #format_float = "{:.2f}".format(item[4]) 
    #print(format_float)
    num_ft = float(tot_ft[0])#numerador
    den_ft = float(tot_ft[1])#denominador
    per_ft = num_ft / den_ft #numero decimal
    #print(per_ft)
    por_fr = int(per_ft * 100) #porcentaje de tiros libres
    y = list(item)
    #y.pop(3) #tiros libres
    #y.pop(4)
    #y.append(format_float)
    y.append(por_fr) #tiros libres
    #print(y)
    csv_rows.append(y)
    #item = tuple(y)
    #print(item)
print(csv_rows)
# Python program to demonstrate
# writing to CSV

# Python code to sort the tuples using second element
# of sublist Inplace way to sort using sort()
def Sort(sub_li):

	# reverse = None (Sorts in Ascending order)
	# key is set to sort using second element of
	# sublist lambda has been used
	sub_li.sort(reverse=True, key = lambda x: x[4])
	return sub_li

# Driver Code
sub_li =[['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
#print(Sort(csv_rows))
tres_puntos = Sort(csv_rows)

import csv
	
# field names
fields = ['Nombre', 'Numero', 'Equipo', 'Anotaciones', 'Promedio']
	
# data rows of csv file
ex_rows = [ ['Nikhil', 'COE', '2', '9.0'],
		['Sanchit', 'COE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Sagar', 'SE', '1', '9.5'],
		['Prateek', 'MCE', '3', '7.8'],
		['Sahil', 'EP', '2', '9.1']]
#rows = [csv_rows]
	
# name of csv file
filename = "promediodepuntos.csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
		
	# writing the fields
	csvwriter.writerow(fields)
		
	# writing the data rows
	csvwriter.writerows(csv_rows)
