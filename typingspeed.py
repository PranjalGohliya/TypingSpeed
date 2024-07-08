from time import time

from click import prompt 

#Calculating the accuracy of input prompt

def accuracy(prompt, inprompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
           if inwords[i] == words[i]:
                    if(inwords[i+1]) & (inwords[i-1] == words[i-1]):
                     continue
           else:
                errors = errors + 1
    else:
        errors = errors + 1
        return errors
    
    #Calculating the typing speed per minute

    def speed(inprompt, stime, etime):
         global inwords
         global time

         inwords = inprompt.split()
         twords = len(inwords)
         speed = twords / time

         return speed
    
#Calculating the total elapsed time 

def elapsedtime(stime, etime):
     time = etime - stime #start and end times
     return time

if __name__=='__main__':
     prompt = "The quick brown fox jumps over the lazy dog."
     print("Type the following :-" ',prompt,')

     input("Press Enter when you are ready to test your speed!!!")

     stime = time()
     inprompt = input("")
     etime = time()

#Collect all information returned by the functions
     time = round(elapsedtime(stime, etime),2)
     speed = speed(inprompt, stime, etime)
     errors = tperror(prompt)

     #printing all the required data to see the result
     
     print("Your Average Typing Speed was ", speed, "Words per minute(w/m)")
     print("You made ", errors, "Errors")