def printQuestion(question):
    question_path = f'system/questions/{question}/questionText.txt'
    examplequestion = f'system/questions/{question}/example.txt'
    ques_txt = None
    ques_test = None
    with open(question_path ,encoding="utf-8") as f:
        # 把每行文本結尾添加 \n
        ques_txt = f.read().replace('\n', '') + '\n'

    with open(examplequestion ,encoding="utf-8") as f:
        # 把每行文本結尾添加 \n
        ques_test = f.read().replace('\n', '') + '\n'
    
    return ques_txt, ques_test
