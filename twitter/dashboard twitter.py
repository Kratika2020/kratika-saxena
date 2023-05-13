# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:28:53 2022

@author: Kratika
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
from twitter_hashtag_tracker import twitter_analytics

app = dash.Dash(__name__)


app.title = 'Twitter Hashtag Tracker'


fig_age= dict(
            data=[go.Bar(x=[0,0,0], y=[0,0,0])],
            
            layout=dict(title="Twitter User Age Distribution" ,
                     xaxis=dict(title='Years'),
                     yaxis=dict(title='Number of Users'),
                         ))
fig_ratio= dict(
            data=[go.Bar(x=[0,0,0], y=[0,0,0])],
            
            layout=dict(title="" ,
                     xaxis=dict(title=''),
                     yaxis=dict(title=''),
                         ))
fig_lang =  dict(
            data=[go.Bar(x=[0,0,0], y=[0,0,0])],
            
            layout=dict(title="Language Distribution" ,
                     xaxis=dict(title='Languages'),
                     yaxis=dict(title='Number of Tweets'),
                         ))
fig_src= dict(
            data=[go.Bar(x=[0,0,0], y=[0,0,0])],
            
            layout=dict(title="Source Distribution" ,
                     xaxis=dict(title='Source Labels'),
                     yaxis=dict(title='Number of Users'),
                         ))
fig_time= dict(
            data=[go.Scatter(x=[0,0,0], y=[0,0,0])],
            
            layout=dict(title="Timeline" ,
                     xaxis=dict(title=''),
                     yaxis=dict(title='Number of Tweets'),
                         ))
fig_v= dict(
            data=[go.Pie(values=[0,0,0])],
            
            layout=dict(title="Verified Users Distribution" 
                         ))




