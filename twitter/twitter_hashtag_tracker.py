# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:34:12 2022

@author: Kratika
"""


#              Project : Twitter Hashtag Tracker

#         ----Decription----
#     * helps in tracking the hashtags used in twitter
#     * works in real time
#     * displays data on analytics dashboard
#     * uses social network data scrapping
#     * to be deployed on heroku (a salesforce cloud service)


#           *----IMPORTANT TERMS----*
#
#       retweets  : tweet.retweetedTweet                    (percentage bar)
#       replies   : tweet.inReplyToTweetId                  (percentage bar)
#       source    :  tweet.sourceLabel                      (Bar chart)
#       twitter joining year :  tweet.user.created          (bar chart/linec hart/ histogram)
#       language used :  tweet.lang                         
#       verified account :  tweet.user.verified             (Pie chart)
#       total tweets : number of rows in dataset            (main display/percentage bar)
#       users who tweeted : tweet.user.username            
#       total contributors : df['users'].value_counts()      (main display)
#       for language chart : df['language'].value_counts()   (bar chart)
#
#
#
#   note: in order to check which parameters are useful reffer to the above terms....
#         These are meant for reffernce
# """



import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime, timedelta
import time



def twitter_analytics(hashtag_in):
    todays_datetime = datetime.now()
    nxt_datetime = todays_datetime + timedelta(1)

    since = todays_datetime.strftime('%Y-%m-%d') 
    until = nxt_datetime.strftime('%Y-%m-%d')

    q = "({}) until:{} since:{}"
    hashtag = hashtag_in
    query = q.format(hashtag,until,since)
    ans=[]

    tend= time.time() + 30
    
    try:
        
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            # print(vars(tweet))
            # break  
            if time.time()>tend:
                break
            ans.append((tweet.user.username,tweet.user.created,tweet.user.verified,tweet.sourceLabel,tweet.lang,tweet.retweetCount,tweet.replyCount,tweet.date))
            
            tweets_df = pd.DataFrame(ans,columns=['User','Date acc. created','Verified','Source of Tweet','Language','RetweetsCount','RepliesCount','Tweet timing'])
    
    
        year=[]
        for i in tweets_df['Date acc. created']:
            d=str(i).split('-')
            year.append(d[0])
        tweets_df['Date acc. created']=year

        hrs=[]
        for i in tweets_df['Tweet timing']:
            t=i.strftime("%H:%M")
            hrs.append(t)
        tweets_df['Tweet timing']=hrs

        tweets,retweets,replies,contributors=0,0,0,0

        contributors = tweets_df['User'].unique().size
        tweets = len(tweets_df['User'])
        if tweets!=0:
            rt=tweets - tweets_df['RetweetsCount'].value_counts()[0]
            rp=tweets - tweets_df['RepliesCount'].value_counts()[0]
            retweets = ((tweets - tweets_df['RetweetsCount'].value_counts()[0])*100/tweets).round(2)
            replies = ((tweets - tweets_df['RepliesCount'].value_counts()[0])*100/tweets).round(2)

    # print("number of tweets: {} and Number of contributors: {}".format(tweets,contributors))
    # print("Retweets: {}%".format(retweets))
    # print("Replies: {}%".format(replies))
    # print("==============================={}===============================".format(hashtag))
    # print(tweets_df)

        tweets_df=tweets_df.sort_values('Tweet timing', ascending=True)


    #    -----------time tracker----------
        x_time=tweets_df['Tweet timing']
        y_time=[]
        for i in tweets_df['Tweet timing']:
            y_time.append(tweets_df['Tweet timing'].value_counts()[i])
    
    
 

        tweets_df=tweets_df.sort_values('Date acc. created', ascending=True)


    #     --------age distribution---------
        x_age=tweets_df['Date acc. created']
        y_age=[]
        for i in tweets_df['Date acc. created']:
            y_age.append(tweets_df['Date acc. created'].value_counts()[i])
    
    



    #   --------Language---------
        x_lang=tweets_df['Language'].value_counts().index
        y_lang=tweets_df['Language'].value_counts()
  


    #    ---------Source label--------

        x_src=tweets_df['Source of Tweet'].value_counts().index
        y_src=tweets_df['Source of Tweet'].value_counts()
   
    
    

    #   -----verified-------
        xv=tweets_df['Verified'].value_counts()
        yv=tweets_df['Verified'].value_counts().index
   

    #   -----tweets count distribution-----
        if tweets!=0:
            tweetsp=100
        else:
            tweetsp=0
        y_ratio=[replies,retweets,tweetsp]
        x_ratio=['replies','retweets','tweets']
    

        return (tweets,contributors,rt,rp,x_age,y_age,x_ratio,y_ratio,x_lang,y_lang,x_src,y_src,x_time,y_time,xv,yv)
  

    except :
        return (0,0,0,0,[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0])

    


