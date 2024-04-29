def reverseWords(s):
    arr = s.split()
    arr.reverse()
    return (" ".join(arr))

if __name__ == '__main__':
    s = "the sky is blue"
    s = reverseWords(s)
    print(s)