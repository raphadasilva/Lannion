import mapclassify
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mco
import pandas as pd

def range_serie(s:pd.core.series.Series):
  """
     Cette fonction retourne une Série Pandas sous forme de liste triée dans l'ordre croissant.
  """
  try:
    return sorted(list(s))
  except:
    print("Quelque chose s'est mal passé")

def seuils_propres(s:pd.core.series.Series, n_seuil:int, meth_seuil:str):
  """
    Cette fonction renvoie des seuils définis par mapclassify sous forme de liste.
  """
  try:
    return list(getattr(mapclassify,meth_seuil)(s, k=n_seuil).bins)
  except:
    print("Quelque chose s'est mal passé")

def couleurs_barres(l_data:list,l_seuil:list,l_col:list):
  """
    Cette fonction met en parallèle une liste de seuils et une liste de couleurs.
    Si une donnée contenue dans une autre liste est inférieure à un des seuils, la couleur correspondante complète le tableau final renvoyé en résultat.
  """
  l_barres=[]
  for d in l_data:
    for i, s in enumerate(l_seuil):
      if d<=s:
        l_barres.append(l_col[i])
        break
  return l_barres

def super_chart(df:pd.core.frame.DataFrame, n_col:str, n_seuil:int, meth_seuil:str,l_col:list):
  """
    Cette fonction superpose une carte générée avec mapclasify avec un diagramme en barres.
    Ce dernier suit la même palette de couleurs (une liste de codes hexadécimaux rentrée en variable) et respecte les mêmes seuils.  
  """
  palette=mco.LinearSegmentedColormap.from_list(colors=l_col, name="tampon")
  fig, ((ax1), (ax2)) = plt.subplots(2,1,figsize = (15,14))
  ax1 = plt.subplot2grid((2, 1), (0, 0))
  df.plot(ax=ax1, column=n_col, scheme=meth_seuil, k=n_seuil, cmap=palette, legend=True)
  ax1.set_axis_off()
  ax2 = plt.subplot2grid((2, 1), (1, 0))
  plt.bar([i for i in range(len(range_serie(df[n_col])))], range_serie(df[n_col]), color=couleurs_barres(range_serie(df[n_col]),seuils_propres(df[n_col],n_seuil,meth_seuil),l_col))
  ax2.set_axis_off()
  plt.show();