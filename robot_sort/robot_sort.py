class SortingRobot:
	def __init__(self, l):
		"""
		SortingRobot takes a list and sorts it.
		"""
		self._list = l  # The list the robot is tasked with sorting
		self._item = None  # The item the robot is holding
		self._position = 0  # The list position the robot is at
		self._light = "OFF"  # The state of the robot's light
		self._time = 0  # A time counter (stretch)

	def can_move_right(self):
		"""
		Returns True if the robot can move right or False if it's
		at the end of the list.
		"""
		return self._position < len(self._list) - 1

	def can_move_left(self):
		"""
		Returns True if the robot can move left or False if it's
		at the start of the list.
		"""
		return self._position > 0

	def move_right(self):
		"""
		If the robot can move to the right, it moves to the right and
		returns True. Otherwise, it stays in place and returns False.
		This will increment the time counter by 1.
		"""
		self._time += 1
		if self._position < len(self._list) - 1:
			self._position += 1
			return True
		else:
			return False

	def move_left(self):
		"""
		If the robot can move to the left, it moves to the left and
		returns True. Otherwise, it stays in place and returns False.
		This will increment the time counter by 1.
		"""
		self._time += 1
		if self._position > 0:
			self._position -= 1
			return True
		else:
			return False

	def swap_item(self):
		"""
		The robot swaps its currently held item with the list item in front
		of it.
		This will increment the time counter by 1.
		"""
		self._time += 1
		# Swap the held item with the list item at the robot's position
		self._item, self._list[self._position] = self._list[self._position], self._item

	def compare_item(self):
		"""
		Compare the held item with the item in front of the robot:
		If the held item's value is greater, return 1.
		If the held item's value is less, return -1.
		If the held item's value is equal, return 0.
		If either item is None, return None.
		"""
		if self._item is None or self._list[self._position] is None:
			return None
		elif self._item > self._list[self._position]:
			return 1
		elif self._item < self._list[self._position]:
			return -1
		else:
			return 0

	def set_light_on(self):
		"""
		Turn on the robot's light
		"""
		self._light = "ON"

	def set_light_off(self):
		"""
		Turn off the robot's light
		"""
		self._light = "OFF"

	def light_is_on(self):
		"""
		Returns True if the robot's light is on and False otherwise.
		"""
		return self._light == "ON"

	def sort(self):
		"""
		Sort the robot's list.
		"""
		# Fill this out
		while True:                             # This will cause the loop to run until a break
			self.set_light_off()                # Turn light off so we can check against it later
			while self.can_move_right():        # Do the following while we are able to move right             This loop will repeat
				self.swap_item()                # Trade None for list[i]                                       As long as we are able to move right
				self.move_right()               # Move to the right                                            It will consistently grab the None value
				if self.compare_item() == 1:    # If the held item is greater than the [i]                     Replace it with [i]
					self.swap_item()            # Swap them                                                    And then compare held item against [i]
				self.move_left()                # Move back to the left
				self.swap_item()                # And swap the [i] with None
				self.move_right()               # Move back right
			while self.can_move_left():
				self.swap_item()
				self.move_left()
				if self.compare_item() == -1:
					self.swap_item()
					self.set_light_on()
				self.move_right()
				self.swap_item()
				self.move_left()
			if self.light_is_on() is False:     # We can only get here if the list is sorted
				break


'''
Code visualization:
IN HAND
CURRENT LIST

BEING LOOP
N
4 2 5 1 3

SWAP
4
N 2 5 1 3

MOVE RIGHT
  4
N 2 5 1 3

SWAP IF 1
  2
N 4 5 1 3

MOVE LEFT
2
N 4 5 1 3

SWAP FOR NONE
N
2 4 5 1 3

MOVE RIGHT
  N
2 4 5 1 3

REPEAT TO END

REVERSE FOR LEFT
'''

'''
The light can be used to start at the beginning of list
If light is on...
Pick up first item
If can move right
Move right
Swap if 1
Turn light on to restart loop
If current item is less than position item
Move left
Swap item
Move right
If can't move right
Move left to end of list (while can move left)
If the light is on, if we move left, it will start the function over
So the light needs to be turned off before we go back to the start of the list
Turn off light, and while we can move left, move left
Then turn the light back on
---------------------------------------------------------------------------------
WE NEED TO COMPARE NEGATIVES AS WELL
---------------------------------------------------------------------------------
Turn light on to start loop
Turn light off so it can be turned back on at end of loop
Swap none for item
Move right while able to move right
Compare items
Swap if 1
Turn light on to repeat loop
When reaching end of list
Go back left and repeat?
'''

if __name__ == "__main__":
	# Test our your implementation from the command line
	# with `python robot_sort.py`

	l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99,
	     93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59,
	     64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75,
	     36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

	robot = SortingRobot(l)

	robot.sort()
	print(robot._list)
