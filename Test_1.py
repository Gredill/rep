
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as gp
import streamlit as st


# Importer le fichier csv, modif \ en / sur le chemin du fichier, identifier le séparateur, traiter les \\N en valeurs nan
df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")



corr = df.corr()

viz_correlation = sns.heatmap(corr, 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

nbr_region = round(df["cylinders"].groupby(by=df["continent"]).sum())

nbr_region_1 = df["year"].value_counts()



# Menu
st.sidebar.title("Navigation")
options = st.sidebar.radio("Menu", options=['Corrélation', "Par région", "Par année",])

# Navigation avec boutons radios
if options == 'Corrélation':
    st.write(corr)
    st.pyplot(viz_correlation.figure)
elif options == 'Par année':
    st.header("Nombre de véhicules par année")
    st.area_chart(nbr_region_1)
elif options == 'Par région':
    st.header("Nombre de véhicules par région")
    st.write(nbr_region)
    st.bar_chart(nbr_region)


