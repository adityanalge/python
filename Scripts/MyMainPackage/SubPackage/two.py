import one

print("Top Level in two.py")

one.myfunc()

if __name__ == '__main__':
	print("Two.py is being run directly")
else:
	print("Two.py is being imported")