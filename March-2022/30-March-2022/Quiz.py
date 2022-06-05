print('Welcome to school Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is your percentile?')
    if answer.lower()=='90':
        score += 1
        print('good')
    else:
        print('Bad :(')
 
 
    answer=input('Question 2: Do you follow any Mentor? ')
    if answer.lower()=='yes':
        score += 1
        print('Good')
    else:
        print('Bad :(')
 
    answer=input('Question 3: What is the name of your favourite Book?')
    if answer.lower()=='book':
        score += 1
        print('good')
    else:
        print('bad :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')