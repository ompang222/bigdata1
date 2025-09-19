import random

random.seed(42)

scores = dict()
for i in range(10,50):
    scores['S'+ str(i)] = random.randrange(50,100+1)

    max_score = 0
    top_student =''

    for student_id, score in sorted(scores.items()):
        if score > max_score:
            max_score = score
            top_student = student_id


print(f'최고 득점자 : {top_student}')
print(f'최고 점수 : {max_score}')

