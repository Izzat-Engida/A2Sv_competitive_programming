class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            decode_str = ''
            k = 0
            while index < len(s):
                char = s[index]
                if char.isdigit():
                    k = k * 10 + int(char)
                elif char == '[':
                    index, decoded = helper(index + 1)
                    decode_str += k * decoded
                    k = 0
                elif char == ']':
                    return index, decode_str
                else:
                    decode_str += char
                index += 1
            return index, decode_str

        return helper(0)[1]
