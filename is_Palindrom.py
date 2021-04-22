"""
Palindrom : 회문 ( 앞에서부터 읽는 것과 뒤에서부터 읽는 것이 동일한 단어나 문장 )
띄어쓰기나 문장부호 무시. 대문자 소문자 구분 X
"""
s = input("문자열 입력:"); is_Palindrom = 1
for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        is_Palindrom = 0

if is_Palindrom == 1:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

