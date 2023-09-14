def reset():
    reset_answer = input("Would you like to play again? Type Y for Yes or N for No \n")

    if reset_answer.upper() == "N":
        exit()

    elif reset_answer.upper() != "N" and reset_answer.upper() != "Y":
        reset()

    return reset_answer
