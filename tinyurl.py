import urllib.request, urllib.error, urllib.parse
import json
import threading
import webbrowser 
def test_word(word):
	url = 'http://tinyurl.com/' + word
	try:
		response = urllib.request.urlopen(url)
		response = response.geturl()
	except:
		return False
	#print (word)
	if response != url and response[0:19] != "http://tinyurl.com/":
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
			#print ("word is " + str(word) + " and url is " + str(response))
			webbrowser.open_new_tab(response)
	for word in words:
		print ("word is " +  word[0] + " and response is " + word[1])
		#print(word[1])
	return words
unix_check()	


	


		
thread_unix_check()
