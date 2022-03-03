# CTI-110
# P2HW2 - Score Avg
# Marcel Brown
# Mar 01, 2022
#
# Have user give a series of 7 scores 
# Program determine lowest score
# Program drop lowest score 
# Program calculates average score
# Print Lowest score, Modified list and Scores Average
#

score_1 = float(input('Enter score #1: '))
score_2 = float(input('Enter score #2: '))
score_3 = float(input('Enter score #3: '))
score_4 = float(input('Enter score #4: '))
score_5 = float(input('Enter score #5: '))
score_6 = float(input('Enter score #6: '))
score_7 = float(input('Enter score #7: '))

all_scores = [score_1, score_2, score_3, score_4, score_5, score_6, score_7]

lowest_score = min(all_scores)

all_scores.remove(lowest_score)

scores_average = sum(all_scores) / 6 






print('--------------Results-----------')

print ('Lowest Score : ' ,f'{lowest_score:}')
print ('Modified_list : ', f'{all_scores:}')
print ('Scores Average : ' ,f'{scores_average : .2f}')

print ('--------------------------------')
