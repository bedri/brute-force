import urllib.request, urllib.error, urllib.parse
import json
from subprocess import Popen, PIPE

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

def unix_check():
  wordlist = open('words.txt')
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
def randomdict():
    spell = Popen(['exec.sh'], stdin = PIPE, stdout=PIPE, stderr = PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    rc = p.returncode
    print(rc)
    spell = str(rc)
    print(spell)
    spell = spell.split('define.php?term=')
    print(spell)
    #print(spell[1])
randomdict()
