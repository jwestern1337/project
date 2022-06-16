""
def is_anagram(one, two):
    if len(one) != len(two):
        return False
    else:
        listone = []
        listtwo = []
        for l in str(one):
            listone.append(l)
        for i in str(two):
            listtwo.append(i)
        listone.sort()
        listtwo.sort()
        if listone == listtwo:
            return True
        else:
            return False

#print(is_anagram("typhoon", "opython"))
#print(is_anagram("Alice", "Bob"))
"""

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array


def sort():
    string=input("Word: ")
    word_to_sort = []
    for s in string:
        word_to_sort.append(s)
    print(bubble_sort(word_to_sort))

    
sort()
