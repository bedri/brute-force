import urllib.request, urllib.error, urllib.parse
import json
import threading
 
def test_word(word):
	url = 'http://shoutkey.com/' + word
	response = urllib.request.urlopen(url)
	response = response.geturl()
	if response != url:
		return response
	else:
		return False


def thread_test_word(word):
	url = 'http://shoutkey.com/' + word
	print(word)
	response = urllib.request.urlopen(url)
	response = response.geturl()
	if response != url:
		print (response)
		return response
	else:
		return False


def unix_check():
	wordlist = open('words.txt')
	wordlist = wordlist.read()
	wordlist = wordlist.split('\n')
	words = []
	for word in wordlist:
		response = test_word(word)
		if response == False:
			continue
		else:
			words.append([word, response])
			print ("word is " + str(word) + " and url is " + str(response))
	for word in words:
		print ("word is " +  word[0] + " and response is " + word[1])
	return words
unix_check()	


	


		
thread_unix_check()
