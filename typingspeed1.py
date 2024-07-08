from time import time

# Calculating the accuracy of the input prompt
def accuracy(prompt, inprompt):
    words = prompt.split()
    inwords = inprompt.split()
    errors = 0
    
    for i in range(min(len(words), len(inwords))):
        if words[i] != inwords[i]:
            errors += 1
    
    # Add any remaining words as errors
    errors += abs(len(words) - len(inwords))
    
    return errors

# Calculating the typing speed per minute
def speed(inprompt, elapsed_time):
    words = inprompt.split()
    twords = len(words)
    speed = twords / (elapsed_time / 60)
    return speed

# Calculating the total elapsed time
def elapsed_time(stime, etime):
    return etime - stime

if __name__ == '__main__':
    prompt_text = "The quick brown fox jumps over the lazy dog."
    print("Type the following: ", prompt_text)

    input("Press Enter when you are ready to test your speed!!!")

    stime = time()
    inprompt = input("")
    etime = time()

    # Collect all information returned by the functions
    elapsed = round(elapsed_time(stime, etime), 2)
    typing_speed = round(speed(inprompt, elapsed), 2)
    error_count = accuracy(prompt_text, inprompt)

    # Print all the required data to see the result
    print("Your Average Typing Speed was ", typing_speed, "Words per minute (wpm)")
    print("You made ", error_count, "Errors")
