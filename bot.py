import requests
from bs4 import BeautifulSoup 
from googlesearch import search
import clipboard

# Using Keyboard module in Python 
import keyboard
import re


SHORTCUT_KEYS = 'ctrl + shift + a'
HEADERS = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}


def get_visible_text(text):

	output = ''
	blacklist = [
	    '[document]',
	   'noscript',
	    'header',
	    'html',
	    'meta',
	    'head', 
	    'input',
	    'script',
	    'style',
	]

	for t in text:
	    if t.parent.name not in blacklist:
	        output += '{} '.format(t)


	return output


def go(a,b):
	question = clipboard.paste().strip()
	print("Question: \n%s"%question)
	print("Searching..")
	res = search(question,tld='com',lang='en',num=3,stop=3,pause=3.0)
	links = []
	for link in res:
		links.append(link)
		print("\nSearching Link : %s\n"%link)
		r = requests.get(link,headers=HEADERS)
		soup = BeautifulSoup(r.content, 'html5lib')
		text = soup.find_all(text=True)

		visible_text = get_visible_text(text)

		# print(visible_text)

		x = re.search(question,visible_text)

		if x:
			start,end = x.span()
			print(visible_text[start:end+50].strip())
		else:
			print("Not found.")

		print()

	print("~~~Search DONE.~~~\n")




def start():
	keyboard.add_hotkey(SHORTCUT_KEYS, go, args = ('you entered', 'hotkey'))

	keyboard.wait('esc')


if __name__ == "__main__":
	start()