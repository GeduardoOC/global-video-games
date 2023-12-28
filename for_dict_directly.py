import read_csv
import list_creator
import dictionary_list_creator

data = read_csv.read('video_games_sales.csv')

game_title = list_creator.get_list(data, 'Game Title')
north_america_sales_strings = list_creator.get_list(data, 'North America')
north_america_sales_ints = list(map(lambda sales: round(float(sales), 2), north_america_sales_strings))

dict = dictionary_list_creator.dict_creator(game_title, north_america_sales_ints)

#Directamente en el diccionario, iteramos a lo largo de las llaves
'''
for games in dict:
    print(games)
'''

#Ejecutar el for en la llamada de los keys, iteraremos a los largo de las llaves
'''
for games in dict.keys():
    print(games)
'''

#Ejecutar el for en la llamada de los values, iteraremos a los largo de los valores
'''
for games in dict.values():
    print(games)
'''

#Ejecutar el for en la llamada de los items del diccionario, nos permite iterar una tupla de las llaves y los valores

for item, value in dict.items():
    print(f'The game {item} got a {value} score in North America')