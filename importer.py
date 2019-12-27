import os
from bs4 import BeautifulSoup

print('This is for taking a bunch of HTML monster statblocks and turning them into the .wiki files I want.')
print('For convenience it should also give me the list of names so that I can create my monster manual page.')

# First things first, find and display the folder contents
filename_list = os.listdir('/home/spekkio/Programming/PycharmProjects/5e Statblock Importer/HTML/')
filepath_list = ['/home/spekkio/Programming/PycharmProjects/5e Statblock Importer/HTML/' + name for name in filename_list]

html_list = []
for filepath in filepath_list:
    with open(filepath) as file:
        html_list.append(file.read())

# print(html_list[29])
# I'm going to work initially with index 29, the Stone Golem

for html_doc in html_list[29:30]:
    # we're testing on this one at first
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.prettify())

# This grabs raw attributes
for cell in soup.find_all('td'):
    print(cell.text)

# This grabs MOST of the required text that is now directly legible
for match in soup.find_all('strong'):
    print(match.contents, match.next_sibling)

# We're still missing how much a slam actually does

# The very first result of this one is handy for size, alignment, and type
for cell in soup.find_all('em'):
    print(cell.text)

# However, attacks have still not been extracted.

# This is my starting point. In this file there's only one h3 tag, which is Actions.
# Should be easy enough to step around from here.
for match in soup.find_all('h3'):
    print(match.contents, match.next_sibling)

# However, note that Legendary Actions also get an h3 heading.
# At least that helps.
