import pandas as pd

# import data
df = pd.read_csv('cinny/df.csv')

# list of attributes
people = ['Eddie', 'Gogo', 'MrPink', 'MrWhite', 'MrBlue', 'Joe', 'ORen', 'MrBlonde',
          'Hattori', 'MrOrange', 'MrBrown', 'Pluribus', 'Bill', 'Budd']
games = [30, 106, 109, 108, 42, 40, 41, 43, 114, 112, 111, 53, 52, 110, 99, 50, 76, 100, 51,
         103, 44, 75, 77, 113, 88, 64, 94, 98, 63, 96, 95, 60, 61, 45, 118, 97, 62, 78,
         70, 73, 65, 117, 115, 89, 116, 71, 85, 86, 72, 83, 102, 104, 84, 101, 32, 33,
         34, 91, 90, 93, 31, 35, 92, 107, 105, 87, 74]

# extract data
data = []
# loop people
for player in people:
    # loop games
    for game in games:
        df_player_game = df[(df['game'] == game) & (df['player'] == player)]
        total_hands = df_player_game[df_player_game['preflop_action']
                                     != 'f'].shape[0]
        total_hands_won = df_player_game[df_player_game['outcome'] > 0].shape[0]
        #print(f'{player} total number of hands in game{game}:', df_player_game[df_player_game['preflop_action']!='f'].shape[0])
        #print(f'{player} total number of hands won in game{game}:', df_player_game[df_player_game['outcome']>0].shape[0])
        entry = []
        entry.append([player, game, total_hands, total_hands_won])
        data.extend(entry)

# export data
DF = pd.DataFrame(
    data, columns=['player', 'game', 'total_hands', 'total_hands_won'])
DF.to_csv('cinny/total_number_of_hands.csv')
