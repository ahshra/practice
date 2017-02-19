# 11. Age teller date time There are 2 kinds of time - naive and aware. 

from datetime import datetime

now = datetime.now()

print ('The year is %s') % (now.year)
how_old = raw_input('Can I tell you how old you are, yes or no? ' )
if how_old == 'no':
	print 'Ok,  I won\'t.'
else:
	if how_old == 'yes': 
		what_year = raw_input('What year were you born? ')
		current_age = int(now.year) - int(what_year)
		print ('So, your current age is about %s.') % (current_age)
