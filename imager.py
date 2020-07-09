bn = ''' ██▓ ███▄ ▄███▓ ▄▄▄        ▄████ ▓█████  ██▀███  
▓██▒▓██▒▀█▀ ██▒▒████▄     ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██    ▓██░▒██  ▀█▄  ▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
░██░▒██    ▒██ ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
░██░▒██▒   ░██▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░  ░      ░  ▒   ▒▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
 ▒ ░░      ░     ░   ▒   ░ ░   ░    ░     ░░   ░ 
 ░         ░         ░  ░      ░    ░  ░   ░     

Version: 1.0
Developer: Muhammad Hanan Asghar
Mail: muhammadhananasghar@gmail.com
                                                 '''

############################# Imager By Muhammad Hanan #####################

#################Imports
import requests
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent
import random
import os
cwd = os.getcwd()
import urllib.request



############Main Fuction#######################
def SearcherEcosia(query):
    ua = UserAgent()
    if " " in query:
        list_query = [i for i in query]
        for i in range(len(list_query)):
            if " " == list_query[i]:
                list_query[i] = "%20"
        query = "".join(list_query)
    ancors = []
    for i in range(1,3):
        soup = BeautifulSoup(requests.get(f"https://www.ecosia.org/images?q={query}&p={i}",headers={"User-Agent":f"{ua.random}"}).content,"html.parser")
        anchors = soup.find_all("a",class_="image-result")
        ancors.append(anchors)
    imgs = [j.attrs.get('href') for i in ancors for j in i]
    return imgs

print(bn)
user_input = input("Enter Search Query : ")
dir_name = input("Enter Directory Name(default: Imager) : ")
print("Wait Please While We Fetch Data.....(Approx 5s)")
data_return = SearcherEcosia(user_input)
lst = ""
lst = dir_name
if lst == "":
	dir_name = "Imager"
else:
	dir_name = lst
path = os.path.join(cwd, dir_name)
os.mkdir(path)
path = os.path.join(cwd, dir_name)
a = 1
for i in data_return:
	#rand = random.randint(999,99999)
	try:
		url_n = i.split("/")
		print(f"Download Image - {a} : "+url_n[-1])
		urllib.request.urlretrieve(f"{i}", f"{path}"+"/"+f"{url_n[-1]}"+".jpg")
	except:
		continue
	a = a + 1
print("Directory '% s' created" % path) 