app.layout = html.Div([
                        html.Div([html.P([html.B('Twitter Hashtag Tracker'),html.Br(),
                                        html.P('Our real-time hashtag tracker converts raw data into useful, accurate and insightful metrics and predictive twitter Hashtag analytics.',
                                               style={'fontSize': '22px'})]),
                        dcc.Input(id='hashtag',type='text',placeholder="enter a hashtag with #",debounce=True,
                                  style={'width': '400px',
                                         'height' : '20px',
                                         'border' : 'none',
                                         'borderRadius' : '20px',
                                         'backgroundColor' : 'rgba(255,255,255,0.8)',
                                         'fontSize' : '22px',
                                         'padding' : '10px 10px 10px 20px'})],

   #header
                                 style= 
                                 {
                                     'backgroundColor' : 'rgba(29,161,242,1)',
                                     'background-image' : 'url("/assets/bgimg6.jpg")',
                                     'background-repeat':'no-repeat',
                                     'background-size': 'cover',
                                     'width' : '100%',
                                     'color' : 'rgb(255,255,255)',
                                     'fontSize': '58px',
                                     'height': '500px',
                                     'textAlign' : 'center',
                                     'paddingTop' : '250px',
                                     'paddingLeft' : '30px',
                                     'marginTop' : '-120px',
                                                        
                                     
                                 }),
                        html.Div([html.Div(html.P([html.P(html.B("0"),id='tweets',style={'fontSize' : '56px'}),html.P("Tweets")],
                                                  style={'textAlign' :'center',
                                                         'width':'100%',
                                                         'height' : '100%',
                                                         'padding' : '30px 10px 10px 10px'}),
   #Row1 Column1
                                style=
                                {
                                    'backgroundColor' : 'rgba(28,78,128,1)',
                                    'width' : '250px',
                                    'height' : '250px',
                                    'textAlign' : 'center',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'padding' : '10px 10px 10px 10px',
                                    'marginLeft' : '10px',
                                    'marginRight':'10px',
                                    'fontSize': '36px',
                                    'color' : 'rgb(255,255,255)',
                                    'borderRadius' : '20px',
                                                            
                                                                    
                                }),
                             html.Div(html.P([html.P(html.B("0"),id='users',style={'fontSize' : '56px'}),html.P("Users")],
                                                  style={'textAlign' :'center',
                                                         'width':'100%',
                                                         'height' : '100%',
                                                         'padding' : '30px 10px 10px 10px'}),
    #Row1 Column2
                                style=
                                {
                                    'backgroundColor' : 'rgba(28,78,128,1)',
                                    'width' : '250px',
                                    'height' : '250px',
                                    'textAlign' : 'center',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'padding' : '10px 10px 10px 10px',
                                    'marginLeft' : '10px',
                                    'marginRight':'10px',
                                    'fontSize': '36px',
                                    'color' : 'rgb(255,255,255)',
                                    'borderRadius' : '20px',
                                                            
                                                                    
                                }),
                             
                             html.Div(html.P([html.P(html.B("0"),id='rt',style={'fontSize' : '56px'}),html.P("Retweets")],
                                                  style={'textAlign' :'center',
                                                         'width':'100%',
                                                         'height' : '100%',
                                                         'padding' : '30px 10px 10px 10px'}),
    #Row1 Column3
                                style=
                                {
                                    'backgroundColor' : 'rgba(28,78,128,1)',
                                    'width' : '250px',
                                    'height' : '250px',
                                    'textAlign' : 'center',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'padding' : '10px 10px 10px 10px',
                                    'marginLeft' : '10px',
                                    'marginRight':'10px',
                                    'fontSize': '36px',
                                    'color' : 'rgb(255,255,255)',
                                    'borderRadius' : '20px',
                                                            
                                                                    
                                }),
                             
                             html.Div(html.P([html.P(html.B("0"),id='rp',style={'fontSize' : '56px'}),html.P("Replies")],
                                                  style={'textAlign' :'center',
                                                         'width':'100%',
                                                         'height' : '100%',
                                                         'padding' : '30px 10px 10px 10px'}),
    #Row1 Column4
                                style=
                                {
                                    'backgroundColor' : 'rgba(28,78,128,1)',
                                    'width' : '250px',
                                    'height' : '250px',
                                    'textAlign' : 'center',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'padding' : '10px 10px 10px 10px',
                                    'marginLeft' : '10px',
                                    'marginRight':'10px',
                                    'fontSize': '36px',
                                    'color' : 'rgb(255,255,255)',
                                    'borderRadius' : '20px',
                                                            
                                                                    
                                }),
                                
                                 
                         ],
                                 style=
                                {
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'paddingTop' : '50px',
                                    'paddingLeft' : '30px',
                                    'paddingRight' : '30px',
                                    'textAlign' : 'center',
                                    'marginRight' : '120px',
                                    'marginLeft' : '120px'
                                                            
                                                                    
                                }),
                        html.Div([html.Div(   
                            
                            dcc.Graph(id='age_chart',
                                      figure=fig_time,
                            style=
                            {
                                'width' : '100%',
                                'height' : '100%'
                                    
                            }),                     
    #Row2 Column1
                                style=
                                {
                                    
                                    'width' : '75%',
                                    'height' : '400px',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'padding' : '5px 5px 5px 5px',
                                    'marginLeft' : '10px',
                                    'marginRight':'10px',
                                    
                                    
                                                            
                                                                    
                                }),
                             html.Div(     
                                 
                            dcc.Graph(id='tweet_ratio',
                                 figure=fig_ratio,
                            style=
                            {
                                'width' : '100%',
                                'height' : '100%'
                                    
                            }),                         
    #Row2 Column2
                                style=
                                {
                                    
                                    'width' : '25%',
                                    'height' : '400px',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'padding' : '5px 5px 5px 5px',
                                    'marginLeft' : '10px',
                                    'marginRight':'10px',
                                                            
                                                                    
                                }),
                             
                                 
                         ],
                                 style=
                                {
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'paddingTop' : '50px',
                                    'paddingLeft' : '30px',
                                    'paddingRight' : '30px',
                                                            
                                                                    
                                }),
                        
                        
                        html.Div([html.Div(    
                            
                            dcc.Graph(id='lang',
                                 figure=fig_lang,
                            style=
                            {
                                'width' : '100%',
                                'height' : '100%'
                                    
                            }),                    
   #Row3 Column1
                                style=
                                {
                                    
                                    'width' : '50%',
                                    'height' : '450px',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'padding' : '5px 5px 5px 5px',
                                    'marginLeft' : '10px',
                                    'marginRight':'10px',
                                                            
                                                                    
                                }),
                             html.Div(     
                                 
                            dcc.Graph(id='source',
                                 figure=fig_src,
                            style=
                            {
                                'width' : '100%',
                                'height' : '100%'
                                    
                            }),                          
   #Row3 Column2
                                style=
                                {
                                    
                                    'width' : '50%',
                                    'height' : '450px',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'padding' : '5px 5px 5px 5px',
                                    'marginLeft' : '10px',
                                    'marginRight':'10px',
                                                            
                                                                    
                                }),
                             
                                 
                         ],
                                 style=
                                {
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'paddingTop' : '50px',
                                    'paddingLeft' : '30px',
                                    'paddingRight' : '30px',
                                                            
                                                                    
                                }),
                         html.Div([html.Div(     
                             
                            dcc.Graph(id='timeline',
                                 figure=fig_age,
                            style=
                            {
                                'width' : '100%',
                                'height' : '100%'
                                    
                            }),                   
    #Row4 Column1
                                style=
                                {
                                    
                                    'width' : '75%',
                                    'height' : '400px',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'padding' : '5px 5px 5px 5px',
                                    'marginLeft' : '10px',
                                    'marginRight':'10px',
                                                            
                                                                    
                                }),
                             html.Div(   
                                 
                            dcc.Graph(id='verified',
                                 figure=fig_v,
                            style=
                            {
                                'width' : '100%',
                                'height' : '100%'
                                    
                            }),                         
    #Row4 Column2
                                style=
                                {
                                    
                                    'width' : '25%',
                                    'height' : '400px',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'padding' : '5px 5px 5px 5px',
                                    'marginLeft' : '10px',
                                    'marginRight':'10px',
                                                            
                                                                    
                                }),
                             
                                 
                         ],
                                 style=
                                {
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'paddingTop' : '50px',
                                    'paddingLeft' : '30px',
                                    'paddingRight' : '30px',
                                                            
                                                                    
                                }),
                         html.Div([html.P([html.B('Twitter Hashtag Tracker'),
                                           html.Br(),
                                           html.P('Our real-time hashtag tracker converts raw data into useful, accurate and insightful metrics and predictive twitter Hashtag analytics.',
                                               style={'fontSize': '16px',
                                                      'color' :'rgb(0,0,0)'}),
                                       
                                           html.P('Connect Us:',
                                                  style={'fontSize' : '16px',
                                                         'color' :'rgb(0,0,0)'}),
                                           html.P(['LinkedIn : ',html.A('Kratika Saxena',href='https://www.linkedin.com/in/kratika-saxena-996616229/',target='_blank',
                                                                        style={'color':'rgb(0,0,0)',
                                                                               'fontSize':'18px'})],
                                                  style={'fontSize' : '20px'}),
                                           
                                        ])
                                   ],
                                  style=
                                  {
                                     'padding': '120px 30px 10px 30px',
                                     'width' : '101%',
                                     'height' : '200px', 
                                     'backgroundColor' : 'rgba(241,241,241,0.8)',
                                     'textAlign' : 'center',
                                     'fontSize': '25px'   , 
                                     'color' : 'rgba(28,78,128,1)',
                                      
                                  })
                         
                        ],
                            style=
                            {
                                'backgroundColor' : 'rgba(241,241,241,0.8)',
                                
                                'marginTop' : '-10px',
                                'marginLeft' : '-10px',
                                'marginRight':'0px',
                                'overflowX': 'hidden',
                                'padding': '0px 0px 0px 0px',
                                'width' : '101%',
                                'height' : '100%',
                                
                                })

