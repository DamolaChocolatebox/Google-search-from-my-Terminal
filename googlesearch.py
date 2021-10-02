
#First, we install google: pip install google
#importing google search: 

from googlesearch import search

query = "Tokecosmetics"
for i in search(query, start = 0, pause = 2):
    print(i)
