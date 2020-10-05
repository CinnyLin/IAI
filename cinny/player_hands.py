# import library
import pandas as pd

# import data
DF = pd.read_csv('cinny/total_number_of_hands.csv')

# list of attributes
people = ['Eddie', 'Gogo', 'MrPink', 'MrWhite', 'MrBlue', 'Joe', 'ORen', 'MrBlonde',
          'Hattori', 'MrOrange', 'MrBrown', 'Pluribus', 'Bill', 'Budd']

# extract data
data_hand = []
# loop people
for player in people:
    # extract df
    DF_player_game = DF[(DF['player'] == player) & (DF['total_hands'] != 0)]
    # get variables
    summary = DF_player_game.describe()
    average_hands_per_game = round(summary['total_hands']['mean'], 2)
    median_hands_per_game = summary['total_hands']['50%']
    min_hands_per_game = summary['total_hands']['min']
    max_hands_per_game = summary['total_hands']['max']
    # create df
    entry = []
    entry.append([player,
                  average_hands_per_game, median_hands_per_game,
                  min_hands_per_game, max_hands_per_game])
    data_hand.extend(entry)

# exoprt data
df_hand = pd.DataFrame(data_hand, columns=[
                       'player', 'average', 'median', 'min', 'max'])
df_hand.to_csv('cinny/player_hands.csv')
