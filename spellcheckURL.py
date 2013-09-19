import sys
import urllib2
from bs4 import BeautifulSoup
import string
import re
from sets import Set

regex_spaces = re.compile('[\t\n]')
regex_non_alpha = re.compile('[^a-zA-Z ]')
dict_s = None
def get_dict_s(path):
	try:
		if (dict_s):
			return dict_s
	except:
		pass
	s = Set()
	f = open(path, 'r')
	words = f.read().split(',')
	f.close()
	for word in words:
		s.add(word)
	dict_s = s
	return s

def try_with_error(fn, message, **kwargs):
	try:
		return fn(**kwargs)
	except:
		print (message)
		return False

def check_args(args):
	if (len(args) < 3):
		print ('Needs parameter containing url')
		return False
	return True

def parse_switch(type):
	return {
		'tag':parse_tags,
		'all':parse_all
	}.get(type, parse_na)

def parse_to_words(text):
	#tab_enter_table = string.maketrans('\n\t','  ')
	#text = text.translate(tab_enter_table, string.punctuation)
	text = regex_spaces.sub(' ',text)
	text = regex_non_alpha.sub('', text)
	word_arr = text.split(' ')
	word_arr = [word for word in word_arr if len(word) is not 0]
	return word_arr

def check_text(text, elem):
	s = get_dict_s('./Dictionary.csv')
	words = parse_to_words(text)
	#words = try_with_error(parse_to_words, message = 'error parsing text "'+text+'"', text = text)
	# if not words:
	#	return
	for word in words:
		if (word.isdigit()):
			continue
		if (word not in s and word.lower() not in s):
			print ('  misspelled word: '+word)
			print ('  in elem: '+str(elem))
			print ('===============================================')


def check_elems(elems):
	for elem in elems:
		text = elem.find(text=True,recursive=False)
		if (text):
			check_text(text, elem)

def parse_tags(soup, args):
	for tag in args:
		check_elems(soup.findAll(tag))

def parse_all(soup, args):
	check_elems(soup.body.findChildren())

def parse_na(soup, args):
	print ('malformed parse type')

def run(args):
	if (check_args(args)):	
		check_type = args[1]
		url = args[2]
		additional_args = args[3:]
		html = try_with_error(urllib2.urlopen, url = url, message = 'error reading url "'+url+'"')
		soup = BeautifulSoup(html)
		parse_switch(check_type)(soup, additional_args)



if __name__ == '__main__':
	run(sys.argv)


