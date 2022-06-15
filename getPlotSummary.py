# movieTitle = input("Enter the movie title: ")

movieTitle = "Madagascar 3"

##pull up the wikiedia page for the movie
import requests
import json
from bs4 import BeautifulSoup
from gtts import gTTS
import os
from pydub import AudioSegment

search = movieTitle.replace(' ', '+') + '+wikipedia+plot+summary'
soup = BeautifulSoup(requests.get('https://www.google.com/search?q=' + search).text, 'html.parser')

##find the first link that contains the string "wikipedia.org"
for link in soup.find_all('a'):
    if 'wikipedia.org' in link.get('href'):
        wikiLink = link.get('href')
        break

##end wikilink string at &
wikiLink = wikiLink[:wikiLink.find('&')]

##start wikilink at https://
wikiLink = wikiLink[wikiLink.find('https://'):]


wiki_soup = BeautifulSoup(requests.get(wikiLink).text, 'html.parser')



##find a span with the id "Plot"
for span in wiki_soup.find_all('span'):
    if span.get('id') == 'Plot':
        plotHeader = span.parent
        plot = ""
        for child in plotHeader.find_all_next():
            if child.name == 'p':
                plot = plot + child.text
            if child.name == 'h2':
                break

        break
##replace new lines with spaces
plot = plot.replace('\n', '... ')
mytext = plot




language = 'en'
myobj = gTTS(text=mytext, lang=language, tld='co.uk')


##create folder for movie in the Movies folder
os.makedirs('Movies/' + movieTitle, exist_ok=True)

##save plot summary as txt file in the new directory
with open('Movies/' + movieTitle + '/plotSummary.txt', 'w') as outfile:
    outfile.write(mytext)

##save plot summary as mp3 file
myobj.save('Movies/' + movieTitle + '/plotSummary.mp3')







# os.mkdir(movieTitle.replace(" ", "_").replace("(", "").replace(")",""))

# ##save plot summary as txt file in the new directory
# with open(movieTitle.replace(" ", "_").replace("(", "").replace(")","") + "/" + movieTitle.replace(" ", "_").replace("(", "").replace(")","") + "_plot.txt", 'w') as outfile:
#     outfile.write(plot)


# ##save plot summary as mp3 file
# myobj.save(movieTitle.replace(" ", "_").replace("(", "").replace(")","") + "/" + movieTitle.replace(" ", "_").replace("(", "").replace(")","") + "_plot.mp3")





