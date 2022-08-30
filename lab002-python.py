'''
Writing a function that returns all the permutation of the given string of length 3
in O(n!) complexity.
'''


def permutaions(word: str):
    result = []  # making empty list that will store all the possible strings
    for i in range(len(word)):
        for j in range(len(word)):
            if j == i:
                continue
            for k in range(len(word)):
                if j == k or i == k:
                    continue
                # if index j==k or i==k then it will skip that arrangement and return others
                result.append(word[i]+word[j]+word[k])
                # append will add the possible arrangements(words) in the empty list
    result.sort()  # it will arrange all posssible elements in order
    return result


if __name__ == '__main__':
    word = input("Enter a 3 letter word: ") #taking input 
    print(f"All permutations of the {word} are: ")
    print(permutaions(word)) #function calling
