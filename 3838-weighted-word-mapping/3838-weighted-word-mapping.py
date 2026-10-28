class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            # Calculate the total weight of the word
            total_weight = sum(weights[ord(c) - ord('a')] for c in word)
            
            # Take the weight modulo 26
            remainder = total_weight % 26
            
            # Map the result using reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a')
            mapped_char = chr(ord('z') - remainder)
            res.append(mapped_char)
            
        return "".join(res)