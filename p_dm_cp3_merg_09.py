import numpy as np
import pandas as pd

# Read 'players.csv' into a DataFrame: players
players = pd.read_csv('data/nba/players.csv', index_col='Index')

# Read 'player_data.csv' into a DataFrame: player_data
player_data = pd.read_csv('data/nba/player_data.csv')

print('-- PLAYERS --'.center(100))
# Print players
print(players.head())

print('-- PLAYERS DATA --'.center(100))
# Print player_data
print(player_data.head())

# Merge players with players left on 'Player' and right on 'name': merge_by_name
merge_by_name = pd.merge(players, player_data, left_on='Player', right_on='name')

print('-- PLAYERS DATA MERGE 1 --'.center(100))
# Print player_data
print(merge_by_name.head())


# Merge players with players left on 'Player' and right on 'name' and suffixes: merge_by_name_suffix
merge_by_name_suffix = pd.merge(players, player_data, left_on='Player', right_on='name', suffixes=['_l', '_r'])

print('-- PLAYERS DATA MERGE 2 --'.center(100))
# Print player_data
print(merge_by_name_suffix.head())

# Update players columns
players.columns = ['name','height','weight','college','born','birth_city','birth_state']

# Merge players with players on 'name' and 'college' and suffixes: merge_by_name_suffix
merge_by_name_suffix = pd.merge(players, player_data, on=['name', 'college'], suffixes=['_left', '_right'])

print('-- PLAYERS DATA MERGE 3 --'.center(100))
# Print player_data
print(merge_by_name_suffix.head())
