#!/usr/bin/env python
# coding: utf-8

# ## 1st Contact Section Assignment
# ### Question 1

# In[2]:


# To scrape books from  http://books.toscrape.com
# (Book name, price, stock status (in stock or out of stock), 
# rating, description, product information, caategory(poetry, fiction,
# historical fiction, etc))
# Scrape the first 5 pages (20 books per page)


# In[3]:


import mechanicalsoup as ms
# Making an instance of mechanical soup funcitonalities
browser = ms.StatefulBrowser()


# In[4]:


# Navigating to the page to be extracted
browser.open("http://books.toscrape.com")


# In[5]:


browser.page


# In[ ]:





# In[64]:


# To scrape 10-20 distinct quote authors from http://quotes.toscrape.com
# (Name, nationality, description, date of birth)

browser_quotes = ms.StatefulBrowser()


# In[ ]:


def scraper(n, no_of_pages)


# In[75]:


browser_quotes.open("http://quotes.toscrape.com")


# In[76]:


browser_quotes.page


# In[77]:


a=browser_quotes.page.find_all('span',)


# # Question 2

# In[ ]:


# To scrape 10-20 distinct quote authors from http://quotes.toscrape.com
# (Name, nationality, description, date of birth)
# This is an automated scraper with two fuctions


# In[145]:


# functions to get all links
def get_links(url, n):
    """ Return list of links to authors' details. """

    links_list = []
    browser_quotes.open(url)
    #--------This is to view content  <browser_quotes.page>  --- This is to view the content
    
    get_spans = browser_quotes.page.find_all('span')
    for span in get_spans: 
        link = span.find('a', class_='')
        
        if link: # check if there is a link in the span to continue
            weblink="http://quotes.toscrape.com" + link.get('href')
            links_list.append(weblink)
    return links_list[:n]


# In[82]:


print(get_links())


# In[146]:


def get_authors_details(no_of_pages, no_of_quotes=-1):
    """Retun the dictionary containing author details."""
    

    #key_list = ('name', 'date_of_birth', 'location', 'description')
    #author_details = dict.fromkeys(key_list, [])
    
    
    author_details = {}                    # A dictionary that will contain all the extracted data
    author_details['name'] = []            # list of  authors' name in the webPages
    author_details['date_of_birth'] = []   # list of authors' date of birth
    author_details['location'] = []        # list of authors' address
    author_details['description'] = []     # list of authors' description
    
    
    # Making a variable of the root url
    root_url = "http://quotes.toscrape.com/"
    
    # looping through the number of pages desired
    for num in range(no_of_pages):
        print(num)
        browser_quotes = ms.StatefulBrowser()
        if  no_of_pages == 1:
            url="http://quotes.toscrape.com/"
        if (no_of_pages) > 1:
            page_num=num +1
            url = f"{root_url}/page/{page_num}"

        
        ##print(get_links(url, no_of_quotes))
        
        # Looping through the links to get the details of each authors
        for link in get_links(url, no_of_quotes):
            browser_quote = ms.StatefulBrowser()
            browser_quote.open(link)
            name = browser_quote.page.find('h3', class_="author-title").text.strip()
            
            #  To get data structure with distinct author
            if name not in author_details['name']: 
                date_of_birth = browser_quote.page.find('span', class_="author-born-date").text
                location = browser_quote.page.find('span', class_="author-born-location").text.replace("in",'')
                description = browser_quote.page.find('div', class_="author-description").text.strip()
                author_details['name'].append(name)
                author_details['date_of_birth'].append(date_of_birth)
                author_details['location'].append(location)
                author_details['description'].append(description[:6])
            else:
                continue
    
    return author_details
    
    


# In[133]:


# to present our data in tables
import pandas as pd
pd.DataFrame(get_authors_details(7))


# In[51]:


browser_quote.page


# In[61]:



name = browser_quote.page.find('h3', class_="author-title").text.strip()
date_of_birth = browser_quote.page.find('span', class_="author-born-date").text
location = browser_quote.page.find('span', class_="author-born-location").text.replace("in",'')
description = browser_quote.page.find('div', class_="author-description").text.strip()


# In[62]:


print(name, date_of_birth, location, description)


# In[ ]:




