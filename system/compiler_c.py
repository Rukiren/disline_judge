from subprocess import call
import os


def cppCompiler(question, test):
    
    test_path = test
    in_path = f'system/compile/{question}/question.in'
    out_path = f'system/compile/{question}/out.txt'
    err_path = f'system/compile/{question}/err.txt'
    ans_path = f'system/compile/{question}/question.out'

    os.system(f"gcc -o test {test_path}")

    call('./test', 
        stdin=(open(in_path)), 
        stdout=(open(out_path, 'w')), 
        stderr=(open(err_path, 'w')))

    try:
        with open(out_path) as f:
            out = f.read()
    except:
        print('output test can not be found')    

    with open(ans_path) as f:
        ans = f.read()
        
    err = None
    if out == ans:
        state = "ac"
        return state, ans, out, err
    else:
        state = "error"
        with open(err_path) as f:
            err = f.read()
        return state, ans, out, err
        
