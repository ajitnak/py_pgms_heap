def smallest(list, k):
	return kth_smallest(list, 0, len(list) - 1, k-1)

def kth_smallest(arr, low, high, k):
    # If k is smaller than number of  
    # elements in array 
    if (k >= 0 and k <= high - low ): 
      
        pos = partition(arr, low, high) 
  
	#print pos, low,k
        if pos - low == k: 
            return arr[pos] 
        if pos - low > k : # If position is more,  
            return kth_smallest(arr, low, pos - 1, k) 
  
        # Else recur for right subarray 
        return kth_smallest(arr, pos + 1, high, k - pos + low - 1) 
  
    # If k is more than number of 
    # elements in array 
    return None

def partition(arr, low, high): 
  
    x = arr[high] 
    i = low 
    for j in range(low, high): 
        if (arr[j] <= x): 
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
    arr[i], arr[high] = arr[high], arr[i] 
    return i 
			
print smallest([12, 3, 5, 7, 4, 19, 26], 1)
print smallest([12, 3, 5, 7, 4, 19, 26], 2)
print smallest([12, 3, 5, 7, 4, 19, 26], 3)
print smallest([12, 3, 5, 7, 4, 19, 26], 4)
print smallest([12, 3, 5, 7, 4, 19, 26], 5)
print smallest([12, 3, 5, 7, 4, 19, 26], 6)
print smallest([12, 3, 5, 7, 4, 19, 26], 7)
