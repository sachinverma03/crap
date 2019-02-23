import urllib.request
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs): 
		
		if(tag == 'a'):
			print("Start tag:", tag)
			for attr in attrs:
				if attr[0]=='href':
					c.append(attr)
				print("     attr:", attr)
c=list()
print(c)
parser = MyHTMLParser()
contents = urllib.request.urlopen("http://example.webscraping.com/").read()
parser.feed(str(contents))
print(contents)
print(c)