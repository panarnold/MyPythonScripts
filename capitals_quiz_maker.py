#! python
# it makes quiz with questions and answers in a random order.
# it also generates correct answers' list with proper key
# X 2020 Arnold Cytrowski

import random, os

capitals = {'Poland' : 'Warsaw', 'Spain' : 'Madrid', 'Germany' : 'Berlin',
'Portugal' : 'Lisbona', 'Austria' : 'Vienna', 'Czech Republic' : 'Prague',
'France' : 'Paris', 'USA' : 'Washington', 'Norway' : 'Oslo', 'England' : 'London',
'Afghanistan' : 'Kabul', 'UAE' : 'Abu Dhabi', 'Greece' : 'Athens',
'Switzerland' : 'Bern', 'Colombia' : 'Bogota', 'Russia' : 'Moscow',
'Brasil' : 'Brasillia', 'Hungary' : 'Budapest', 'Italy' : 'Rome',
'Egypt' : 'Cairo', 'Syria' : 'Damascus'}

for quizNum in range(1,15):
    
    pathname1 = '.\\quiz'
    pathname2 = '.\\answers'

    if not os.path.exists(pathname1):
        os.mkdir(pathname1)
    if not os.path.exists(pathname2):
        os.mkdir(pathname2)

    quizFile = open('.\\quiz\\capitalsquiz%s.txt' % quizNum, 'w+')
    answer_key_file = open('.\\answers\\capitalsquiz_answers%s.txt' % quizNum, 'w+')

    quizFile.write('Name:\nData:\nClass:\n')
    quizFile.write((' ' * 20) + 'quiz Know Capitals of Countries (quiz %s)' % quizNum)
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for question_num in range(1, len(capitals)):
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        quizFile.write('%s. What is the capital of %s?\n' % (question_num, states[question_num]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answer_options[i]))
        quizFile.write('\n')

        answer_key_file.write('%s. %s\n' % (question_num, 'ABCD'[answer_options.index(correct_answer)]))
        
    quizFile.close()
    answer_key_file.close()


