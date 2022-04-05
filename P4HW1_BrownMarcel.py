
# CTI-110
# P4HW1 - Score List
# Marcel Brown 
# April 2,2022
#
# Have user give a series of scores
# Program collects scores entered and determines if valid
# Program add scores to a list 
# Program determine lowest score
# Program drop lowest score 
# Program calculates average score
# Print Lowest score, Modified list, Scores Average and Grade

num_scores=int(input('How many scores do you want to enter? '))
print()
i = 1
total_score=[]


while i<=num_scores:
    print('Enter score #{}: '.format(i), end= '')
    score = float(input())
    
    if score<0 or score>100:
        print()
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')

    else:
        total_score.append(score)
        i+=1 

lowest_score = min(total_score)
total_score.remove(lowest_score)
score_avg=sum(total_score)/len(total_score)

if score_avg>=90:
    grade = 'A'

elif score_avg>=80:
    grade = 'B'

elif score_avg>=70:
    grade = 'C'

else:
    grade = 'F'

print()
print()

print('--------------Results-----------')
print('Lowest Score  :',lowest_score)
print('Modified List :',total_score)
print('Scores Average:',f'{score_avg: .2f}')
print('Grade         :',grade)
print('-----------------------------------')

    


    






    


    




