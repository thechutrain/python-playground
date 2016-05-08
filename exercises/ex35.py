from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	choice = raw_input("> ")
	# better code to see if the raw_input is an int, since it will always return a string
	# try to cast it to an int
	try:
		how_much = int(choice)
	except ValueError:
		dead("Man, learn to type a number.")
	# if type(choice) == int:
	# 	how_much = int(choice)
	# else:
	# 	dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win 1 million doll-hairs!"
		exit("blah")
	else:
		dead("You greedy bastard")

def bear_room():
	print """
	There is a bear here.
	The bear has a bunch of honey.
	The fat bear is in front of another door.
	How are you going to move the bear?"""
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from teh door. You can go through it now"
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what %r means" % choice


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "he, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)


def start():
	print "You are in a dark room."
	print "There is a door to your right and left"
	print "Which one do you take?"

	choice = raw_input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stuble around the room until you starve.")

start()
