def solution(n, m, section):
    answer = 0
    _st = section[0] - 1

    for _blk in section:
        if _st < _blk:
            answer += 1
            _st = _blk + m - 1

    return answer

if __name__ == "__main__":
    gt = [2,1,4]
    n = [8,5,4]
    m = [4,4,1]
    section = [[2,3,6], [1,3], [1,2,3,4]]

    for i in range(len(n)):
        if solution(n[i],m[i],section[i]) == gt[i]:
            print("correct")
        else:
            print("fail")