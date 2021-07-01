import random

# Dictionary of questions and answers

questions = {
            'Where is the Mount Everest?':
            ('\na. China\nb. Russia\nc. The United States\nd. India\n', 'd'),
            'What is the capital of India?':
            ('\na. Zimbabwe\nb. New York\nc. Delhi\nd. Panama', 'c'),
            'How many Planets are there in the Solar System':
            ('\na. Nine\nb. Eight\nc. Six\nd. Seven', 'b')
            }

def ask_question(questions):
    '''Asks random questions mentioned in the dictionary'''

    item = random.choice(list(questions.items()))
    question = item[0]
    (variants, answer) = item[1]
    print(question, variants)
    attempt = input('\nHit \'a\', \'b\', \'c\' or \'d\' for your answer\n')
    return (attempt, answer)

# Questions loop
tries = 0
for questions_number in range(4):
    while True: 
        attempt, answer = ask_question(questions)
        if attempt not in {'a', 'b', 'c', 'd'}:
            print('INVALID INPUT!!! ')
        elif attempt == answer:
            print('Correct')
            stop_asking = False
            break
        elif tries == 1: # Specify the number of tries to fail the answer        
            print('Incorrect!!! You ran out of your attempts')
            stop_asking = True
            break
        else:
            tries += 1
            print('Incorrect!!! Try again.')
    if stop_asking:
        break
