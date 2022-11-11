keyboard = "abcdefghijklmnopqrstuvwxy"
text = "cba" 

def abs_diff(key_board,txt):

    dico={}

    dp=[0]*len(txt)

    for idx, char_ in enumerate(key_board):

        dico[char_]=idx

    dp[0]=dico[txt[0]]
    for idy in range(1,len(txt)):

        dp[idy]= abs(dp[idy-1]-dico[txt[idy]])


    return sum(dp)


##print(abs_diff(keyboard,text))

    