class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # Split the date string by '-' to separate year, month, and day
        parts = date.split('-')
        
        # Convert each part to an integer, then to a binary string using bin(), 
        # and slice off the '0b' prefix
        binary_parts = [bin(int(part))[2:] for part in parts]
        
        # Join the binary representations back together with hyphens
        return '-'.join(binary_parts)