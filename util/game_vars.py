"""
List of global game variables and their starting defaults, if relevant.

    POTENTIAL FUTURE VARIABLES:
        - Player
            - Name
            - Wallet/Money
        - Company
            - # of tracks used
            - # of tracks available
            - ordered list of shares and their values
            - # of connections to towns
            - # of connections to cities
            - # of connections to major cities
        - Interest Cube (Manager)
            - # of cubes on map
            - # of cubes used as dividends
            - # of cubes left to be used
            - cube percentage breakdowns
        - Dividend Payout Object (Manager)
            - Dividend history
                - Company payouts?
                - Player payouts?
        - Locations
            - Type: Town, City, Major City
            - Interest Cube type: Black, Pink, White, None
        - Terrain
            - Type: Easy, Medium (Easy + Tracks), Hard (Difficult)

    POTENTIAL FUTURE DATA POINTS:
        * storing the above variables
        - company rating
        - interest cube rating
        - player threat rating
"""

last_action = None
data_point = {}

# data point tags
CAIT_WALLET = 'data.cait.wallet'
