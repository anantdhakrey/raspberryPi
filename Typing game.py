from turtle import *
#typing game for kids. Currently, single digit practice to know the keyboard. then we will join alphabets to increase

import random
import timeit

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits=[0,1,2,3,4,5,6,7,8,9]
jkl=['j','k','l',';']

mylist=digits
minLetters=2
maxLetters=4
ht()
pu()

correct=0
incorrect=0
total=10

start=timeit.default_timer()

for i in range(total):
    lett=''
    for j in range(random.randint(minLetters,maxLetters)):
        lett=lett+str(random.choice(mylist))
        
    randomLetter=lett
    #print(randomLetter)
    setpos(-10,300)
    progressText='Progress: '+str(i+1)+'/'+str(total)
    write(progressText,move=False,align='center',font=('Arial',16))
    
    setpos(0,-100)
    write(randomLetter,move=False,align='center',font=('Arial',180,'bold'))
    myinput=textinput('Word','Write the word')
    if myinput==randomLetter:
        correct+=1
    else:
        incorrect+=1

    clear()
    
setpos(0,0)
end=timeit.default_timer()
totTime=end-start
#print(totTime)

home()
sety(70)
write('Total:  ',True,align='center',font=('Calibri',60,'bold'))
write(total,True,align='center',font=('Calibri',60,'bold'))

home()
write('Correct:  ',True,align='center',font=('Calibri',60,'bold'))
write(correct,True,align='center',font=('Calibri',60,'bold'))

home()
sety(-70)
write('Incorrect:  ',True,align='center',font=('Calibri',60,'bold'))
write(incorrect,True,align='center',font=('Calibri',60,'bold'))

#Scoring shall be done based on the time taken and no of correct and incorrect letters
#Consider that kids take 5 sec for each letter
maxScore=7*total

#-1 for each incorrect entry and +3 for each correct entry0
corScore=correct*7
incorScore=incorrect*(-2)
totScore=round(corScore+incorScore-totTime/4)
if totScore<0 or incorrect>total/4:
    totScore=0

pencolor('red')
home()
sety(200)
write('SCORE:    ',True,align='center',font=('Calibri',100,'bold'))
write(totScore,True,align='center',font=('Calibri',100,'bold'))

exitonclick()
#quit()
