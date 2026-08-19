class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_hash = defaultdict(list) # array_key: string_list[]
        for word in strs:
            char_array = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                char_array[index] += 1
            string_hash[tuple(char_array)].append(word)
        return list(string_hash.values())