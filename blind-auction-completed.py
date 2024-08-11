logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bid_continus = False
dict_bids = {}

while not bid_continus :
    
    name = input("What is your name? : ")
    bid = input("What is your bid? : $")

    dict_bids[name] = bid
    
    other_biders = input("is there are other users who want to bid? Type 'Yes' or 'No' : ").lower()

    if other_biders == "no" :
        the_highest_bid = 0
        Winner = ""

        for bidder in dict_bids :

            Bid = int(dict_bids[bidder])
            if Bid > the_highest_bid :
                the_highest_bid = Bid
                Winner = bidder

        print(f"The Winner is {Winner}!! with a bid of ${the_highest_bid}")
        bid_continus = True
        
    else :
        print('\n' * 100)

