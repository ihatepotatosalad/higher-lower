import random
import data
import os

def play_game():
    score = 0
    in_session = True
    while in_session:
        
        choice_a = random.choice(data.data)
        choice_b=random.choice(data.data)

        while choice_a == choice_b:
            choice_a = random.choice(data.data)
            choice_b=random.choice(data.data)

        
        print(f'Score: {score}')
        print(f'compare A: {choice_a["name"]}: {choice_a["description"]} from: {choice_a["country"]} ')
        print('VS')
        print(f'compare B: {choice_b["name"]}: {choice_b["description"]} from: {choice_b["country"]}')
        answer = max(choice_a["follower_count"],choice_b["follower_count"])


        user_pick = input('Who has more followers A or B: ')
        if user_pick == 'a':
            pick = choice_a["follower_count"]
        else:
            pick = choice_b["follower_count"]
        if pick == answer:
            score+=1
            print('correct')
            os.system('cls')
        else:
            in_session = False
            print(f'wrong you lose final score: {score}')
    

play_game()