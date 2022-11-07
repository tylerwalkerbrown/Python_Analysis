```python
import os
from credentials import *
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd 
import numpy as np 
import re 
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
```


```python
os.chdir("Desktop/mojo")
```


```python
#reading in the csv file that contains our keys to access twitter
config = pd.read_csv("api.csv")
```


```python
twitterApiKey = config['API Key']
twitterApisecret = config['API key secret']
twitterBearer = config['Bearer']
twittherAcctoken = config['Access Token Secret']
twitterAccessScret = config['Access token']
```


```python
#Getting proper authentication using the keys above
auth = tweepy.OAuthHandler(apikey,apikeysecret)
auth.set_access_token(accesstoken,Accesstokensecret)
twitterApi = tweepy.API(auth,wait_on_rate_limit = True)
```


```python
#Choosing the account you would like to look at 
account = "FoxNews"
```


```python
#Extracting the tweets using the Cursor function 
tweets = tweepy.Cursor(twitterApi.user_timeline,
                      screen_name = account,
                      count = None,
                      max_id = None,trim_user = True, exclude_replies = True
                       , contribubtori_details = False, include_entities = False).items(500);
```


```python
#creating a dataframe for the tweets extracted in the tweepy.Cursor
df = pd.DataFrame(data = [tweet.text for tweet in tweets], columns = ["Tweet"])
```

   


```python
#Cleaning up the tweets with urls, ReTweets and hashtags
def cleanUpTweet(txt):
    txt = re.sub(r'@[A-Za-z0-9_]+', '', txt)
    txt = re.sub(r'#', '', txt)
    txt = re.sub(r'RT : ', '', txt)
    txt = re.sub(r'https?:\/\/[A-Za-z0-9\.\/]+', '', txt)
    return txt
```


```python
#Applying the function created to clean the tweets
df['Tweet'] = df['Tweet'].apply(cleanUpTweet)
```


```python
#Creating two different functions to capture Subjectivity and POlarity in the tweets
def getTextSubjectivity(txt):
    return TextBlob(txt).sentiment.subjectivity

def getTextPolarity(txt):
    return TextBlob(txt).sentiment.polarity
```


```python
#Applying the functions created to the dataset with new columns
df['Subjectivity'] = df['Tweet'].apply(getTextSubjectivity)
df['Polarity'] = df['Tweet'].apply(getTextPolarity)

```


```python
#Based on the polarity score we will create a function to assign it to a category 
def getTextAnalysis(a): 
    if a < 0:
        return "Negative"
    elif a == 0:
        return "Neutral"
    else: 
        return "Positive"
```


```python
#Applying the function to the dataset
df["Score"] = df["Polarity"].apply(getTextAnalysis)
```


```python
positive = df[df["Score"]=='Positive']
print(str(len(positive)/len(df))[2:4],"% of  Fox's tweets are postive.")
pos = (len(positive)/len(df))*100
```

    26 % of CNNs tweets are postive.



```python
negative = df[df["Score"]=='Negative']
print(str(len(negative)/len(df))[2:4],"% of  Fox's  tweets are negative.")
neg = (len(negative)/len(df)) * 100
```

    29 % of CNNs tweets are negative.



```python
neutral = df[df["Score"]=='Neutral']
print(str(len(neutral)/len(df))[2:4],"% of Fox's tweets are negative.")
neut = (len(neutral)/len(df))* 100
```

    45 % of CNNs tweets are negative.


Here we are creating differint inputs for the charts that will be created. Explode is used to create a clearer distinction by popping out one of the slices in a pie chart. 


```python
explode = (0,0.1,0)
labels = 'Positive', 'Negative', 'Neutral'
sizes = [pos,neg,neut]
colors = ['green','red','yellow']
```


```python
#plot a pie chart showing the break down of the different categories
plt.pie(sizes, explode = explode, colors = colors,autopct='%.2f' )
plt.legend(labels, loc = (-0.05,0.05))
plt.title('Fox News Sentiment Pie Chart')
plt.axis('equal')
```




    (-1.1989296651282861,
     1.1047109364346803,
     -1.128884626373277,
     1.158193158217936)




    
![png](output_20_1.png)
    



```python
#Bar plot of the number of tweets rather than percentages
values = df.groupby('Score').size().values
labels = df.groupby('Score').count().index.values
plt.bar(labels,values)
```




    <BarContainer object of 3 artists>




    
![png](output_21_1.png)
    



```python
#Creating a sentiment analysis scatter plot showing the x = polarity and y = subjectivity
for index, row in df.iterrows():
    if row['Score'] == 'Positive':
        plt.scatter(row['Polarity'], row['Subjectivity'], color = 'Green')
    elif row['Score'] == 'Negative':
        plt.scatter(row['Polarity'], row['Subjectivity'], color = 'Red')
    elif row['Score'] == 'Neutral':
        plt.scatter(row['Polarity'], row['Subjectivity'], color = 'Yellow')
        
plt.title('Fox Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
```




    Text(0, 0.5, 'Subjectivity')




    
![png](output_22_1.png)
    



```python

```
