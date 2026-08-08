# This program calculates the grades for students based on their average scores in ENG, Maths, Science

S = {"AMIT": [92, 86, 64], "NAGMA": [65, 42, 43], "DAVID": [92, 90, 88]}

for key in S:
    scores = S[key]
    total_score = sum(scores)
    average_score = total_score // len(scores)
    
    if average_score >= 90:
        print(key, "-", "A")
    elif average_score >= 60:
        print(key, "-", "B")
    else:
        print(key, "-", "C")