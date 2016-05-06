# this one is like your scfipts with argv
#adding * in the arguments makes it flexible?
# asterisk arg --> passing in a list into the argument
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments:
def print_none():
	print "I got nothin'."

print_two("alan", "chew")
print_two_again("alan", "chewbacca")
print_one("First!")
print_none()