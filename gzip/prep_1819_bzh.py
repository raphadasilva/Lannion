import os
import pandas as pd


final_df = pd.DataFrame(columns=[
                                 "annee",
                                 "TNTXM"
	                            ])
for file in os.listdir("data"):
	try:
		df = pd.read_csv(f"data\\{file}",
			             sep=";")
		df["annee"] = pd.to_datetime(df["AAAAMMJJ"].astype(str),
                                     format='%Y%m%d').dt.year
		df["mois"] = pd.to_datetime(df["AAAAMMJJ"].astype(str),
                                    format='%Y%m%d').dt.month
		df["jour"] = pd.to_datetime(df["AAAAMMJJ"].astype(str),
                                    format='%Y%m%d').dt.day
		col_temps = [
		             "jour",
		             "mois",
		             "annee"
		             ]
		dfg = df.copy()
		for col in ["jour","mois","annee"]:
			dfg = dfg[col_temps+["TNTXM"]].groupby(by=col_temps).mean().reset_index()
			col_temps.remove(col)
		final_df = pd.concat([final_df,dfg],
        	                 ignore_index=True)
	except Exception as e:
		print(f"La boucle a planté en raison d'une {e}")

final_df = final_df.groupby(by="annee").mean().reset_index()
final_df.to_csv("bzh_1855-1949.csv",
	            sep=";",
	            index=False)