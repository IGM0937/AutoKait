# Developer Wishlist

The following list contains desired changes to be implemented, preferably in order.

## Low level, next/immediate changes

* Expand `README.md` usage section or create a separate tutorial file.
* Write some issues based on `WISHLIST.md` on GitHub.
* Write unit tests.
  
### v0.4-beta Feedback:
* Game setup - Special interest cube setup:
  * Ability to back/revert to a previous selection.
  * Choose to either randomise the starting SI cubes or input starting cubes manually.
  * Ability to check if the game pieces are correctly placed on the board.
* Game setup - Initial bidding process:
  * A questionnaire type process, automated.
  * Seen a situation when Kait did not know she was the starting bid and bid too high. 
  * Could be an issue because she is not aware of others financial standings?
* Ability to have 2 or more AI players.
* Add a `stats` option to show things like Kait's wallet.
* Add a `viewboard` option to show what pieces are on the board.

## High level, future aspirational changes

* Introduce player tracking of money and company shares.
  * Automate dividend calculations per share.
* Remove user inputs for anything related to Kait.
  * Where to put trains.
  * Where to put special interest cubes.
  * Which company share to bid for.
  * ... and so on. _Have Kait tell you what to do!_
* Pathfinding for track and special interest cube placements.
* tkinter UI elements, such as:
  * board state view.
  * user input buttons.
* Calculate pros and cons for each action.
