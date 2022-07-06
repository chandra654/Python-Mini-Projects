#Project No : 8
#Binary search implementation



def binary_search(lst , search_key):
    low = 0
    high = len(lst) - 1

    index = (low + high) // 2
    
    while lst[index] != search_key and low <= high: #!important
        if lst[index] > search_key:
            high = index - 1

        elif lst[index] < search_key:
            low = index + 1

        index = (low +high) // 2

    #failing condition        
    if low > high:
        print(f"{search_key} not found in list")
        return
        
    print(f"{search_key} is found at {index+1} position")

#Test cases
binary_search([1,2,3,4,6],4)
binary_search([1,2,3,4,6],5)
