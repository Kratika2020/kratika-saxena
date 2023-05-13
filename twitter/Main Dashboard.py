# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:16:23 2022

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
server = app.server


fig_age= dict(
            data=[go.Bar(x=[0,0,0], y=[0,0,0])],
            
            layout=go.Layout(title="Twitter User Age Distribution" ,
                     xaxis=dict(title='Years',showgrid=False),
                     yaxis=dict(title='Number of Users',showgrid=False),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)',
                     font= dict(color='rgb(255,255,255)')
                         ))
fig_ratio= dict(
            data=[go.Bar(x=[0,0,0], y=[0,0,0])],
            
            layout=go.Layout(title="" ,
                     xaxis=dict(title='',showgrid=False),
                     yaxis=dict(title='',showgrid=False),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)',
                     font= dict(color='rgb(255,255,255)')
                         ))
fig_lang =  dict(
            data=[go.Bar(x=[0,0,0], y=[0,0,0])],
            
            layout=go.Layout(title="Language Distribution" ,
                     xaxis=dict(title='Languages',showgrid=False),
                     yaxis=dict(title='Number of Tweets',showgrid=False),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)',
                     font= dict(color='rgb(255,255,255)')
                         ))
fig_src= dict(
            data=[go.Bar(x=[0,0,0], y=[0,0,0])],
            
            layout=go.Layout(title="Source Distribution" ,
                     xaxis=dict(title='',showgrid=False),
                     yaxis=dict(title='Number of Users',showgrid=False),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)'
                         ))
fig_time= dict(
            data=[go.Scatter(x=[0,0,0], y=[0,0,0])],
            
            layout=go.Layout(title="Timeline" ,
                     xaxis=dict(title='',showgrid=False),
                     yaxis=dict(title='Number of Tweets',showgrid=False),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)',
                     font= dict(color='rgb(255,255,255)')
                         ))


fig_v= dict(
            data=[go.Pie(values=[0,0,0])],
            
            layout=go.Layout(title="Verified Users Distribution" ,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font= dict(color='rgb(255,255,255)')
                         ))




app.layout = html.Div([ html.Div([
                        html.Div([html.P([html.B('Twitter Hashtag Tracker',style={'color' : '#538FF8'}),html.Br(),
                                        html.P('Our real-time hashtag tracker converts raw data into useful, accurate and insightful metrics and predictive twitter Hashtag analytics.',
                                               style={'fontSize': '22px',
                                                      'color' : '#b8b8b8'})]),
                        dcc.Input(id='hashtag',type='text',placeholder="enter a hashtag with #",debounce=True,
                                  )],
                                 
                                 className = 'header',                                 

   #header
                                
                                 ),
                        html.Div(id='sideimg')],style={'display': 'flex'}),
    
                        html.Div([html.Div(html.P([html.P(html.B("0"),id='tweets',style={'fontSize' : '56px'}),html.P("Tweets")],
                                                  style={'textAlign' :'center',
                                                         'width':'100%',
                                                         'height' : '100%',
                                                         'padding' : '30px 10px 10px 10px'}),
   #Row1 Column1
                               className = 'figures'),
                                  
                             html.Div(html.P([html.P(html.B("0"),id='users',style={'fontSize' : '56px'}),html.P("Users")],
                                                  style={'textAlign' :'center',
                                                         'width':'100%',
                                                         'height' : '100%',
                                                         'padding' : '30px 10px 10px 10px'}),
                                
                                className = 'figures'
    #Row1 Column2
                               ),
                             
                             html.Div(html.P([html.P(html.B("0"),id='rt',style={'fontSize' : '56px'}),html.P("Retweets")],
                                                  style={'textAlign' :'center',
                                                         'width':'100%',
                                                         'height' : '100%',
                                                         'padding' : '30px 10px 10px 10px'}),
    #Row1 Column3
                               className = 'figures'),
                             
                             html.Div(html.P([html.P(html.B("0"),id='rp',style={'fontSize' : '56px'}),html.P("Replies")],
                                                  style={'textAlign' :'center',
                                                         'width':'100%',
                                                         'height' : '100%',
                                                         'padding' : '30px 10px 10px 10px'}),
    #Row1 Column4
                               className = 'figures'),
                                
                                 
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
                                'height' : '100%',
                                
                                    
                            }), 
                            
                            className='graph',
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
                            
                             className='graph',
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
                            
                             className='graph',
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
                            
                             className='graph',
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
                             className='graph',
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
                             className='graph',
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
                                                      'color' :'#b8b8b8'}),
                                       
                                           html.P('Connect Us:',
                                                  style={'fontSize' : '16px',
                                                         'color' :'#b8b8b8'}),
                                           html.P(['LinkedIn : ',html.A('Kratika Saxena',href='https://www.linkedin.com/in/kratika-saxena-996616229/',target='_blank',
                                                                        style={'color':'#b8b8b8',
                                                                               'fontSize':'18px'})],
                                                  style={'fontSize' : '20px'}),
                                           
                                        ])
                                   ],
                                  style=
                                  {
                                     'padding': '120px 30px 10px 30px',
                                     'width' : '101%',
                                     'height' : '200px', 
                                     'backgroundColor' : 'rgba(241,241,241,0)',
                                     'textAlign' : 'center',
                                     'fontSize': '25px'   , 
                                     'color' : '#538FF8',
                                      
                                  })
                         
                        ],
                            )

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
        
       layout=go.Layout(title="Twitter User Age Distribution" ,
                     xaxis=dict(title='Years',showgrid=False),
                     yaxis=dict(title='Number of Users',showgrid=False),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)',
                     font= dict(color='rgb(255,255,255)')
                         ))
    fig_ratio= dict(
        data=[go.Bar(x=ans[6], y=ans[7])],
        
        layout=go.Layout(title="" ,
                     xaxis=dict(title='',showgrid=False),
                     yaxis=dict(title='',showgrid=False),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)',
                     font= dict(color='rgb(255,255,255)')
                         ))
    fig_lang =  dict(
        data=[go.Bar(x=ans[8], y=ans[9])],
        
       layout=go.Layout(title="Language Distribution" ,
                     xaxis=dict(title='Languages',showgrid=False),
                     yaxis=dict(title='Number of Tweets',showgrid=False),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)',
                     font= dict(color='rgb(255,255,255)')
                         ))
    fig_src= dict(
        data=[go.Bar(x=ans[10], y=ans[11])],
        
        layout=go.Layout(title="Source Distribution" ,
                     xaxis=dict(title='',showgrid=False),
                     yaxis=dict(title='Number of Users',showgrid=False),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)',
                     font= dict(color='rgb(255,255,255)')
                         ))
    fig_time= dict(
        data=[go.Scatter(x=ans[12], y=ans[13])],
        
        layout=go.Layout(title="Timeline" ,
                     xaxis=dict(title='',showgrid=False),
                     yaxis=dict(title='Number of Tweets',showgrid=False),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)',
                     font= dict(color='rgb(255,255,255)')
                     ))
    fig_v= dict(
        data=[go.Pie(labels=ans[15], values=ans[14])],
        
        layout=go.Layout(title="Verified Users Distribution" ,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font= dict(color='rgb(255,255,255)')
                         ))
    return ans[0],ans[1],ans[2],ans[3],fig_time,fig_ratio,fig_lang,fig_src,fig_age,fig_v
   



if __name__== '__main__':
    app.run_server(debug=True)
    
