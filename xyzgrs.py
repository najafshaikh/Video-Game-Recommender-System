#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

# In[2]:


from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity

from streamlit import session_state as session
import pickle

# In[3]:


df = pd.read_csv('data/vgsales2.csv')


# ### Data Cleaning

# Dropping columns with many missing values that are not valuable
df.drop(['Critic_Count', 'User_Count', 'Critic_Score', 'Global_Sales'], axis=1, inplace=True)


#Dropping rows with too many missing values
for index in df[df['User_Score'].isna()].index:
  df.drop(index, axis=0, inplace=True)

for index in df[df['Developer'].isna()].index:
  df.drop(index, axis=0, inplace=True)

for index in df[df['Rating'].isna()].index:
  df.drop(index, axis=0, inplace=True)

for index in df[df['Year_of_Release'].isna()].index:
  df.drop(index, axis=0, inplace=True)


#Year of release is better as categorical
df['Year_of_Release'] = df['Year_of_Release'].astype('str')

# In[17]:
image = Image.open('images/Game.png')


df = df.reset_index(drop=True)


df_categorical=df.select_dtypes(include=object)
df_numeric=df.select_dtypes(include=np.number)


# ### PreProcessing

# Creating dataframe of the y variable (Game names)
df_game_name = pd.DataFrame({'Game': df['Name']}).reset_index(drop=True)


# In[24]:


df.set_index('Name', inplace=True)


# In[25]:


column_object = df.dtypes[df.dtypes == 'object'].keys()


# In[26]:


one_hot_label = pd.get_dummies(df[column_object])


# In[27]:


df.drop(column_object,axis=1,inplace=True)


# In[28]:


df = pd.concat([df,one_hot_label],axis=1)


# In[29]:


column_numeric = list(df.dtypes[df.dtypes == 'float64'].keys())


# In[30]:


scaler = MinMaxScaler()


# In[31]:


scaled = scaler.fit_transform(df[column_numeric])


# In[32]:


i=0
for column in column_numeric:
    df[column] = scaled[:,i]
    i += 1


# ### Recommendation Model: Cosine Similarity

# In[34]:


# Calculate the cosine similarity of the dataframe
cosine_sim = cosine_similarity(df)

# Keep the result of the calculation dataframe
cosine_sim_df = pd.DataFrame(cosine_sim, index=df_game_name['Game'], columns=df_game_name['Game'])


def recommend(game):

    game_index = df_game_name[df_game_name['Game']==game].index[0]
    distances = cosine_sim[game_index]
    games_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]



    for i in games_list:
        print(df_game_name.iloc[i[0]].Game)


# In[38]:


recommend('Mortal Kombat: Deadly Alliance')


# In[39]:


df.to_csv('data/clean_data.csv', index= False)


games_dict = pickle.load(open('games.pkl','rb'))
games = pd.DataFrame(games_dict)

st.title('# XYZ Game Recommender')

selected_game_name = st.selectbox(
"Type or select a game from the dropdown",
 df_game_name['Game'].values
)



similarity = pickle.load(open('cosine_sim.pkl','rb'))
def recommend(game):
    game_index = games[games['Game']==game].index[0]
    distances = similarity[game_index]
    games_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_games = []
    for i in games_list:
             recommended_games.append(games.iloc[i[0]].Game)
    return recommended_games

if st.button('Show Recommendation'):
    recommendations = recommend(selected_game_name)

    for i in recommendations:
        st.write(i)

st.image(image)
