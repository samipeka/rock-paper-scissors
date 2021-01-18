rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



import random
human_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")


horizontal = int(human_choice) 
if horizontal >=3:
  print("You chose invalid number, you lose.")
else:
  if horizontal == 0:
    print(f"You played rock.\n {rock}")
  elif horizontal == 1:
    print(f"You played paper.\n {paper}")
  elif horizontal == 2:
    print(f"You played scissors.\n {scissors}")

  #comp_choice
  vertical = random.randint(0, 2) 

  if vertical == 0:
    print(f"Computer played rock.\n {rock}")
  elif vertical == 1:
    print(f"Computer played paper.\n {paper}")
  elif vertical == 2:
    print(f"computer played scissors.\n {scissors}")

# # Need to make a nested list.
  row1 = ["draw", "human", "computer"] 
  row2 = ["computer", "draw", "human"]
  row3 = ["human", "computer", "draw" ]
  map = [row1, row2, row3]
  # # if selected field is "x" then print it's draw, if selected field "human" then print Human won
  selected_field = map[vertical][horizontal]

  if selected_field == "draw":
    print("It's a draw.")
  elif selected_field == "computer":
      print("Computer wins.")
  else:
    print("YOU win!")
