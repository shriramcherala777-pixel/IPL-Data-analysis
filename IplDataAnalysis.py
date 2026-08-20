import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

#top wicket taker
wickets=deliveries[
    (deliveries["dismissal_kind"].notna())
    &(deliveries["dismissal_kind"]!="run out")
]

top_wicket_taker= wickets["bowler"].value_counts().head(1)
print("--------------------")
print("top wicket taker is",top_wicket_taker)

#most matches won by a team
most_matches_won= matches["winner"].value_counts().head(1)
print("--------------------")
print("most matches won by",most_matches_won)

#best strike rates,wides should be excluded
wides=deliveries[deliveries["extras_type"]!="wides"]

stats= wides.groupby("batter").agg({
    "batsman_runs" :"sum",
    "ball":"count"

})

stats["strike_rate"]= (( stats["batsman_runs"]/stats["ball"]))*100

top_str=stats[stats["ball"]>500].sort_values(by="strike_rate" , ascending=False).head(5)

print("------------------------")
print("top strike rates are ",top_str)

#this is to know whether winning toss impact winning match
toss_impact= matches[matches["toss_winner"]== matches["winner"]]
percentage=(len(toss_impact)/len(matches["id"]))*100
print("----------------------")
print("toss impact",percentage)

#most runs scored in death overs by batters
death_overs= deliveries[deliveries["over"]>=16]
most_runs_in_deathovers= death_overs.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(3)

print("--------------------------")
