print("Welcome to out blind auction!")

bids = {}
more = ""

while more != "n":
  name = input("Please tell us your name: ")
  bid_value = float(input("What is your bidding price? $"))
  more = input("Is there any other bidder? [y/n] \n ")
  bids[name] = bid_value

highest_bid = 0
highest_bidder = ""

for name, bid_value in bids.items():
  if bid_value > highest_bid:
    highest_bid = bid_value
    highest_bidder = name

print(f"The winner of this aucition is {highest_bidder.capitalize()} with the bid of ${highest_bid} ")
