# Battleship

This is a desktop version of the popular board game Battleship written in Python 2.7.

## Setup

Download a 32-bit version of pygame from [pygame][pygame-download-directory]. For Mac OS X users, you can download pygame directly
from [here][pygame-download-mac].

Make sure that you have Python 2.7 installed. You may download the appropriate version [here][python-download]

To run the game, go the main directory and run `python2.7-32 main.py` from the command line.

## Instructions

The game plays exactly as the table-top version except that players' fleet configurations are randomly determined at start. To receive indication of hit or miss, turn sound on. A "kaboom" means a hit, and a "sploosh" means a miss. Press enter to reveal each player's side of the board. Click on the square that you want to fire at. 

![battleship_instructions][battleship_instructions]

The left board (in green) is the current player's board. The board on the right (in red) is the current player's view of the enemy board.


## Gameplay

![gameplay_gif][gameplay_gif]

## Credits

![blockSky.png][block]
![fire.png][fire] 

These images were designed by [Koh Terai][Koh-Terai] for the [game][HideAndSeak] we developed for an Intro to CS class in 2013.

The salvatoreSinkingShips.mp3 file was made by converting the following [video][Salvatore] to mp3. Salvatore's Sinking Ships is a mini-game within the video game, _The Legend of Zelda: the Wind Waker_, released by Nintendo on the Nintendo GameCube. 

[pygame-download-directory]: http://www.pygame.org/download.shtml
[pygame-download-mac]: http://pygame.org/ftp/pygame-1.9.1release-python.org-32bit-py2.7-macosx10.3.dmg
[python-download]: https://www.python.org/downloads/
[Koh-Terai]: http://www.kohterai.com/#/
[battleship_instructions]: https://github.com/mav-zate/battleship/blob/master/readme_images/board_help.png
[gameplay_gif]: https://github.com/mav-zate/battleship/blob/master/readme_images/battleship.gif
[HideAndSeak]: https://github.com/kohterai/HideAndSeak 
[Salvatore]: https://www.youtube.com/watch?v=q_rQpf7yF9Y
[block]: https://github.com/mav-zate/battleship/blob/master/battleship/data/blockSky.png "Block sky"
[fire]: https://github.com/mav-zate/battleship/blob/master/battleship/data/fire.png "Fire"

