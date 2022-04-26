# Program collects score listed
# April 24,2022
# CTI-110 P5HW1 - Score List
# Marcel Brown
#
# Create a function that collects and stores valid scores 
# Create another function to drop the lowest score, determines the average score and letter grade 
# Program add scores to a list 
# Program determine lowest score
# Program drop lowest score 
# Program calculates average score
# Print Lowest score, Modified list, Scores Average and Grade
# Create a menu that allows user to create and view the list of score created  
#

def collect_scores(scores):
    total_score=[]
    for i in range(1,scores+1):
        score=int(input(f'Enter Score #{i}: '))
        if score>=0 and score<=100:
            total_score.append(score)
        else:
            while score<0 or score>100:
                print('INVALID Score entered!!!!')
                print('Score should be between 0 and 100')
                score=int(input(f'Enter Score #{i}: '))
    return total_score
def results(total_score):
    print('--------------Results----------------')
    lowest_score = min(total_score)
    print('Lowest Score  :',lowest_score)
    total_score.remove(lowest_score)
    print('Modified List :',total_score)
    score_avg=sum(total_score)/len(total_score)
    print('Scores Average:',f'{score_avg: .2f}')
    
    if score_avg>=90:
        grade = 'A'
    elif score_avg>=80:
        grade = 'B'
    elif score_avg>=70:
        grade = 'C'
    elif score_avg>=60:
        grade = 'D'
    else:
        grade = 'F'

    print('Grade         :',grade)
    print('-------------------------------------------')

    return results

for i in range(1,2,3):
    print('-----------MENU-------------')  
    print('1) Create Score List')  
    print('2) Display Results')  
    print('3) Exit')
    print('-----------------------------')
    print('')
    choice1 = int(input('Enter Choice:'))
    
  
    if choice1 == 1:
        num_score=int(input('How many scores do you want to enter? '))
        total_score=collect_scores(num_score)
        print('')
        print('-----------MENU-------------')  
        print('1) Create Score List')  
        print('2) Display Results')  
        print('3) Exit')
        choice2 = int(input('Enter Choice:'))  
  
        if choice2 == 2:
            results(total_score)
            
              
        elif choice3 == 3:
            print('Program terminating....')
            print('Good Bye!')

            break  
              
        
    else:  
        print('INVALID choice entered !!!!!')
        print('Choose from menu options please')  
