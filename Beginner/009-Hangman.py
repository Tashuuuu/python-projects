import random
word_list = ["secret", "hey", "tomato", "house", "rainbow"]

word = random.choice(word_list)
turns = 5
right_ans = set()
all_ans = ""
print(f"Guess the correct word. It has {len(word)} letters.")
while turns > 0:
  ask = input("Guess a character: ")
  all_ans += ask
  for i in word:
    if i in all_ans:
      print(i, end = " ")
      right_ans.add(i)
    else:
      print("_", end = " ")
  if ask not in word:
    turns = turns - 1
    print("\nWrong guess!")
    print(f"You have {turns} attempts left.")
  if turns == 0:
    break
  if right_ans == (q:=set(word)):
    print(f"\nThe word was \'{word}\'. You guessed it right.")
    print("Yay!\nYou won!")
    break
if right_ans != q:
  print("You lost.")
