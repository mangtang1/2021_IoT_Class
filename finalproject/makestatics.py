import matplotlib.pyplot as plt
import json
import numpy as np
import pandas as pd

from const_data import *

def make_stick():
    with open(relative_path+store_path, "r") as f:
        stores_data = json.load(f)

    store_data = stores_data.get(stores_data.get("chosen_store"))

    df = pd.DataFrame(store_data['datas'])
    x = np.arange(12)
    values = np.zeros(12)
    s = 0
    best_val = 0
    worst_val = 100
    best_age = ""
    worst_age = ""
    for i in range(10, 61, 10):
        if i!=60:
            values[s] = df[ (df['age']>=i) & (df['age']<i+10) & (df['gender']=='M') ]['grade'].mean() 
            if best_val<values[s]: 
                best_val=values[s]
                best_age="%d대 남성"%i
            if worst_val>values[s]: 
                worst_val=values[s]
                worst_age="%d대 남성"%i
            s=s+1
            values[s] = df[ (df['age']>=i) & (df['age']<i+10) & (df['gender']=='F') ]['grade'].mean()
            if best_val<values[s]: 
                best_val=values[s]
                best_age="%d대 여성"%i
            if worst_val>values[s]: 
                worst_val=values[s]
                worst_age="%d대 여성"%i
            s=s+1
        else:
            values[s] = df[ (df['age']>=i) & (df['gender']=='M') ]['grade'].mean() 
            s=s+1
            values[s] = df[ (df['age']>=i) & (df['gender']=='F') ]['grade'].mean()
            s=s+1
        
    years=['10M','10F','20M','20F','30M','30F','40M','40F','50M', '50M', '60M', '60F']
    colors=['b','r','b','r','b','r','b','r','b','r','b','r']
    
    plt.clf()
    plt.bar(x, values, color=colors)
    plt.xticks(x, years)
    plt.rcParams["figure.figsize"] = (40,4)
    plt.savefig(relative_path+'static/datas/stick_figure.png', dpi=300,  facecolor='#eeeeee', edgecolor='blue')
    return best_age, worst_age

def make_circle():

    
    with open(relative_path+store_path, "r") as f:
        stores_data = json.load(f)

    store_data = stores_data.get(stores_data.get("chosen_store"))
    df = pd.DataFrame(store_data['datas'])
    x = np.arange(12)
    values = np.zeros(12)
    s = 0
    for i in range(10, 61, 10):
        if i!=60:
            values[s] = len(df[ (df['age']>=i) & (df['age']<i+10) & (df['gender']=='M') ]['grade'])
            s=s+1
            values[s] = len(df[ (df['age']>=i) & (df['age']<i+10) & (df['gender']=='F') ]['grade'])
            s=s+1
        else:
            values[s] = len(df[ (df['age']>=i) & (df['gender']=='M') ]['grade'])
            s=s+1
            values[s] = len(df[ (df['age']>=i) & (df['gender']=='F') ]['grade'])
            s=s+1

    years=['10~19/M','10~19/F','20~29/M','20~29/F','30~39/M','30~39/F','40~49/M','40~49/F','50~59/M','50~59/F','60~/M','60~/F']

    labels = ['10M','10F','20M','20F','30M','30F','40M','40F','50M', '50M', '60M', '60F']
    explode = [0, 0.10, 0, 0.15, 0, 0.10, 0, 0.10, 0, 0.10, 0.2, 0.10]
    
    plt.clf()
    plt.pie(values, labels=labels, autopct='%.1f%%', startangle=1000, counterclock=False, shadow=False, explode = explode)
    plt.title("%d people"%len(store_data['datas']))
    plt.savefig(relative_path+'static/datas/circle_figure.png', dpi=300, facecolor='#eeeeee', edgecolor='blue')