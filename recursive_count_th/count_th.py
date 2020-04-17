'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):            # Moved count into params of func
										# When it was in body, every loop reset it to 0

	if len(word) < 2:                   # If the length is less than 2, it cannot contain 'th'
		return count
	elif word[:2] == 'th':              # Check the first 2 chars of the string for 'th'
		count += 1                      # If present, increment count by 1
	return count_th(word[1:], count)    # Return the function and start and the 1st index of the word and return the count


def begin(word):                        # Main function that just lets me pass in a string
	return count_th(word)               # Returns the function with the string as a param


print(begin('afdlkjasdfl;kthsadfkljdsalkthaskldfjdsklthasdklfjdsalkthsakldfjdslkthththth'))
