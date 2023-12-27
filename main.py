import read_csv

def run(path):
    data = read_csv.read(path)
    print(data)
    
if __name__ == '__main__':
    run('video_games_sales.csv')