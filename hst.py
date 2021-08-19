import shelve

class Score_Card:
    high_scores = []

    def load_high_scores():
        try:
            hsd = shelve.open('high_scores')
            Score_Card.high_scores = hsd['high_scores']
            hsd.close()

        except:
            Score_Card.high_scores = [['Ben Jammin', 0], ['Grackus Rex', 0], ['Kelsir', 0], ['Vin', 0], ['The Governator', 0]]
            


    def print_scores():
        print('\nHigh Scores!')
        for position in Score_Card.high_scores:
            print(position)
        print('\n')


    def update_high_scores(new_score):
        for position in Score_Card.high_scores:
            if new_score[1] > position[1]:
                Score_Card.high_scores.insert(Score_Card.high_scores.index(position), new_score)
                print('\nCongrats on making the top 5!\n')

                if len(Score_Card.high_scores) > 5:
                    Score_Card.high_scores.pop(5)
                
                break
            
            elif new_score[1] == position[1]:
                Score_Card.high_scores.insert((Score_Card.high_scores.index(position)+1), new_score)
                print('\nCongrats on making the top 5!\n')

                if len(Score_Card.high_scores) > 5:
                    Score_Card.high_scores.pop(5)

                break

        Score_Card.print_scores()

        hsd = shelve.open('high_scores')
        hsd['high_scores'] = Score_Card.high_scores
        hsd.close()