high_scores = [['Ben Jammin', 0], ['Grackus Rex', 0], ['Kelsir', 0], ['Vin', 0], ['The Governator', 0]]

def update_high_scores(new_score):
    
    for position in high_scores:
        if new_score[1] > position[1]:
            high_scores.insert(high_scores.index(position), new_score)
            print('\nCongrats on making the top 5!\n')
            if len(high_scores) > 5:
                high_scores.pop(5)
            break
        elif new_score[1] == position[1]:
            high_scores.insert((high_scores.index(position)+1), new_score)
            print('\nCongrats on making the top 5!\n')
            if len(high_scores) > 5:
                high_scores.pop(5)
            break
        else:
            print('\nTry again for a top score!\n')
    print('\n')
    for position in high_scores:
        print(position)

    with open("high_scores.txt", "w") as score_doc:
        for score in high_scores:
            score_doc.writelines(str(score) + "\n")

        
    
name = input('Greetings friend! What is your name?\n')
score = int(input('What was your score?\n'))

update_high_scores([name, score])
print('\nthis works\n')
            

""" class Player:

    def welcome():
        player_name = input('Greetings friend! What is your name?')
 """    