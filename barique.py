#!/usr/bin/env python


from nba_api.stats.endpoints import TeamYearByYearStats
import pandas as pd
import matplotlib.pyplot as plt


# Golden State Warriors data
data = TeamYearByYearStats(team_id=1610612744)
tfdas = data.team_stats.get_data_frame()
df = tfdas

# only want Golden State era
df.drop(df[(df['TEAM_CITY'] == "Philadelphia")].index, inplace=True)
df.drop(df[(df['TEAM_CITY'] == "San Francisco")].index, inplace=True)


print(df)
# pandas data frames (optional: pip install pandas)
# df = career.get_data_frames()[0]


# df['PLAYER_AGE'] = df['PLAYER_AGE'].astype(int)



# df.plot.scatter(y='TOV', x='PLAYER_AGE', figsize = (16,8))

# plt.show()


