def solution(name, yearning, photo):
    result = []
    name_yearning = dict(zip(name, yearning))
    for photo_ in photo:
        score = 0
        for person in photo_:
            if person in name_yearning:
                score += name_yearning[person]
        result.append(score)   
    return result
print(solution(["may","kein","kain","radi"],[5,10,1,3],[["may","kein","kain","radi"],["may","kein","brin","deny"],["kon","kain","may","coni"]]))