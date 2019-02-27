# Robot Vacuum

Due: February 6, 2019</br>

• A Map instance has 19 × 19 locations, and each location is dirty `(1)` or not `(0)`.
• The robot can change the status of a location `(from dirty (1) to clean (0))` when it is located on the location.
• The robot should begin the cleaning job from `[0, 0]` location.
• The robot has up to 8 adjacent locations, i.e., Top-left, Top-middle, Top-right, Left, Right, Bottom-left, Bottom-middle, Bottom-right.
• The robot can see only adjacent locations’ cleaning condition.
• The robot can move to the one of the adjacent locations of the current location.
• The robot should record its locations in the `self.track list`.
• The robot should clean all of the `dirty` locations.
• The length of the self.track list should be definitely less than `19 × 19`.
