import read_csv
import list_creator
import functools
import math

data = read_csv.read('video_games_sales.csv')

#Cree un lista de puro los ranks del csv 
rank_list_strings = list_creator.get_list(data, 'Rank')
rank_list_ints = list(map(lambda rank: int(rank), rank_list_strings))

#Segundo la acorte la mitad dejando solo los pares
pair_numbers = list(filter(lambda pair_rank: pair_rank%2==0,rank_list_ints))

#Tercero le quite la mitad a la nueva lista dejando los mayores al promedio de la nombrada lista
sum_pair_numbers = functools.reduce(lambda counter, item: counter + item, pair_numbers)
prom = sum_pair_numbers/len(pair_numbers)
biggest_pair_numbers = list(filter(lambda number: number > prom, pair_numbers))

#Cuarto la acorte mas aun, dejando solo los que tienen raices cuadradas exactas
square_root_list = list(filter(lambda square: math.sqrt(square)%2 ==0, biggest_pair_numbers))


#Busqueda binaria
def busqueda_binaria(list):
    epsilon = 0.00001
    
    for num in list:
        bajo = 0.0
        alto = max(1.0, num)
        respuesta = (alto + bajo)/2
        
        while abs(respuesta**2 - num) >= epsilon:
            print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
            if respuesta**2 < num:
                bajo = respuesta
            else:
                alto = respuesta
            
            respuesta = (alto + bajo)/2
        
        print(f'La raiz cuadrada de {num} es {respuesta}')
    
busqueda_binaria(square_root_list)