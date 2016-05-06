# /r is the carriage return
# while True:
# 	for i in ["/","-","|", "\\","|"]:
# 		print "%s\r" % i,

print "How old are you?",
age = raw_input()
print "How tall are you? (in inches)",
height = int(raw_input())
height_inches = height % 12
height_feet = (height - height_inches) / 12
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r\'%r\" tall and %r heavy." % (age, height_feet, height_inches, weight)