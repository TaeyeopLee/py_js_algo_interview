class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ', paragraph)
                .lower().split()
                if word not in banned]
        # ['bob', 'a', 'ball', 'the', 'ball', 'flew', 'far', 'after', 'it', 'was']
        counts = collections.Counter(words)
        # Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
        return counts.most_common(1)[0][0]