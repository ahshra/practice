#English to Chinese Study Tool
#To setup session, get unicode fro desired character set at: 
#http://www.mobilefish.com/services/unicode_escape_sequence_converter/unicode_escape_sequence_converter.php
#Format utf-8 to match existing format. Enter pinyin with tonal marks in number form (ex: 你 ni3)

print u'\u4e9a' u'\u4f26' u'\u5b66' u'\u4e60' u'\u6c49' u'\u8bed' u'\u7684' u'\u5de5' u'\u5177' '!'
#import sys
#sys.stdout.encoding 
#'US-ASCII'
#welcome_message.encode('utf-8')
#'\xe7\x8c\xab'
#print welcome_message.encode('utf-8')
print "\nSelect an English word or phrase and then think of \
\nthe Chinese equivalent and tone. \
\nThen enter the word as it appears in the word bank below. \
\nThe Chinese equivalent along with pinyin and tonal marks will be printed. \
\nDoes what you thought and the result match? \
\n \
\n       *** WORD BANK ***  \
\n1. to take the opportunity \
\n2. to harm \
\n3. \
\n4. \
\n5. \
\n6. \
\nNote that only 50 words can be studied in one session before you have to \
\nrestart. \
\n" # this is your introduction, and also where you can add words that can be looked up.



# here is there you can add new words to the dictionary so they can be searched.
word_bank = {
	'to take the opportunity': u'\u8d81' + ' chen4',
	'to harm': u'\u4f24' u'\u5bb3' + ' shang1hai4'
	
}

for turn in range(50): # can be adjusted for longer sessions
    translation = raw_input("What word do you select? ")
    if translation in word_bank:
        print word_bank[translation], "Lookup Number", turn + 1
    else:
        print "That word or phrase is either incomplete, \
        \nmisspelled, or is not in this word bank. \
        \nPlease try again."
    
    if turn == 50:
        print "Restart."

        
	
#import sys
#sys.stdout.encoding
#'US-ASCII'
#translation.encode('utf-8')
#'\xe7\x8c\xab'