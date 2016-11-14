#! /usr/bin/python

import re
from bs4 import BeautifulSoup
import requests
from optparse import OptionParser
import sys
import time

class Scholar():
	def __init__(self, options):
		self.author = options.author
		self.all = options.all
		self.some = options.some
		self.none = options.none
		self.phrase = options.phrase
		self.pub = options.pub
		self.after = options.after
		self.before = options.before
		self.count = options.count
		if options.title_only:
			self.title = 'title'
		else:
			self.title = 'any'

	def create_url(self):
		default = 'https://scholar.google.com/scholar?'
		url = default + 'as_q=' + '+'.join(self.all.split()) \
			  		  + '&as_epq=' + '+'.join(self.phrase.split()) \
			  		  + '&as_oq=' + '+'.join(self.some.split()) \
			  		  + '&as_eq=' + '+'.join(self.none.split()) \
			  		  + '&as_occt=' + self.title \
			  		  + '&as_sauthors=' + '+'.join(self.author.split()) \
			  		  + '&as_publication=' + '+'.join(self.pub.split()) \
			  		  + '&as_ylo=' + self.after \
			  		  + '&as_yhi=' + self.before \
			  		  + '&btnG=&hl=en&as_sdt=0%2C39'
		return url

	def send_query(self, url):
		response = requests.get(url)
		html = response.content
		return html

	def parse_html(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		title_tag = soup.findAll('div', 'gs_ri')
		title = []
		next_link = None
		for i in xrange(len(title_tag)):
			try:
				atag = title_tag[i].h3.a
				title.append(''.join(atag.findAll(text=True)))
			except:
				continue
		next_tag = soup.find('span', 'gs_ico gs_ico_nav_next')
		if next_tag:
			next_link = 'https://scholar.google.com' + next_tag.parent['href']
		return title, next_link

	def get_content(self):
		url = self.create_url()
		html = self.send_query(url)
		title_set, next_link = self.parse_html(html)
		while next_link:
			html = self.send_query(next_link)
			title, next_link = self.parse_html(html)
			title_set.extend(title)
			time.sleep(1)
		print title_set

	def get_all_content(self):
		title = get_page_content(url)


def main():
	parser = OptionParser()
	parser.add_option('-a', '--author', metavar='AUTHORS', default='',
                      help='Author name(s)')
	parser.add_option('-A', '--all', metavar='WORDS', default='',
                      help='Results must contain all of these words')
	parser.add_option('-s', '--some', metavar='WORDS', default='',
                      help='Results must contain at least one of these words. Pass arguments in form -s "foo bar baz" for simple words, and -s "a phrase, another phrase" for phrases')
	parser.add_option('-n', '--none', metavar='WORDS', default='',
                      help='Results must contain none of these words. See -s|--some re. formatting')
	parser.add_option('-p', '--phrase', metavar='PHRASE', default='',
                      help='Results must contain exact phrase')
	parser.add_option('-t', '--title-only', action='store_true', default=False,
                      help='Search title only')
	parser.add_option('-P', '--pub', metavar='PUBLICATIONS', default='',
                      help='Results must have appeared in this publication')
	parser.add_option('--after', metavar='YEAR', default='',
                      help='Results must have appeared in or after given year')
	parser.add_option('--before', metavar='YEAR', default='',
                      help='Results must have appeared in or before given year')
	parser.add_option('-c', '--count', type='int', default=None,
                      help='Maximum number of results')
	options, _ = parser.parse_args()

	querier = Scholar(options)
	querier.get_content()

	return 0

if __name__ == "__main__":
    sys.exit(main())