# Final Project

## Outline
### Topic: Movies
Our group selected this topic because the movie industry has been severely impacted by COVID and we are interested in analyzing what makes movies successful or not to help future movie makers. We are going to look at data from the Rotten Tomatoes website to compare movies rated Fresh and Rotten in the hopes of being able to predict how a future movie will be rated.
### Dataset
The datasets used in the project are hosted on the Kaggle database. They can be downloaded at the following link: <br>
https://www.kaggle.com/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_movies.csv
### Goal
The selected topic for our model is based on the dataset pertaining movie’s tomato status given by critics. This topic was selected so that we can understand what features are important to receiving a fresh or rotten status. In our source data we have information that includes 22 columns:
<br>
- movie link <br>
- movie title <br>
- movie info <br>
- critic consensus <br>
- content rating <br>
- genres <br>
- directors <br>
- authors <br>
- actors <br>
- original release date <br>
- streaming release date <br>
- runtime <br>
- production company  <br>
- tomatometer status <br>
- tomatometer ratings <br>
- tomatometer count <br>
- audience status <br>
- audience rating <br>
- audience count <br>
- tomatometer top critic ratings <br>
- tomatometer top fresh critic ratings <br>
- tomatometer rotten critic ratings <br>
<br>
The goal of this project is to understand what features will help us determine which movies will receive a tomato status of fresh or rotten. We will use tomato status as our target for our model. We hope to construct a model that will accurately predict tomato status for future movies. <br>

## Team Members

- Briana Brown
- Devin Hughes
- Priscilla Van Dyke

### Communication Protocols
Our team plans to communicate primarily through a Slack channel for team members only and direct messages as needed. In case of an emergency, a message should be sent through Slack since we all agreed we would see that sooner than an email. 

## Tools and Techniques

### Data Cleaning and Analysis
We plan to primarily use Pandas to clean and analyze the data. For some of the columns, natural language processing will be necessary, so we intend to use NLTK.
### Database Storage
Since our data is tabular, we plan to use a PostgreSQL database. In order to integrate with the other pieces of the project we intend to use SQLAlchemy to make the connection.
### Machine Learning
Our supervised machine learning model will use scikit-learn to create the classifier and split the data into training and testing sets. We intend to start with a Random Forest algorithm since it can handle outliers, nonlinear data, and large datasets. We hope to avoid overfitting and increase overall model performance with ensemble learning.
### Dashboard
We plan to build our dashboard using Flask as well as D3.js to add interactive elements.

## Challenges
The dataset shows some challenges that might become present in our project. The dataset will require efficient preprocessing to be able to use the dataset optimally. We also face the challenge of knowing if we have enough features to accurately fit our model to be able to predict our target. This might require an additional dataset to merge with our current dataset. 
