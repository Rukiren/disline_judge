from subprocess import call

test_path = "test.py"
in_path = 'compile/in.txt'
out_path = 'compile/out.txt'
err_path = 'compile/err.txt'
ans_path = 'compile/ans.txt'

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
        out = f.readlines()
except:
    print('output test can not be found')    

with open(ans_path) as f:
    ans = f.readlines()
    

if out == ans:
    print("AC")
else:
    print('ans: ')
    print(ans)
    print("your output: ")
    print(out)
    with open(err_path) as f:
        err = f.readline()
    print(err)
    
