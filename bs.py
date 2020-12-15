from bs4 import BeautifulSoup
import os
import requests
g_url = "https://novels80.com"
url = "https://novels80.com/241092-a-game-of-thrones.html"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")


ul = soup.findAll('ul',{"class": "list-chapter"})

path = os.getcwd()

chaote_number = 1
for u in ul:
    for li in u.findAll('li'):
        c_url = g_url+str(li.a['href'])
        c_r = requests.get(c_url)
        soupc = BeautifulSoup(c_r.text, "html.parser").body

        content = soupc.findAll('div',{"class": "chapter-content"})
        
        par = content[0].findAll('p')

        file = "game_of_thrones/c"+str(chaote_number)+".txt"
        with open(os.path.join(path, file), 'w') as fp:

            

            for p in par:
                fp.write(p.text)
                fp.write("\n")
                # print(p.text) 

        chaote_number += 1


