from system.compiler_c import cppCompiler
from system.compiler_py import pythonCompiler
from system.questionOut import printQuestion

while True:
    question = input('選擇題目:')
    try:
        printQuestion(question=question)
    except:
        print("題目不存在")
        break
    test = input('選擇檔案路徑:')
    language = input("選擇語言：\n1 = C/C++ \n2 = python\n")
    if language == '1':
            state = cppCompiler(question=question, test=test)
    elif language == "2" :
            state = pythonCompiler(question=question, test=test)
    print(state[0])