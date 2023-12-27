import read_csv
import list_creator

data = read_csv.read('video_games_sales.csv')

video_games_name = list_creator.get_list(data, 'Game Title')
video_games_year = list_creator.get_list(data, 'Year')

def dict_creator(list1, list2):
    dict = {name:year for (name, year) in zip(list1, list2)}
    return dict

games_dict = dict_creator(video_games_name, video_games_year)
print(games_dict)