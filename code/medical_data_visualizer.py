import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
bmi = (df['weight'] / ((df['height'] / 100) ** 2))
df['overweight'] = (bmi > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], value_name='value')

    # 6
    # Show count
    df_cat_grouped = df_cat.groupby(['cardio', 'value', 'variable']).size().reset_index(name='total')

    # 7
    catplot = sns.catplot(data=df_cat_grouped, 
    x='variable', 
    y='total', 
    kind='bar', 
    hue='value', 
    col='cardio')

    # 8
    fig = catplot.figure


    # 9
    fig.savefig('catplot.png')
    return fig
draw_cat_plot()

# 10
def draw_heat_map():
    # 11
    #Cleaning the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, 
                mask=mask, 
                vmax=0.30, 
                annot=True, 
                center=0, 
                annot_kws={'size': 6},
                square=False, 
                linewidths=0.5, 
                cbar_kws={"shrink": 0.7}, 
                fmt='.1f', 
                ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig
draw_heat_map()
