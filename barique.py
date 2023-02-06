#!/bin/env python

from nba_api.stats.endpoints import playercareerstats
import pandas as pd
import matplotlib.pyplot as plt


# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
df = career.get_data_frames()[0]

print(list(df.columns.values))

df['PLAYER_AGE'] = df['PLAYER_AGE'].astype(int)



df.plot.scatter(y='TOV', x='PLAYER_AGE', figsize = (16,8))

plt.show()
