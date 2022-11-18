def questionOut(question):
    question_path = f'system/compile/{question}/questionText.txt'
    examplequestion = f'system/compile/{question}/example.txt'
    with open(question_path) as f:
        ques_txt = f.read()
    print(ques_txt)


    with open(examplequestion) as f:
        ques_txt = f.read()
    print(ques_txt)
