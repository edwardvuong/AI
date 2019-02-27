# Robot Vacuum

Due: February 6, 2019</br>

## Requirements ##
* A Map instance has `X * Y` locations, and each location is dirty `(1)` or not `(0)`.</br>
* The robot can change the status of a location `(from dirty (1) to clean (0))` when it is located on the location.</br>
* The robot should begin the cleaning job from `[0, 0]` location.</br>
* The robot has up to 8 adjacent locations, i.e., Top-left, Top-middle, Top-right, Left, Right, Bottom-left, Bottom-middle, Bottom-right.</br>
* The robot can see only  `adjacent locations’ ` cleaning condition.</br>
* The robot can move to the one of the adjacent locations of the current location.</br>
* The robot should record its locations in the `self.track list`.</br>
* The robot should clean all of the `dirty` locations.</br>
* The length of the self.track list should be definitely less than `X * Y`.</br>

## Methodology ##
Given a square map the `clean`  function cleans the entire first row if the map is of an odd size by going towards the rightwards direction. Now that we ensure we have an map size that is divisible by `2` . We can clean rest of the map by looking at dirt in the `3` adjacent locations from our current position. </br>

Skipping an additonal 2 rows and repeat the process going in the leftwards direction the robot will move in the leftwards direction searching for dirt in the adjacent top-left, top-middle, and left positions. This process repeats till we hit the end of the map at location  `[0, Y]`.  </br>

We now repeat the process again skipping `2` rows moving in the opposite direction and checking the adjacent locations from there. </br>

From `[0, Y]` we increase `Y` by `2` then move in the rightwards direction opposite from our previous step. We continue this loop till all rows have been checked.</br>

By checking the `3` adjacent locations from our robot we can ensure that the robot will never visit  
