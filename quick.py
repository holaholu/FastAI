def firstUniqChar(s: str) -> int:
        for val in s:
            if s.count(val) == 1:
                print(f"Found unique character: {val}")
                return s.index(val)
        return -1


print(firstUniqChar("leetcoders1"))