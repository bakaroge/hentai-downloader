# Project Title

Hentai Downloader

These scripts are used to download hentai from nhentai.com
It downloads all the manga found in a search bar in nhentai using the pre-defined tags and puts it in a folder called hentai


## Getting Started

The required library is requests and BeautifulSoup.
BeautifulSoup4 was used and it can be installed via pip

## How To Use

open terminal
call python nhentai.py num num tags tags

the first num is the start page, second num is the end page
the tags are the tags of the manga (e.g. yaoi, yuri, loli, english, japanese, korean, chinese) #read the rules of tags in nhentai
if you don't want to see a certain tags, use - sign before tag such as -yaoi -yuri -english
tags can be character name, series name, or also artist's name


an example of the script is

python nhentai.py 1 10 english misaka mikoto -yuri -rape touma 

the result of the script will be like

Name of hentai
Name of hentai - page.jpg
...

Next name of hentai

##API

Downloadfile.py needs two input : Name and Identifier
Identifier is the manga identifier found in the image file in the website https://i.nhentai.net/galleries/
If only one manga wants to be downloaded, this will make download the manga and the name is up to you

