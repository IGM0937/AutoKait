def welcome_text():
    res = "Welcome to AutoCait."
    res += '\n'
    res += "Let's play Irish Gauge!"
    res += '\n'
    res += "Please setup the game and proceed when completed..."
    res += '\n'
    return res


def exit_text(forced):
    text = 'Goodbye'
    return f"Forced exit... {text}" if forced else text


def cait_waiting_turn_text():
    return "Press enter when it is Cait's turn... "


def cait_turn_text():
    return "Cait would like to... "


def invalid_input():
    return "Invalid input. Try again.\n"


def special_interest_action_text():
    return "Place a special interest cube\n"


def special_interest_action_explain_text():
    res = "Place a special interest cube for the company Cait has the most share value, prioritising companies " \
          "it owns first. In case of a tie, place for the company Cait owns that has the most trains on the map."
    res += '\n\n'
    res += "Choose a colour that isn't present on that trainline yet. If there are 2 colours, choose at random."
    res += '\n\n'
    res += "When deciding on which city to place the cube, select from the following list:"
    res += '\n'
    res += "    * Towns occupied by 2+ of Cait's trains"
    res += '\n'
    res += "    * Towns occupied by 1 of Cait's trains"
    res += '\n'
    res += "    * Towns occupied by 2 different player's trains"
    res += '\n'
    return res


def place_tracks_action_text():
    return "Place rail tracks\n"


def place_tracks_action_explain_text():
    res = "Place trains for the company that Cait owns, but has the least trains on the map. " \
          "If tied, place for the company with the most share value."
    res += '\n\n'
    res += "Build towards the closest Town or City. If tied, follow the rule: " \
           "City with special interest not present on line > City > Town"
    res += '\n'
    return res


def call_auction_action_text():
    return "Call an auction action\n"


def call_auction_action_explain_text():
    res = "Perform a blind auction a share for a company that currently has the most connections to Towns or Cities. " \
          "If tied, pick the share with the lowest face value."
    res += '\n\n'
    res += "If Cait does not have enough money for that share, she performs Call for Dividends instead."
    res += '\n\n'
    res += "If Cait is in the bidding war, roll a d10 (9 max) and add the number to the minimum value of share to " \
           "calculate her maximum bid. The rest of the players choose what their maximum bid as well."
    res += '\n\n'
    res += "The winner of the share is the player who bid the most, but pays the bid of the second highest bid."
    res += '\n\n'
    res += "If there is a tie, the player closes to the auctioneer in turn order (including the auctioneer) wins."
    res += '\n'
    return res


def call_auction_action_be_performed_text():
    return "Can Cait auction the specific share? Y/N "


def call_dividends_action_text():
    return "Call for dividends\n"


def call_dividends_action_explain_text():
    return "In the event where there are no dividend cubes in the bag with the same colours owned by Cait's " \
           "companies or she does not stand to gain any dividends, she will place a special interest cube instead.\n"


def call_dividends_action_be_performed_text():
    return "Do the dividend cubes exist in the bag or does Cait stand to gain money? Y/N "
