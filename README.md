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

## Features

As of the latest release, v0.4:

- Automated Game A.I. as a stand-in for nth player in Irish Gauge.
- Kait can choose her next action when it's her turn.
  - Call for **auctions**.
  - Place company **train tracks**.
  - Place **special interests**.
  - Call for company **dividends**.
- Participate in the above actions out of turn, with the ability to back out of bids.
- Keep track (pun intended) of changes in board game pieces.
  - Placement of all company train tracks.
  - Placement of all special interests.
- Auto-calculate dividends per company.
- Keep track of Kait's money during bidding and dividend actions.

## Usage

All major releases are tagged and merged to the `main` branch. They could also be found under 'Releases' within GitHub.

To run AutoKait, simply execute the module containing the main function using Python 3:

```
$ python3 autokait.py
```

At any point, type `help` to get more information.

### Development

All development work is on the `dev` branch, until it is tagged and merged to main for release.

To run AutoKait in dev mode, allowing for a consistent game setup for development purposes, add the dev flag
or the short form `-d`: 

```
$ python3 autokait.py --dev
```

Please see `setup_init_game_pieces` function in `util.game_vars.py` module for more information.

## Important files

### ... for Contributions

Please see `CONTRIBUTING.md` for more information.

### ... for Changelog

Please see `CHANGELOG.md` for more information on notable changes.

### ... for Code of Conduct

Please see `CODE_OF_CONDUCT.md` for detailed guidelines.

### ... for Developer Wishlist

Alongside issues and discussions that exist within GitHub, `WISHLIST.md` also exists to keep a general list of desired changes.

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

* Main Developer: Igor Goran Mačukat

## Licence

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

See `LICENSE` in the root directory of the project.