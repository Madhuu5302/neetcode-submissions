class Solution:

    def encode(self, strs):
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            length = ""

            while s[i] != "#":
                length += s[i]
                i += 1

            length = int(length)

            i += 1

            word = s[i:i + length]
            result.append(word)

            i += length

        return result