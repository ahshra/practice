# 3. real time English and Chinese RMB to USD converter

import requests

# begin Chinese characters. To get unicode, go to: 
# http://www.mobilefish.com/services/unicode_escape_sequence_converter/unicode_escape_sequence_converter.php

x = u'\u4f60' u'\u60f3' u'\u77e5' u'\u9053' u'\u76f8' u'\u5e94' u'\u7684' u'\u7f8e' u'\u91d1' u'\u662f' u'\u591a' u'\u5c11' '?'
import sys
sys.stdout.encoding
'US-ASCII'
x.encode('utf-8')
'\xe7\x8c\xab'
print x.encode('utf-8')

# English translation

x = float(raw_input('How much CNY do you want to know equals how much USD? '))

url = ('https://currency-api.appspot.com/api/CNY/USD.json')

print url

#  another Chinese sentence

y = u'\u5f53' u'\u4e0b' u'\u7684' u'\u6c47' u'\u7387' u'\u662f' u'\uff1a' ':'
import sys
sys.stdout.encoding
'US-ASCII'
y.encode('utf-8')
'\xe7\x8c\xab'
print y.encode('utf-8')

r = requests.get(url) # this retrieves the URL above

# another English sentence 

print ('The exchange rate right now is ') 
print r.json()['rate']

# another Chinese sentence

z= u'\u00a0' u'\u76f8' u'\u5e94' u'\u7684' u'\u7f8e' u'\u91d1' u'\u662f' ':'
import sys
sys.stdout.encoding
'US-ASCII'
z.encode('utf-8')
'\xe7\x8c\xab'
print z.encode('utf-8')

# another English sentence

print ('The amount of equivalent USD for the amount entered is ') 
print x*float(r.json()['rate'])