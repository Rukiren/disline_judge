from subprocess import call
import os


def cppCompiler(question, test):
    
    # 獲取相關路徑
    test_path = test
    in_path = f'system/compile/{question}/.in'  # 正確輸入
    ans_path = f'system/compile/{question}/.out'  # 正確輸出
    out_path = f'system/test/out.txt'   # 測試檔案輸出結果
    err_path = f'system/test/err.txt'   # 測試檔案錯誤資訊

    os.system(f"gcc -o test {test_path}") # 執行測試

    call('./test', 
        stdin=(open(in_path,encoding="utf-8")), 
        stdout=(open(out_path, 'w',encoding="utf-8")), 
        stderr=(open(err_path, 'w',encoding="utf-8")))

    try:
        with open(out_path,encoding="utf-8") as f:
            out = f.read()
    except:
        print('output test can not be found')    

    with open(ans_path,encoding="utf-8") as f:
        ans = f.read()
        
    err = None
    if out == ans:
        state = "ac"
        return state, ans, out, err
    else:
        state = "error"
        with open(err_path,encoding="utf-8") as f:
            err = f.read()
        return state, ans, out, err
        
