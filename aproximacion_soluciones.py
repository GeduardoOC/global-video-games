import read_csv
import list_creator

data = read_csv.read('video_games_sales.csv')

world_score_strings = list_creator.get_list(data, 'Rest of World')
world_score_ints = list(map(lambda score: round(float(score), 3), world_score_strings))

ten_world_score = list(filter(lambda score: score>2, world_score_ints))

def aproximacion(list):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    
    for score in list:
        respuesta = 0.0
        while abs(respuesta**2 - score) >= epsilon and respuesta <= score:
            #print(abs(respuesta**2 - score), respuesta)
            respuesta += paso
            
        if abs(respuesta**2 - score) >= epsilon:
            print(f'No se encontro la raiz cuaderada de {score}')
        else:
            print(f'La raiz cuadrada de {score} es {respuesta}')
            
print(aproximacion(ten_world_score))