# Changelog

All notable changes to this project will be documented in this file.

The following list of major changes can also be found under designated git tags.

>The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
<!--
## [version number] - YEAR-MONTH-DAY

### Sections
'Added' for new features.
'Changed' for changes in existing functionality.
'Deprecated' for soon-to-be removed features.
'Removed' for now removed features.
'Fixed' for any bug fixes.
'Security' in case of vulnerabilities.

[version number]: Link
-->

[comment]: <> (## [Unreleased])

## [v0.4] - 2021-03-20

### Added

- Added developer mode, `--dev` and `-d` flags on start up.
- Game setup for players (Kait only), game board and pieces.
- Game teardown, exit text only.
- New reference game board/map.
- Ability to reference tile locations, train pieces and special interest cubes.
- Player class for containing player information.
- Tile class for the creation of in memory board game definition.
- `CHANGELOG.md` file, a log of changes between current and future releases.
- `CODE_OF_CONDUCT.md` file, containing GitHub's community conduct rules. 
- `CONTRIBUTING.md` file, list or rules and notes on contributing to the project.
- `WISHLIST.md` file, containing a small to do list of next desired changes.
- `LICENSE` file, containing GNU v3 licence text and updates to all files with license references.

### Changed

- Improved console output text.
- Improved help actions text.
- Improved general action.
  - Ability to back or exit out of questions and inputs.
  - Changes to the term 'last action' to the more appropriate 'current action'.
  - Call every action out of turn for 'human' players.
- Improved auctions action.
  - Added checks for ability to perform auctions based on current wallet balance.
- Improved bidding action.
  - Bidding logic and refactoring of code to improve readability.
- Improved special interest action.
  - Ability to select a special interest cube and for placement.
- Improved dividends action.
  - Ability to select drawn special interest cubes.
  - Auto-calculation of dividends per company.
- Improved tracks action.
  - Ability to add tracks to the board based on company selection.
  - Automatically validate track placement, including locations and building costs.
- Improved common tools for game piece control and calculations.
- Changed the Game A.I. name to Kait to avoid confusion with original CAIT.
- Improved documentation on modules and functions.
- `README.md` file, separating out sections into individual files.

## [v0.3] - 2021-03-20

### Added

- Trigger bidding and dividends actions out of Cait's turn.
- Wallet to keep track of money.
- Ability for Cait to pay for winning bids.
- Ability for Cait to receive dividends into wallet.
- Ability for Cait to potentially back out of bidding.
  
### Changed

- Improved blind bidding logic.
- Improved dividend functionality.
- Expanded quality of life improvements.
- Improvements to console text.
- Logical changes to output text.
- Renamed application start file.
- Added TODOs for next version.
- Clean up of code and refactors.

## [v0.2] - 2021-03-15

### Added

- Basic comments and documentation.
- Blind bidding.
- Project specific files.
- Expanded on the project with boilerplate code.
- Addition of packages: `action` and `util`.
- Splitting up of different actions into separate modules.
- Constants module.
- Global variables module.
- Output module for externalising console outputs.
- Common utility module for externalising commonly used functions.

### Changed

- Basic quality of life improvements.
- Clean up of code and refactors.

## [v0.1] - 2021-03-14

### Added

- MVP application.
- Single Python module.
- Raw implementation of the original CAIT.
- Main decision-making function, using random number generator as a 6 sided dice.

[unreleased]: https://github.com/IGM0937/AutoKait/compare/v0.4...dev
[v0.4]: https://github.com/IGM0937/AutoKait/compare/v0.3...v0.4
[v0.3]: https://github.com/IGM0937/AutoKait/compare/v0.2...v0.3
[v0.2]: https://github.com/IGM0937/AutoKait/compare/v0.1...v0.2
[v0.1]: https://github.com/IGM0937/AutoKait/releases/tag/v0.1