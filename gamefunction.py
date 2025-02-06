def deathLogic(response, memory, summary):
    if "DEAD-GAME-OVER" in response:
        deathstate = 1
        while deathstate == 1:
            print("You have met an unfortunate end have you not? Would you like to leave or try-again from scratch?")
            choice = input("Type quit to quit or restart to restart\n>> ")
            if choice == "quit":
                exit()
            elif choice == "restart":
                memory = ""
                summary = ""
                deathstate = 0
            else:
                pass