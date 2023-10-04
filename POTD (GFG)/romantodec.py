def romanToDecimal(S): 
        # code here
        lookup = {
            "I": 1,
            "V" :5,
            "X" :10,
            "L" :50,
            "C" :100,
            "D" :500,
            "M" :1000 
        }
        result = 0
        N = len(S)
        # i = N-1
        for i in range(N-1,-1,-1):
                # print(f"{S[i]} = {lookup[S[i]]}")
                # print(f"next = {lookup[S[i+1]]}")
                # print(f"result = {result}")
                if i < N-1 and lookup[S[i]] < lookup[S[i+1]]:
                        # print(f"current= {lookup[S[i]]}  next = {lookup[S[i+1]]}")
                        result -= lookup[S[i]]
                        # print(f"result = {result}")
                else: 
                       result += lookup[S[i]]
                # print(f"result = {result}")
        return result
print(romanToDecimal("MCMXCIV"))
