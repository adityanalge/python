import one

print("Top Level in two.py")

one.myfunc()

if __name__ == '__main__':
	print("two.py is being run directly")
else:
	print("two.py is being imported")