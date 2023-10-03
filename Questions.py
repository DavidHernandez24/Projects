score = 0

questions = [
    'How many times a month do you eat pizza? (a) more than 3 times (b) 1-2 times (c) I seldom eat pizza: ',
    'How many slices of pizza do you eat? (a) 4 (b) 3-2 (c) 1: ',
    'Which is your favorite pizza? (a) Hawaiian (b) Meat pizza (c) I have no preference: ',
    'If you order something online, the first thing you think of ordering is pizza? (a) Yes (b) Sometimes (c) No, it depends: ',
    'Is pizza your favorite fast food? (a) Yes (b) No, but I like to eat it (c) No, I prefer other fast food: '
]

for question in questions:
    while True:
        answer = input(question)
        if answer in ("a","b","c"):
            break
    if answer == "a":
        score += 3
    elif answer == "b":
        score += 2
    else:
        score += 1

if score >= 12:
    score = "You love Pizza"
elif score >= 7:
    score = 'You kinda like Pizza'
else:
    score = 'You don\'t like Pizza at all'

print(score)
