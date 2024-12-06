Dungeon Quest

ATP

Test case 1: Test player movement (left and right)
Test description: verify that the player can left and right with the arrow keys
Test steps:
1. Start the game
2. Press left arrow key
3. Verify the player moves left
4. Press right arrow key
5. Verify the player moves right
Expected outcome: The player's character should move left and right when the left and right arrow keys are pressed

Test case 2: Test player movement (up and down)
Test description: Verify that the player can move up and down with the arrow keys
Test steps:
1. Start the game
2. Press up arrow key
3. Verify the player moves up
4. Press the down arrow key
5. Verify the player moves down
Expected outcome: The player's character should move up and down when the up and down arrow keys are pressed

Test case 3: Test player collision 
Test description: Verify that the player cannot move outside the boundaries of the map
Test steps:
1. Start the game
2. Use the arrow keys to move the character
3. Move the player into a wall
4. Verify the player is unable to walk through or beyond the wall
Expected outcome: the player should be unable to walk outside the map, staying in the boundaries of the map

Test case 4: Test player attack
Test description: Verify the player can attack an enemy
Test steps:
1. Start the game
2. Use the arrow keys to move the player
3. Approach an enemy
4. Press SPACE to attack the enemy when next to them
5. Verify the player is attacking the enemy until the enemy dies
Expected outcome: The player should be able to attack the enemy until the enemy dies

Test case 5: Test player death
Test description: Verify that the player can die
Test steps:
1. Start the game
2. Use the arrow keys to move the player
3. Move the player to an enemy
4. let the enemy attack the player
5. DO NOT ATTACK THE ENEMY
6. Verify that the player can die and the Game over screen appears
Expected outcome: The player should die once hit enough by enemies and a game over screen should appear allowing you to restart
  
