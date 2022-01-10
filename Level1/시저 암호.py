def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            if (n + ord(s[i]) - ord('a')) < 26:
                answer += chr(n + ord(s[i]))
            else:
                answer += chr(n - (ord('z') - ord(s[i])) + ord('a') - 1)
        elif 'A' <= s[i] <= 'Z':
            if (n + ord(s[i]) - ord('A')) < 26:
                answer += chr(n + ord(s[i]))
            else:
                answer += chr(n - (ord('Z') - ord(s[i])) + ord('A') - 1)
        else:
            answer += s[i]

    return answer

