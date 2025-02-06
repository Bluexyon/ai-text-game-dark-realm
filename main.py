import llm_generation
import gamefunction

systemcontext = ""
memory = ""
summary = ""
memorycycle = 0

try:
    with open('ai-text-game/expansions/expansion.context', 'r') as file:
        line = file.readline()
        while line:
            #print(line.strip())  # `strip()` removes newline characters
            systemcontext += line
            line = file.readline()
except FileNotFoundError:
    print("Context Missing: the context file was not found")
except PermissionError:
    print("Permission Error: You do not have permission to access the context file")
except Exception as e:
    print(f"An unexpected error occured: {e}")
finally:
    file.close()


if __name__ == '__main__':
    print(r"""
$$$$$$$\   $$$$$$\  $$$$$$$\  $$\   $$\       $$$$$$$\  $$$$$$$$\  $$$$$$\  $$\       $$\      $$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |      $$  __$$\ $$  _____|$$  __$$\ $$ |      $$$\    $$$ |
$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |$$  /       $$ |  $$ |$$ |      $$ /  $$ |$$ |      $$$$\  $$$$ |
$$ |  $$ |$$$$$$$$ |$$$$$$$  |$$$$$  /        $$$$$$$  |$$$$$\    $$$$$$$$ |$$ |      $$\$$\$$ $$ |
$$ |  $$ |$$  __$$ |$$  __$$< $$  $$<         $$  __$$< $$  __|   $$  __$$ |$$ |      $$ \$$$  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$$\        $$ |  $$ |$$ |      $$ |  $$ |$$ |      $$ |\$  /$$ |
$$$$$$$  |$$ |  $$ |$$ |  $$ |$$ | \$$\       $$ |  $$ |$$$$$$$$\ $$ |  $$ |$$$$$$$$\ $$ | \_/ $$ |
\_______/ \__|  \__|\__|  \__|\__|  \__|      \__|  \__|\________|\__|  \__|\________|\__|     \__|
""")
    
    print("Version 0.1b\nQuit the Program by typing exit, quit or end.")
    print("To start the game try asking where you are.")

    while True:
        try:
            
            userquery = input(">> ")
            if not userquery:
                pass
            else:
                match userquery:
                    case "exit":
                        break
                    case "quit":
                        break
                    case "end":
                        break
                    case _:
                        if memorycycle != 5:
                            print("loading...")
                            memorycycle = memorycycle+1
                            response = llm_generation.generateInstruction(systemcontext,userquery,summary,memory)
                            print("-------------GAME MASTER--------------\n")
                            print(response.strip() + "\n")
                            memory += "User: "+ userquery +"\nGame Master:"+ response.strip()

                            gamefunction.deathLogic(response, memory, summary)
                        else:
                            memorycycle = 0
                            print("loading...")
                            summary = llm_generation.generateSummary(summary, memory)
                            memory = ""
                            response = llm_generation.generateInstruction(systemcontext,userquery,summary,memory)
                            print("-------------GAME MASTER--------------\n")
                            print(response.strip() + "\n")
                            memory += " User: "+ userquery +"\nGame Master:"+ response.strip()

                            gamefunction.deathLogic(response, memory, summary)
        except Exception as e:
            raise e
        finally:
            pass