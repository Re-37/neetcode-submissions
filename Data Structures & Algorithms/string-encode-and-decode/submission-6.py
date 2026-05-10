class Solution:

    def encode(self, strs: List[str]) -> str:
        coded=''
        for i in str(strs):
            coded+=(chr(ord(i)-20))
        return coded
    def decode(self, s: str) -> List[str]:
        decoded=''
        for i in s:
            decoded+=(chr(ord(i)+20))
        return ast.literal_eval(decoded)