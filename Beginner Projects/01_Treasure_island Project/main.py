print(r'''            _
         -._ \'.
          \ '.\_\_
       _.--'  _   '.---.
      /._   _<_)/)/ .-'
      _.-'- ([d,p]? _.-       .;
       '--.'-\ _ /-'--      .:'
         __  )'-'(  __    .:'
      .-/  ]' -Y- '[ /\ _:'
     /\|  | -----/ | ,r |
     |  ,\  \'= /'  .:\ "(
     | / /\; \,/  .:'  |_|
     \ _ )<   /  :' \ /__|
      '__\ {---:'-/  \(  )
      \_ _|/_:'-__]   '-'
        ) .:'    \ \
       (L:/  ;      \
      .:~'   |  .   7
    .:'  /   \   ' /\
  .;'    |\ . |;     )
 ;'      | '  |\'. _/|
         /'.' (\\..  |
        ( \. ,|\ '   /
        |\_  / \ ': /\
        \    | |\  __/
        |\   )  \,___>
        <-'-/    \'  |
        |_ /      |=j|
     _.-' /       \  (
snd '-----'        \  \
                    '-'
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Choose carefully! 🫡")

choice0 = input("Do you want to go left or right?\n").upper().strip()

if choice0 == "LEFT":
    print("You fell into a pit of snakes. Better luck next time!")
    print("YOU DIED! 🫡")

elif choice0 == "RIGHT":
    print("After moving forward, you reach the sea and can see Treasure Island in the distance.")

    choice1 = input(
        "Do you want to wait and figure out another way, or swim across? "
        "(wait or swim)\n"
    ).upper().strip()

    if choice1 == "SWIM":
        print("Your greed was your killer.")
        print("You tried to swim across and ended up in a sea monster's belly.")
        print("YOU DIED! 🫡")

    elif choice1 == "WAIT":
        print("You waited for some time, saw a sea monster, and backed away from the sea.")

        choice2 = input(
            "After investigating, you find two possible ways forward: "
            "an old underwater tunnel or an abandoned plane. "
            "(plane or tunnel)\n"
        ).upper().strip()

        if choice2 == "PLANE":
            print("You tried to reach the island using the plane...")
            print("But it didn't even start and exploded while you were inside. 😂😂😂")
            print("YOU DIED! 🫡 You got so close to the treasure.")

        elif choice2 == "TUNNEL":
            print("You reached the island through the tunnel.")
            print("You finally found the treasure!")
            print("But there was a highly poisonous white snake inside the treasure box.")
            print("You opened the box, and it bit you. 😂😮‍💨")
            print("YOU DIED! 🫡")

        else:
            print("You couldn't decide where to go and got lost.")
            print("YOU DIED! 🫡")

    else:
        print("You waited too long to make a decision.")
        print("YOU DIED! 🫡")

else:
    print("Wrong choice. The island doesn't forgive hesitation.")
    print("YOU DIED! 🫡")