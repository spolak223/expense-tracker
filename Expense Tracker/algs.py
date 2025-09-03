def merge_sort(user):
    if len(user) <= 1:
        return user
    else:
        L = user[len(user) // 2:]
        R = user[:len(user) // 2]
        sorted_L = merge_sort(L)
        sorted_R = merge_sort(R)
        return merge(sorted_L, sorted_R)

def merge(left, right):
    i = 0
    j = 0
    result = []

    #checking the left side of the list to the right
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    #checking the right list to the left list
    while j < len(right) and i < len(left):
        if right[j] < left[i]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    
    #now just adding the final bits
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def display(user):
    if user:
        result = merge_sort(user)
        for item in result:
            print(f"> {item}")
        print("\n")
    else:
        print("Nothing here...\n")

            