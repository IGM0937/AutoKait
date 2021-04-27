def welcome_text():
    res = '\n'
    res += "Welcome to AutoCait."
    res += '\n'
    res += "Let's play Irish Gauge!"
    res += '\n'
    res += "Please setup the game and proceed when completed..."
    res += '\n'
    return res


def exit_text(forced, msg='Goodbye'):
    return f"Forced exit... {msg}" if forced else msg


def cait_waiting_turn_text():
    return "Type bid, tracks or dividend or press enter to take Cait's turn... "


def cait_turn_text():
    return "Cait would like to..."


def invalid_input(text='Try again'):
    return f"Invalid input, {text}.\n"


def special_interest_action_text():
    return f"{cait_turn_text()} Place a special interest cube\n"


def special_interest_action_explain_text():
    res = '\n'
    res += "Place a special interest cube for the company Cait has the most share value, prioritising companies " \
           "it owns first. In case of a tie, place for the company Cait owns that has the most trains on the map."
    res += '\n\n'
    res += "Choose a colour that isn't present on that trainline yet. If there are multiple colours, choose at random."
    res += '\n\n'
    res += "When deciding on which city to place the cube, select from the following list:"
    res += '\n'
    res += "    - Towns occupied by 2+ of Cait's trains"
    res += '\n'
    res += "    - Towns occupied by 1 of Cait's trains"
    res += '\n'
    res += "    - Towns occupied by 2 different player's trains"
    res += '\n'
    return res


def special_interest_action_be_performed_text():
    return "Can Cait place any special interest cubes? Y/N "


def place_tracks_action_text():
    return f"{cait_turn_text()} Place rail tracks\n"


def place_tracks_others_action_text():
    return "Placing rail tracks\n"


def place_tracks_action_explain_text():
    res = '\n'
    res += "Place trains for the company that Cait owns, but has the least trains on the map. " \
           "If tied, place for the company with the biggest combined share value."
    res += '\n\n'
    res += "Build towards the closest Town or City."
    res += '\n\n'
    res += "If tied, follow the rule: City (with special interest not present on track) -> City -> Town"
    res += '\n'
    return res


def call_auction_action_text():
    return f"{cait_turn_text()} Call an auction action\n"


def call_auction_action_explain_text():
    res = '\n'
    res += "Perform an auction on a share for a company that currently has the most connections to Towns or Cities. " \
           "If tied, pick the share with the lowest face value."
    res += '\n\n'
    res += "If Cait does not have enough money for that share, she performs Call for Dividends instead."
    res += '\n\n'
    res += "If Cait is in the bidding war, she will determine the maximum bid based on:"
    res += '\n\n'
    res += "    (minimum company share + d10 dice roll) capped at Cait's overall money available"
    res += '\n\n'
    res += "Cait will raise the bid at random by from £1 to £3 at a time. She will pass if she is unable to raise " \
           "the bid or is unable to got bid past the funds of her maximum bid for the share."
    res += '\n'
    return res


def call_auction_action_be_performed_text():
    return "Can Cait auction the specific share? Y/N "


def place_bid_action_text():
    return "Cait is participating in bids\n"


def place_bid_action_explain_text():
    return "\nParticipate in bidding by following the instructions. Type 'back' to back out of bidding.\n"


def ask_company_minimum_share_price():
    return "Please input the minimum share price of the company being actioned... £ "


def ask_current_bid_price():
    return "Please input the current bid price £ "


def cait_bid_bidding_text(bid):
    return f"Cait is bidding £{bid}\n"


def cait_bid_winning_question_text():
    return "Did Cait win the share or is there a new bid? Y/£ "


def cait_bid_won_text(bid, new_total):
    return f"Cait has won the bid at £{bid}, she now has £{new_total} left.\n"


def cait_bid_passing_text():
    return "Cait is passing\n"


def call_dividends_action_text():
    return f"{cait_turn_text()} Call for dividends\n"


def call_dividends_action_explain_text():
    return "\nIn the event where there are no dividend cubes in the bag with the same colours owned by Cait's " \
           "companies or she does not stand to gain any dividends, she will place a special interest cube instead.\n"


def call_dividends_action_be_performed_text():
    return "Do the dividend cubes exist in the bag or does Cait stand to gain money? Y/N "


def reward_dividends_text():
    return "How much dividends has Cait won? £ "


def cait_wallet_update_text(dividend, new_total):
    return f"Cait has won £{dividend} in dividends, she now has £{new_total}.\n"
