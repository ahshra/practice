# 1. A tip calculator

meal = 44.51
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print "Your total with tax and tip is " + ("%.2f" % total) # print two decimals with %.2f