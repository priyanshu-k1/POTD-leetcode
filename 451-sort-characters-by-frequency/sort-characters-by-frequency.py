class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}
        for i in s:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i]+=1
        sortedData = sorted(mp.items(),key=lambda item:(-item[1],item[0]))
        return "".join([i[0]*i[1] for i in sortedData])
       

        