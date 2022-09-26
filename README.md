# XYZ Game Recommender System
## Introduction 
Video games are a very popular hobby enticing all groups of people. Since video games can be expensive, it is important to a person that they invest in the right choice; not wanting to regret later. 
This project aims to create a recommender system that will take a game the user likes and suggest new games to try that are similar.

## Data
The data was acquired from Kaggle. The data is a webscrape from the popular videogame newssite VGChartz. After cleaning the dataset, there were 7382 Games and 12 Features which would be used to return 5 suggestions.
### Data Dictionary
Name- The title of the game

Platform - The platform the game is played on.

Year - The year the game was released.

Genre -  The genre of the game (Action, Adventure, Simulation)

Publisher - The publisher of the game.

Developer - The developer of the game.

NA_Sales -  The total sales in North America in millions

EU_Sales - The total sales in Europe in millions

JP_Sales - The total sales in Japan in millions

Other Sales_ The total sales in other parts of the world in millions

User_score - The average score users gave the game.

Rating - What ESRB has rated the game (E, T, M).

## The Recommender
Content-based Filtering:
Recommendations based on a user’s activity

Cosine Similarity:
A metric used to determine the similarity between two things.


## The App
To allow users to use the recommender, a webapp was created using StreamLit and then later deployed to Heroku.
Below is a screenshot of the app: A game was selected from the dropdown menu and 5 suggestions were returned.
![Screenshot (89)](https://user-images.githubusercontent.com/100548755/192379889-3c7184e0-1b2c-4fa3-92a0-14dbed9a138c.png)

