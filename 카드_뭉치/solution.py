def solution(cards1, cards2, goal):
    answer = ''

    len_c1 = len(cards1)
    len_c2 = len(cards2)
    len_g = len(goal)

    _idx0 = []
    _idx1 = []

    if not len_c1 == 0:
        if not cards1[0] in goal:
            cards1 = []
            len_c1 = 0
        else:
            for word1 in cards1:
                try:
                    _idx0.append(goal.index(word1))
                except:
                    break
            
    if not len_c2 == 0:
        if not cards2[0] in goal:
            cards2 = []
            len_c2 = 0
        else:
            for word2 in cards2:
                try:
                    _idx1.append(goal.index(word2))
                except:
                    break

    if len(_idx0) == 0:
        if cards2 == goal:
            return "Yes"
    elif len(_idx1) == 0:
        if cards1 == goal:
            return "Yes"
    elif len(_idx0) + len(_idx1) == len_g:
            if sorted(_idx0) == _idx0 and sorted(_idx1) == _idx1:
                return "Yes"
            
    answer = "No"

    return answer


gt = ["Yes", "No", "No", "Yes", "No", "Yes", "Yes", "Yes", "No"]
lst_cards1 = [["i","drink","water"],["i","water","drink"],["a"],[],["a","b","c"],["a"],["a","b"],
              ["a","b"],["e", "f", "h"]]
lst_cards2 = [["want","to"],["want","to"],["b","d","c"],["do","that"],["d","e"],["b","c"],
              ["c", "e"],["c", "e"],["k", "l"]]
goal = [["i","want","to","drink","water"],["i","want","to","drink","water"],
        ["a","b","c","d"],["do","that"],["b","c","d","e"], ["b","c"],["a","c"],["a","c","e"],
        ["e", "h", "k"]]

if __name__ == "__main__":
    for i in range(len(goal)):
        if solution(lst_cards1[i],lst_cards2[i],goal[i]) == gt[i]:
            print("correct")
        else:
            print("fail")