@app.callback(Output('tweets','children'),
              Output('users','children'),
              Output('rt','children'),
              Output('rp','children'),
              Output('age_chart', 'figure'),
              Output('tweet_ratio', 'figure'),
              Output('lang', 'figure'),
              Output('source', 'figure'),
              Output('timeline', 'figure'),
              Output('verified', 'figure'),
              Input('hashtag','value'))
def callback_in1(hashtag_val):
    if hashtag_val is not None:
        ans= twitter_analytics(hashtag_val)
    else:
        ans= (0,0,0,0,[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0])
    
    fig_age= dict(
        data=[go.Bar(x=ans[4], y=ans[5])],
        
        layout=dict(title="Twitter User Age Distribution" ,
                 xaxis=dict(title='Years'),
                 yaxis=dict(title='Number of Users'),
                     ))
    fig_ratio= dict(
        data=[go.Bar(x=ans[6], y=ans[7])],
        
        layout=dict(title="" ,
                 xaxis=dict(title=''),
                 yaxis=dict(title='percentage'),
                     ))
    fig_lang =  dict(
        data=[go.Bar(x=ans[8], y=ans[9])],
        
        layout=dict(title="Language Distribution" ,
                  xaxis=dict(title='Languages'),
                  yaxis=dict(title='Number of Tweets'),
                      ))
    fig_src= dict(
        data=[go.Bar(x=ans[10], y=ans[11])],
        
        layout=dict(title="Source Distribution" ,
                  xaxis=dict(title=''),
                  yaxis=dict(title='Number of Users'),
                      ))
    fig_time= dict(
        data=[go.Scatter(x=ans[12], y=ans[13],fill='tozeroy')],
        
        layout=dict(title="Timeline" ,
                  xaxis=dict(title=''),
                  yaxis=dict(title='Number of Tweets'),
                      ))
    fig_v= dict(
        data=[go.Pie(labels=ans[15], values=ans[14])],
        
        layout=dict(title="Verified Users Distribution" 
                 
                      ))
    return ans[0],ans[1],ans[2],ans[3],fig_time,fig_ratio,fig_lang,fig_src,fig_age,fig_v
   



if __name__== '__main__':
    app.run_server(debug=True)
    
    