"""
Palindrom : 회문 ( 앞에서부터 읽는 것과 뒤에서부터 읽는 것이 동일한 단어나 문장 )
띄어쓰기나 문장부호 무시. 대문자 소문자 구분 X
"""

def isPalindromSent(s):
    result = ''.join(c for c in s if c.isalnum())
    return isPalindromWord(result)


def isPalindromWord(w):
    w = w.lower()
    print('변환된 문자열:', w)
    for i in range(len(w)//2):
        if w[i] != w[len(w)-1-i]:
            return False
    return True


if __name__ == '__main__':
    s = input('문자열 입력>>')

    if isPalindromSent(s):
        print('회문입니다.')
    else:
        print('회문이 아닙니다.')