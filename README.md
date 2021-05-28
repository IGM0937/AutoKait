# AutoKait - Automated Irish Gauge Player

## Overview

The automa Kait (**K**ait the **A**utomated **I**rish **T**ransport, a.k.a. AutoKait) is an automated A.I. player designed to be used for the board game, Irish Gauge.

The original concept and design was based on an existing Irish Gauge automa called CAIT (Chase's Automa for Irish Transit). Whilst Kait closely follows the princibles or dice rolls to determine Kait's next move, the future versions of AutoKait will hopefully expand to be more deterministic in how it chooses their next action.

The project has since turned into a little side passion project to create board game A.I. and in turn investigate artificial intelligence in general.

>Please be aware that this automa was written as an exercise in learning the Python 3 language.
> 
> The code may have potentially questionable, non-standardised or non-conventional practices and implementations.
> 
> Please be kind. I'm happy to hear about any improvements.

## Contributions

TODO

## Usage

Simply execute the application from `autocait.py` and follow the instructions to setup the state of the board.

At any point, type **_explain_** to get more information.

## Features

TODO

## Developer Wishlist

The following list contains desired changes to be implemented, preferably in order.

If you wish to contribute, please raise a pull request. Successful merge not guaranteed.
  
### Low level, next/immediate changes
  * Complete README.md file
  * Replace `explain` with `help` where applicable
  * Re-write help text
  * Add help text for new/recent user inputs
  * Write simple README file
  * Alter game and code text to Kait and AutoKait
  * Re-write and add more method documentations
  * Write unit tests

### High level, future aspirational changes
  * Introduce player tracking of money and company shares
    * Automate dividend calculations per share
  * Remove user inputs for anything related to Kait
    * Where to put trains
    * Where to put special interest cubes
    * Which company share to bid for
    * ... and so on
    * ... _have Kait tell you what to do on the game board for her!_
  * Pathfinding for track and special interest cube placements
  * `tkinter` UI elements, such as:
    * board state view
    * user input buttons
  * Make Kait choose her next steps/actions
    * Calculate Pros and Cons of each step
    * Ranking algorithm to help choose 

## Release Notes

The following list of major changes and can be found under designated git tags.

### v0.3
TODO
### v0.2
TODO
### v0.1
TODO

## Credits
#### Irish Gauge 
  * Designer: Amabel Holland
  * Artist: Ian O'Toole
  * Publisher: Capstore Games
  * Official Game Website: [capstone-games.com](https://capstone-games.com/board-games/irish-gauge/)
#### Cait Automa
  * Designer: Chase Estep
  * Release Forum Post: [boardgamegeek.com](https://boardgamegeek.com/thread/2321313/cait-irish-gauge-automa-solo-or-2p-games)
  * Download Page: [boardgamegeek.com](https://boardgamegeek.com/filepage/192125/cait-automa)
#### AutoKait
  * Developer: Igor Goran Mačukat
  * GitHub Profile: [github.com/IGM0937](https://github.com/IGM0937)
