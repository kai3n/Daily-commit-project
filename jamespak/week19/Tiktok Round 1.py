# number of ways to decode a string
# A -> 1 B->2, Z -> 26, C:3 D:4 E:5 F:6 G:7 H:8 I:9 J:10 K:11 L:12 M:13
# '12' => 'AB', ''  => 2
# '01' => 0 
# '110' => Ax => 1 AA


# "4113" -> DAAAC, DKM, DKAC
# "021" -> 0

"""
1. look back one previous element

2. look back two previous elements
"""

"""
4113 -> DAAC, DAM, DKC
0232 -> 0
[1, 1, 0, 0, 0]
"""

def get_number_of_ways_to_decode_string(s): # s represent int values
    if s and s[0] == "0":
        return 0
        
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 0 if s[0] == "0" else 1 # [1, 0, 0, 0, 0]
    
    for i in range(2, len(s) + 1): # [1, 0, 0, 0, 0]
        # 1 <= x <= 9
        if 1 <= int(s[i - 1]) <= 9: # [1, 0 ,0 ,0 ,0]
            dp[i] += dp[i - 1]
            
        # 10 <= x <= 26
        if 10 <= int(s[i-2:i]) <= 26: # [1, 0, 0, 0, 0]
            dp[i] += dp[i - 2]
            
    return dp[-1]
    
print(get_number_of_ways_to_decode_string("4113"))
print(get_number_of_ways_to_decode_string("0232"))
