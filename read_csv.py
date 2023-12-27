import csv

def read(path):
    with open(path, 'r') as cvsfile:
        reader = csv.reader(cvsfile, delimiter=",")
        
        header = next(reader)
        video_games_dictionary = []
        
        for row in reader:
            iterable = zip(header, row)
            game = {key: value for key, value in iterable}
            video_games_dictionary.append(game)
            
        return video_games_dictionary