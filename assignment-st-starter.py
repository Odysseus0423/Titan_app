# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
# show the title
st.title('Titan App by Mingzhe Liu')

# read csv and show the dataframe
df=pd.DataFrame('train.csv')

# create a figure with three subplots, size should be (15, 5)
fig, ax=plt.subplots(1,3,figsize=(15,5))

# show the box plot for ticket price with different classes
Pclass1=df[df['Pclass']==1]['Fare']
Pclass2=df[df['Pclass']==2]['Fare']
Pclass3=df[df['Pclass']==3]['Fare']
ax[0].boxplot(Pclass1)
ax[1].boxplot(Pclass2)
ax[2].boxplot(Pclass3)

# you need to set the x labels and y labels
for i in range(0,3):
    ax[i].set_ylabel('Fare')
    ax[i].set_xticks([])
ax[0].set_xlabel('Pclass1')
ax[1].set_xlabel('Pclass2')
ax[2].set_xlabel('Pclass3')

# a sample diagram is shown below
plt.show()
