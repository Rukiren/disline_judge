from subprocess import call


def pythonCompiler(question, test):
    test_path = test
    in_path = f'system/compile/{question}/question.in'
    out_path = f'system/compile/{question}/out.txt'
    err_path = f'system/compile/{question}/err.txt'
    ans_path = f'system/compile/{question}/question.out'
    try:
        call(['python3',test_path], 
            stdin=(open(in_path)), 
            stdout=(open(out_path, 'w')), 
            stderr=(open(err_path, 'w')))
    except:
        print('compile failed')
        BrokenPipeError

    try:
        with open(out_path) as f:
            out = f.read()
    except:
        print('output test can not be found')    

    with open(ans_path) as f:
        ans = f.read()
        

    if out == ans:
        print("AC")
    else:
        print('ans: ')
        print(ans)
        print("your output: ")
        print(out)
        with open(err_path) as f:
            err = f.read()
        print(err)
        
