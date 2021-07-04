# Developer Wishlist

The following list contains desired changes to be implemented, preferably in order.

## Low level, next/immediate changes

* Expand `README.md` usage section or create a separate file.
* Write some issues based on `WISHLIST.md` on GitHub.
* Write unit tests.
  
### v0.4-beta Feedback:
* Ability to have 2 or more AI players.
* Choose to either randomise the starting SI cubes or input starting cubes manually.
* Ability to back/revert during SI cube starting phase.
* Initial bids need to be their own step and probably automated.
  * Seen a situation when Kait did not know she was the starting bid and bid too high...
  * ... could be an issue because she is not aware of others financial standings?
* Add a 'stats' option to show things like Kait's wallet.
* Add a question/option to do something other than place track if Kait does not own any company shares.

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
