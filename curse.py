import urllib.request, urllib.error, urllib.parse
import json

def apple_check():
  wordlist = open('/usr/share/dict/words')
  wordlist = wordlist.read()
  wordlist = wordlist.split('\n')
  curse = []
  for word in wordlist:
    url = 'http://www.wdyl.com/profanity?q=' + word
    response = urllib.request.urlopen(url)
    response = json.loads(response.read().decode())
    if response['response']=='true':
      print(word)
      curse.append(word)
      continue
    print(word)
    print(response)
    continue
  print ('\n\n\n')
  for word in curse:
    print(word)

def urban_dictionary():
  pass
apple_check()
