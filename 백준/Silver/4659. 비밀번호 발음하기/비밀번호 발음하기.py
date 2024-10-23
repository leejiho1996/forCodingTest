import sys
input = sys.stdin.readline

vowel = {"a", "e", "i", "o", "u"}

while True:
    word = input().rstrip()

    if word == 'end':
        break

    is_vowel = False  # 모음 포함 여부
    is_three = False  # 세 글자 연속 자음/모음 여부
    is_two = False    # 같은 글자 연속 여부

    if len(word) == 1:  # 한 글자 처리
        if word not in vowel:
            print(f"<{word}> is not acceptable.")
        else:
            print(f"<{word}> is acceptable.")
        continue
    
    for i in range(len(word)):  # 첫 글자부터 확인
        char = word[i]
        
        # 세 글자 연속 자음/모음 확인
        if i >= 2:
            v, c = 0, 0
            for j in range(i-2, i+1):  # 3글자 범위 확인
                if word[j] in vowel:
                    v += 1
                else:
                    c += 1

            if c == 3 or v == 3:
                is_three = True
                break

        # 모음 포함 여부 확인
        if char in vowel:
            is_vowel = True

        # 연속된 같은 글자 확인 (ee, oo는 허용)
        if i > 0 and word[i] == word[i-1]:
            if word[i] != 'e' and word[i] != 'o':
                is_two = True
                break

    # 모든 조건을 만족하는지 확인
    if not is_vowel or is_three or is_two:
        print(f"<{word}> is not acceptable.")
    else:
        print(f"<{word}> is acceptable.")
