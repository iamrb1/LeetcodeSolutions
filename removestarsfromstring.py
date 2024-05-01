def removeStars( s: str) -> str:
    rl = []
    for ele in s:
        if ele == "*" and len(rl) != 0:
            rl.pop()
        else:
            rl.append(ele)
    return "".join(i for i in rl)

if __name__ == '__main__':
    s = "leet**cod*e"
    print(removeStars(s))