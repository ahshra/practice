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
	
	#print now
	#print now.year
	#print now.month
	#print now.day

from datetime import datetime
now = datetime.now()

print 'Today\'s date is %s-%s-%s' % (now.year, now.month, now.day)

from datetime import datetime,time
now = datetime.now()
time = datetime.now()

print 'The time is now %s:%s:%s' % (now.hour, now.minute, now.second)
to_go = raw_input('What time would you like to go? ')
time_until = float(to_go) - float(time.hour)
print 'That\'s in %s hours!' % (time_until)
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
print "%02d:%02d:%02d" % (time.hour, time.minute, time.second)