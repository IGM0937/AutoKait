"""
List of global game variables and their starting defaults, if relevant.

    POTENTIAL FUTURE VARIABLES:
        - Player
            - Name
            - Money
        - Company
            - # of tracks used
            - # of tracks available
            - ordered list of shares and their values
            - ?? connections and what does this company "own" ??
        - Interest cubes
            - # of cubes on map
            - ?? breakdown, # of pink, black, white ??

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
