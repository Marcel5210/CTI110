# Fix the program
# Mar 19,2022
# CTI-110 P3HW1-Debugging
# Brown Marcel
#




def main():
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    

    score = int(input('Please enter score: '))

    if score >= A_score:
        print('Grade is A.')

    elif score >= B_score:
        print('Grade is B.')
    elif score >= C_score:
        print('Grade is C.')
    elif score >= D_score:
        print('Grade is D.')

    else:
        print('Grade is F.')
main()
