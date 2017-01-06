import requests
from bs4 import BeautifulSoup
import Downloadfile
import sys

begin=sys.argv[1]   #first argument = first page
end=sys.argv[2]     #second argument = second page
begin=int(begin)
end=int(end)

for x in range(begin,end):
    link="https://nhentai.net/search/?q="
    link=link+sys.argv[3]
    for y in range(4,len(sys.argv)):
        link=link+'+'
        link=link+sys.argv[y]
    link=link+("&page=%r")%x


    files = requests.get(link)
    soup = BeautifulSoup(files.text, 'html.parser')

    for link in soup.find_all('a'):
        temp=link.get('href')
        if("/g/" in temp): #check if /g/ is in the string temp
            temp2="https://nhentai.net/"+temp+'/1/'
            files2=requests.get(temp2)



            soup = BeautifulSoup(files2.text, 'html.parser')


            temp= soup.title
            temp2=soup.find(id="image-container")

            temp=str(temp)
            title = temp[7:-56]
            temp3=str(temp2)
            number=temp3.find("galleries/") #find manga identifier
            number2=temp3.find('g" width') #find manga identifier

            identifier=temp3[number+10:number2-5] #find manga identifier

            print
            print title
            print
            Downloadfile.download(title, int(identifier))


#How to use
# in terminal python nhentai.py #starting page #ending page #tags (at least 1)
# python nhentai.py 1 10 english -rape -yaoi
# this will download all manga with these tags from found in page 1 to 10 and put in in folder called hentai
# multiple instances of this script can be used at the same time
