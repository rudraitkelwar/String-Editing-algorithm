# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 18:21:38 2019

@author: RUDRA
"""

class EditDistance:

    def __init__(self):
        self.__prepare__()

    def __prepare__(self, N = 0, M = 0):
        self.dp = [[-1 for y in range(0,M)] for x in range(0,N)]

    def __solveDP(self, x, y):
        if (x==-1):
            return y+1
        elif (y==-1):
            return x+1
        elif (self.dp[x][y]>-1):
            return self.dp[x][y]
        else:
            if (self.A[x]==self.B[y]):
                self.dp[x][y] = self.__solveDP(x-1,y-1)
                print("UPDATE","(",x,y,")")
            else:
                self.dp[x][y] = 1+min(self.__solveDP(x,y-1), self.__solveDP(x-1,y), self.__solveDP(x-1,y-1))
                print("INSERT/DELETE","(",x,y,")")

            return self.dp[x][y]

    def solve(self, A, B):
        if isinstance(A,bytes):
            A = A.decode('ascii')

        if isinstance(B,bytes):
            B = B.decode('ascii')

        self.A = str(A)
        self.B = str(B)

        self.__prepare__(len(A), len(B))

        return self.__solveDP(len(A)-1, len(B)-1)


def min_distance_bottom_up(word1: str, word2: str) -> int:
    
    m = len(word1)
    n = len(word2)
    dp = [[0 for _ in range(n+1) ] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):

            if i == 0:  
                dp[i][j] = j
            elif j == 0: 
                dp[i][j] = i
            elif word1[i-1] == word2[j-1]: 
                dp[i][j] = dp[i-1][j-1]
                
            else:
                insert = dp[i][j-1]
                delete = dp[i-1][j]
                replace = dp[i-1][j-1]
                
                dp[i][j] = 1 + min(insert, delete, replace)
                
               
    a=dp[i][j]
    if(int(a+1)==insert or int(a+1)==delete):
                   
                     print("INSERT/DELETE")
    else:
                     print("UPDATE")
    return dp[m][n]

if __name__ == '__main__':
        solver = EditDistance()

        print("****************** Testing Edit Distance DP Algorithm ******************")
        print()

        S1 = input("Enter the first string: ").strip()
        S2 = input("Enter the second string: ").strip()

        print()
        if(min_distance_bottom_up(S1, S2) == 0):
            print("CORRECT SPELLING, NO NEED TO CHANGE!!!")
        else:
            print("")
       
        print("The minimum String Edit Distance is: %d" % (min_distance_bottom_up(S1, S2)))
        print("The minimum String Edit Distance is: %d" % (solver.solve(S1, S2)))
        print()
        print("*************** End of Testing Edit Distance DP Algorithm ***************")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
