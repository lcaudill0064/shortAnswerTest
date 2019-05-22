def main():
    study_qs_list = studyQs()
    study_as_list = studyAs(study_qs_list)
    correct_as_list = correctAs()
    correct_checker(correct_as_list, study_as_list, study_qs_list)


def studyQs():
    question = []
    indexer = 0
    questions = open("File Path", "r").readlines()
    questions = [q.strip() for q in questions]
    for quest in range(len(questions)):
        indexer += 1
        question.append(questions[quest])

    return question 


def studyAs(study_qs_list):
    answer = []
    count = 0
    for answers in range(len(study_qs_list)):
        print(study_qs_list[answers])
        count += 1
        answerEntered = input(": ")
        print()
        print("--------------------------------------------------------------------------------")
        print()
        answer.append(answerEntered)

    return answer


def correctAs():
    correct = []
    index = 0
    correct_answers = open("File Path", "r").readlines()
    correct_answers = [answer.strip() for answer in correct_answers]
    for items in range(len(correct_answers)):
        index += 1
        correct.append(correct_answers[items])

    return correct

def correct_checker(correct_as_list, study_as_list, study_qs_list):
    counter = 0
    for item in range(len(study_as_list)):
        if study_as_list[item] == correct_as_list[item]:
            counter += 1
            print("Correct!")
            print()
            print("----------------------------------------------")
        else:
            print("Incorrect answer")
            print(study_qs_list[item])
            print("Your answer: ",study_as_list[item])
            print("Correct answer: ",correct_as_list[item])
            print()
            print("----------------------------------------------")

    total = counter / 97
    total = int(total * 100)
    print("You scored: ",counter,"out of: ",97)
    print("Or: ", total, "%", sep='')

main()
