# AutoKait - Automated Irish Gauge Player

## Overview

The automa Kait (**K**ait the **A**utomated **I**rish **T**ransport, a.k.a. AutoKait) is an automated A.I. player
designed to be used for the board game, Irish Gauge.

The original concept and design is based on an existing Irish Gauge automa called CAIT (Chase's Automa for Irish
Transit). Whilst Kait closely follows the principles or dice rolls to determine Kait's next move, the future versions of
AutoKait will hopefully expand to be more deterministic in how it chooses their next action.

The project has since turned into a little side passion project to create board game A.I. and in turn investigate
artificial intelligence in general.

> Please be aware that this automa was written as an exercise in learning the Python 3 language.
>
> The code may have potentially questionable, non-standardised or non-conventional practices and implementations.
>
> Please be kind. I'm happy to hear about any improvements.

## Usage

All major releases are tagged and merged to the `master` branch.

All development work is on the `dev` branch, until it is tagged and merged to master for release.

Simply execute the application from `autocait.py` module.

At any point, type **_explain_** to get more information.

## Overall Features

As of version v0.3:

- Automated Game A.I. as a stand in for nth player in Irish Gauge.
- Decide on next action, when it is Kait's turn. 
- Participate in auctions, with the ability to back out of bids.
- Activate dividend action out of turn for purposes of receiving dividends.
- Keep track of Kait's money during bidding and dividend actions.

## Contributions

Projects contributions of any kind a welcome and any sizable contributions to the project will be credited.

- If you have any suggestions, raise an issue.
- If you have any code changes, raise a pull request for any changes.
    - To which branch you to merge to is up to you.

All contributions have are a few stipulations:

1. Not all suggestions or code changes are guaranteed to be accepted into the project.
2. Not all suggestions or code changes are guaranteed to be accepted in the state they have been submitted.

Hopefully discussions can be had over the contributions in order to avoid any confusion or misunderstandings.

As always, thank you in advance for taking the time to look at the project in depth.

## Developer Wishlist

The following list contains desired changes to be implemented, preferably in order.

### Low level, next/immediate changes

* Re-write and add more method documentations
* Write unit tests
* Manual testing of v0.4-beta in game

### High level, future aspirational changes

* Introduce player tracking of money and company shares
    * Automate dividend calculations per share
* Remove user inputs for anything related to Kait
    * Where to put trains
    * Where to put special interest cubes
    * Which company share to bid for
    * ... and so on. _Have Kait tell you what to do!_
* Pathfinding for track and special interest cube placements
* tkinter UI elements, such as:
    * board state view
    * user input buttons
* Calculate pros and cons for each action

## Release Notes

The following list of major changes can be found under designated git tags.

### v0.4 provisional

- Changed the Game A.I. name to Kait to avoid confusion with original CAIT
- Introduction of a game board, game pieces and placement checks
- Major Quality of Life improvements

### v0.3

- Added wallet to keep track of money
- Improved blind bidding logic
  - Now incremental, with potential to back out of bidding
  - Added ability for Cait to pay for winning bids
- Improved dividend functionality
  - Added ability to Cait to receive dividends into wallet 
- Expanded quality of life improvements
  - Improvements to console text
- Organisation
  - Logical changes to output text and file
  - Added TODOs for next version
- Clean up of code and refactors

### v0.2

- Added basic comments and documentation
- Added blind bidding
- Added basic quality of life improvements 
- Added project specific files
- Expanded on the project with boilerplate code
  - Added constants module
  - Added global variables module
  - Externalising console outputs to a separate module
  - Externalising commonly used functions to a separate module
- Organisation
  - Addition of packages: `action` and `util`
  - Splitting up of different actions into separate modules
- Clean up of code and refactors

### v0.1

- MVP application.
- Single Python module.
- Raw implementation of the original CAIT.
- Main decision-making function, using random number generator as a 6 sided dice.

## Credits

#### Irish Gauge

* Designer: Amabel Holland
* Artist: Ian O'Toole
* Publisher: Capstore Games
* Official Website: [Capstone Games](https://capstone-games.com/board-games/irish-gauge/)

#### CAIT Automa

* Designer: Chase Estep
* Release Forum Post: [BoardGameGeek](https://boardgamegeek.com/thread/2321313/cait-irish-gauge-automa-solo-or-2p-games)
* Download Page: [BoardGameGeek](https://boardgamegeek.com/filepage/192125/cait-automa)

#### AutoKait

* Main Developer: Igor Mačukat
