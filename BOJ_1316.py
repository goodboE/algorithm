"""
1. 알파벳을 저장할 리스트를 만들고 리스트에 없는 알파벳이라면 추가.
2. 만약 리스트에 있는 알파벳이라면 ?
    2.1 리스트의 마지막 알파벳과 같다면 ok
    2.2 마지막 알파벳이 아니라면 그룹문자가 아니다.
"""
n = int(input())
count = 0

for i in range(n):
    words = list(input())
    tmp = words[0] # 비교대상
    used = []
    is_group_word = True
    for word in words: # 한글자씩 가져옴
        if word in used:
            if word != tmp:
                is_group_word = False
                break
        # 리스트에 없는 알파벳일경우 리스트에 추가
        used.append(word)
        tmp = word

    if is_group_word:
        count += 1

print(count)







