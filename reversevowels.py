def reverseVowels(s):
    ss = {'a', 'e', 'i', 'o', 'u'}
    vowels = [i for i in s if i in ss]
    vowels = vowels[::-1]
    i = 0
    j = 0
    return_string = ""
    while j < len(s):
        if s[j] in ss:
            return_string += vowels[i]
            i += 1
        else:
            return_string += s[j]
        j += 1

if __name__ == '__main__':
    s = "hello"
    reverseVowels(s)