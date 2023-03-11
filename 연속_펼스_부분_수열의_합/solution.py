def solution(sequence):
    p_pulse = []
    n_pulse = []
    
    for i in range(len(sequence)):
        if i % 2 == 0:
            p_pulse.append(sequence[i])
            n_pulse.append(-sequence[i])
        else:
            p_pulse.append(-sequence[i])
            n_pulse.append(sequence[i])
            
    p_sum = [0]*len(sequence)
    n_sum = [0]*len(sequence)
    p_sum[0] = p_pulse[0]
    n_sum[0] = n_pulse[0]
    
    for j in range(1,len(sequence)):
        p_sum[j] = max(0, p_sum[j-1]) + p_pulse[j]
        n_sum[j] = max(0, n_sum[j-1]) + n_pulse[j]
    
    answer = max(max(p_sum),max(n_sum))
    return answer

if __name__ == "__main__":
    gt = 10
    sequence = [2,3,-6,1,3,-1,2,4]
    if solution(sequence) == gt:
        print("correct")
    else:
        print("fail")