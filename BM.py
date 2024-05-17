def main():
    print("                                                          Welcome to the challenge where you fail, you die!")
    player_name = input("Enter your name... or die: ")
    print(f"                                                         Hello, {player_name}! Let's start.")
    
    # Starting point of the game
    print("                                                          There are two parts to this challenge, the is the first part, trivia! Do you wish to continue?")
    
    first_choice = input("Yes or No? (Yes/No): ")
    
    
    if first_choice.lower() == "yes":
        hehe()
    else:
        print("                                                      Aww, guess I'll see you next time... ")
        print("                                                      Or is there a next time?")
        return


def hehe():
    print("                                                          Okay, brave warrior, you shall continue.")
    print("                                                          First question..")
    riddle_answer = input("                                          What has keys but can't open locks? ")

    if riddle_answer.lower() == "piano":
        print("                                                      Correct! Wait, is this too easy for you?")
    elif riddle_answer.lower() == "keyboard":
        print("                                                      Correct! Wait, is this too easy for you?")
    else:
        print("                                                      Wrong answer. Better luck next time... Corpse!")
        return
    print("                                                          Guess I really need to come up with some harder ones... Anyways, second question..")
    riddle_answer = input("                                          I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? ")
    if riddle_answer.lower() == "echo":
        print("                                                      Really bro? Imma die if u get one more.")  
    else:
        print("                                                      Wrong answer. Better luck next time.... Hehe")
        return
    print("Third question")
    print("Actually, u pass! Time to go to the next part of the challenge, its a gimkit!")
    
if __name__ == "__main__":
    main()
