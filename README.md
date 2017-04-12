## battleship

This is a desktop version of the board game Battleship I designed using python and the [pygame module][pygame-download], which must be downloaded for the game to run succesfully.  
To run the game, go the main directory and type the following command into the command line:  
`python2.7-32 main.py`

(Running simply `python main.py` will not work because this version of [pygame][pygame-download] is the 32 bit one)

## Note

This current version of the battleship game provides all the functionality of the boardgame version except that it does not allow you to configure your fleet formation. Instead, your fleet configuration is determined at start randomly.  
The ability for manual fleet configuration will be added soon.

## Credit 

The [blockSky.png][block] and [fire.png][fire] files were created by [Koh Terai][Koh-Terai] for the [game][HideAndSeak] we made as a final project for our Intro to CS class in Fall of 2013.

The salvatoreSinkingShips.mp3 file was made by converting the following [video][Salvatore] to mp3. Salvatore's Sinking Ships is a mini-game within the video game, _The Legend of Zelda: the Wind Waker_, released by Nintendo on the Nintendo GameCube. 

## Bug

If the program doesn't run, and instead, you receive the following message, don't worry! Just retry the command, and it should work!  
>Traceback (most recent call last):
  File "main.py", line 132, in <module>
    player1_fleet = fleet_builder.fleet_builder(player1_board)
  File "/Users/NoobyPls/code/self_projects/battleship/fleet_builder.py", line 236, in fleet_builder
    ship_builder(player_board, player_fleet[ship], player_fleet)
  File "/Users/NoobyPls/code/self_projects/battleship/fleet_builder.py", line 195, in ship_builder
    direction = direction_picker(player_board, current_ship, first_coordinate, player_fleet)
  File "/Users/NoobyPls/code/self_projects/battleship/fleet_builder.py", line 169, in direction_picker
    direction = random.choice(possible_directions)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py", line 274, in choice
    return seq[int(self.random() * len(seq))]  # raises IndexError if seq is empty
IndexError: list index out of range



[pygame-download]: http://www.pygame.org/download.shtml
[Koh-Terai]: http://www.kohterai.com/#/
[HideAndSeak]: https://github.com/kohterai/HideAndSeak
[Salvatore]: https://www.youtube.com/watch?v=q_rQpf7yF9Y
[block]: https://github.com/mav-zate/battleship/blob/master/battleship/data/blockSky.png
[fire]: https://github.com/mav-zate/battleship/blob/master/battleship/data/fire.png

