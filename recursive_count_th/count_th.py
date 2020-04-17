'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
	print(word)
	if len(word) < 2:
		return count
	elif word[:2] == 'th':
		count += 1
	return count_th(word[1:], count)


def begin(word):
	return count_th(word)


print(begin('afdlkjasdfl;kthsadfkljdsalkthaskldfjdsklthasdklfjdsalkthsakldfjdslkthththth'))
