str = input()
str = str.lower()
if str[0] in 'aeiou':
	str = str + 'ay'
else:
	str = str[1:] + str[0] + 'ay'
print (str)	