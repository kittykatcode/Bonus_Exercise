import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)
for question in data:
    print(question['question_text'] + '?')
    for index, option in enumerate(question['alternatives']):
        print(index +1 , '-' , option)
    user_choice = int(input('Enter your ans - '))
    
    question['user_ans']= user_choice
score = 0
for index, question in enumerate(data):
    if question['correct_ans'] == question['user_ans']:
        score = score+1
        result = 'Correct Ans'
    else:
        result = 'WRONG ANS'

    message = f"{index +1} : {result}  - your ans was, {question['user_ans']} and the correct ans is {question['correct_ans']}"
    print(message)

print('Your score is ' ,score, 'out of ', len(data))
print(data)


