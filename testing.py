import random

questions_div = ["#q1", "#q2", "#q3", "#q4", "#q5", "#q6", "#q7", "#q8"]
num_questions = len(questions_div)
num_done = 0

while (num_done < num_questions):
    id1 = random.randint(0, (num_questions-1) - num_done)
    id2 = random.randint(0, (num_questions-1) - num_done)
    
    while (id2 == id1):
        id2 = random.randint(0, (num_questions-1) - num_done)

    print id1
    print id2

    item1 = questions_div.pop(id1)
    item2 = questions_div.pop(id2)
    num_done += 2    

    print "SWAP {0} with {1}".format(item1, item2)



