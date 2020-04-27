#!/usr/bin/env python
# coding: utf-8

# ### Description 

# #### I'll create a movie picker that will crawl the imdb Top charts website and will randomly select a movie for you. Showing the movie title,name of the actor, Genre 

# #### Function that sends requests

# In[44]:


import random
import pandas as pd 
import numpy as np 
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"



def main():
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    #soup = BeautifulSoup(response.text, 'lxml') # faster

    # print(soup.prettify())

    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1] # last item 
        return year

    years = [get_year(tag) for tag in movietags]
    actors_list =[tag['title'] for tag in inner_movietags] # access attribute 'title'
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in ratingtags] # access attribute 'data-value'
    
    elements = ['Titles','Actors','Year_produced','Ratings']
    
    movies_grouped = pd.DataFrame(list(zip(titles,actors_list,years,ratings)),columns=elements)
    movies_table = pd.DataFrame(movies_grouped)
    
    #movies_table.to_csv('movies_table.csv')      -- Remove ash to print and save the Movies table on a csv file 
    print(movies_table)

if __name__ == '__main__':
    main()


# In[ ]:




