# below is a game where 儿 is added to the end of everything.

z= u'\u513f'
import sys
sys.stdout.encoding
'US-ASCII'
z.encode('utf-8')
'\xe7\x8c\xab' #some coding to account for variations in terminal environment 
#that will influence utf-8 and Chinese character output.

original = raw_input('Enter a word and I\'ll put an "er" on the end of it : ')
if len(original) > 0:
    new_word = original + z.encode('utf-8')
    print new_word
else:
    print 'empty'