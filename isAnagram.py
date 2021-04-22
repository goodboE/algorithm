"""
어구전철(Anagram) : 단어나 문장에 있는 철자를 뒤섞어서 다른 의미를 가지는 단어나 문장이 되는 관계
"""

def isAnagramWithSorted(a, b):

    a = ''.join(c for c in a if c.isalnum()).lower()
    b = ''.join(c for c in b if c.isalnum()).lower()

    if len(a) != len(b):
        return False

    sorted(a); sorted(b);

    return a == b

def isAnagramWithCounter(a, b):
    from collections import Counter

    a = ''.join(c for c in a if c.isalnum()).lower()
    b = ''.join(c for c in b if c.isalnum()).lower()

    return Counter(a) == Counter(b)


if __name__ == '__main__':
    s1 = input('첫 번째 문자열 입력:')
    s2 = input('두 번째 문자열 입력:')
    print('V1', end='-')
    if isAnagramWithSorted(s1, s2):
        print('어구전철입니다.')
    else:
        print('어구전철이 아닙니다.')

    print('V1', end='-')
    if isAnagramWithCounter(s1, s2):
        print('어구전철입니다.')
    else:
        print('어구전철이 아닙니다.')


