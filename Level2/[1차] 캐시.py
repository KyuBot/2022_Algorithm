def solution(cacheSize, cities):
    answer = 0
    city = [''] * cacheSize

    if cacheSize == 0:
        return len(cities) * 5

    for word in cities:
        word = word.lower()
        if word in city:
            l = city.index(word)
            city.pop(l)
            city.append(word)
            answer += 1
        else:
            city.pop(0)
            city.append(word)
            answer += 5

    return answer