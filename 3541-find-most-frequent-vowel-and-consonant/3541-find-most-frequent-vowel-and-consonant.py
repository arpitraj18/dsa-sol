class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        vowel_counts = {}
        consonant_counts = {}
        
        for char in s:
            if char in vowels:
                vowel_counts[char] = vowel_counts.get(char, 0) + 1
            else:
                consonant_counts[char] = consonant_counts.get(char, 0) + 1
                
        max_vowel = max(vowel_counts.values()) if vowel_counts else 0
        max_consonant = max(consonant_counts.values()) if consonant_counts else 0
        
        return max_vowel + max_consonant