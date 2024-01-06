import read_csv
import list_creator

data = read_csv.read('video_games_sales.csv')

rank_list_string = list_creator.get_list(data, 'Rank')
rank_list_int = list(map(lambda rank: int(rank), rank_list_string))

def enumeracion_exhaustiva(list):
    ban = 0
    for num in list:
        while ban**2 < num:
            ban += 1
        if ban**2 == num:
            print(f'La raiz cuadrada de {num} es {ban}')
        else:
            print(f'{num} no tiene raiz cuadrada exacta')
            
enumeracion_exhaustiva(rank_list_int)