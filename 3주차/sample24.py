import random

from dask.array import average

random.seed(42)

scores = dict()
for i in range(10,50):
    scores['S'+ str(i)] = random.randrange(50,100)

total_sum = sum(scores.values())
average_score = total_sum/len(scores)

print(f'평균점수 : {average_score:.2f}')
