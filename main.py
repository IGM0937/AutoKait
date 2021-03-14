import random


def special_interest_action():
    print("""
    SPECIAL INTEREST CUBE ACTION
    
    Place a special interest cube for the company Cait has the most share value, prioritising companies it owns first. In case of a tie, place for the company Cait owns that has the most trains on the map.
    
    Choose a colour that isn't present on that trainline yet. Choose the cubes at random.
    
    When deciding on which city to place the cube, select from the following list
        * Towns occupied by 2+ of Cait's trains
        * Towns occupied by 1 of Cait's trains
        * Towns occupied by 2 different player's trains
    """)


def place_tracks_action():
    print("""
    PLACE RAIL TRACKS ACTION
    
    Place trains for the company that Cait owns, but has the least trains on the map. If tied, place for the company with the most share value.
    
    Build towards the closest Town or City. If tied, follow the rule: City with special interest not present on line > City > Town
    """)


def call_auction_action():
    print("""
    CALL AN AUCTION ACTION
    
    Perform a blind auction a share for a company that currently has the most connections to Towns or Cities. If tied, pick the share with the lowest face value.
    
    If Cait does not have enough money for that share, she performs Call for Dividends instead.
    
    If Cait is in the bidding war, roll a d10 (9 max) and add the number to the minimum value of share to calculate her maximum bid. The rest of the players choose what their maximum bid as well.
    
    The winner of the share is the player who bid the most, but pays the bid of the second highest bid.
    
    If there is a tie, the player closes to the auctioneer in turn order (including the auctioneer) wins.
    """)
    ask_if_cait_can_auction()


def call_dividends_action():
    print("""
    CALL FOR DIVIDENDS ACTION

    In the event where there are no divident cubes in the bag with the same colours owned by Cait's companies, she will place a special interest cube instead.
    """)
    ask_if_cait_can_call_dividents()


def ask_if_cait_can_auction():
    while True:
        answer = input("\nCan Cait auction the specific share? Y/N").lower()
        if answer == 'y' or answer == 'yes':
            break
        elif answer == 'n' or answer == 'no':
            call_dividends_action()
            break
        else:
            print('Invalid input. Try again. Y/N')
            continue


def ask_if_cait_can_call_dividents():
    while True:
        answer = input("\nDo those dividend cubes exist in the bags?")
        if answer == 'y' or answer == 'yes':
            break
        elif answer == 'n' or answer == 'no':
            special_interest_action()
            break
        else:
            print('Invalid input. Try again. Y/N')
            continue


special_interest_act_range = range(1, 2)
place_tracks_act_range = range(2, 5)
call_auction_act_range = range(5, 6)
call_dividends_act_range = range(6, 7)


def take_turn():
    roll = random.randint(1, 6)

    if roll in special_interest_act_range:
        special_interest_action()
    elif roll in place_tracks_act_range:
        place_tracks_action()
    elif roll in call_auction_act_range:
        call_auction_action()
    elif roll in call_dividends_act_range:
        call_dividends_action()
    else:
        raise Exception("Rolled an impossible roll")
        exit()


def perform_setup():
    pass


def start_event_loop():
    while True:
        current_input = input("Enter when it is Cait's turn... ")
        if current_input == 'exit':
            print('Goodbye')
            exit()
        else:
            take_turn()


if __name__ == '__main__':
    perform_setup()
    start_event_loop()
