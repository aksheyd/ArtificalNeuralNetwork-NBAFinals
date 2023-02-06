#!/bin/env python

from nba_api.stats.endpoints import playercareerstats
import pandas

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
print(career.get_data_frames()[0].head())

# json
print(career.get_json().type())

# dictionary
career.get_dict()

