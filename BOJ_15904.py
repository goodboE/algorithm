get_string = input()
UCPC = ['U', 'C', 'P', 'C']
count = 0

for i in range(len(get_string)):
    if get_string[i] == UCPC[count]:
        count += 1
    if count >= 4:
        break
if count >= 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
