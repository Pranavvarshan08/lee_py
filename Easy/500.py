class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        return [w for w in words if any(all(c.lower()in r for c in w)for r in rows)]
