class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        groups=[]
        for word in strs:
            lettersInWord={}
            for letter in word:
                if letter in lettersInWord:
                    lettersInWord[letter]+=1
                else:
                    lettersInWord[letter]=1
            key=tuple(sorted(lettersInWord.items()))
            if key in freq.keys():
                freq[key].append(word)
            else:
                freq[key]=[word]
        
        for group in freq.values():
            groups.append(group)
        return groups
            