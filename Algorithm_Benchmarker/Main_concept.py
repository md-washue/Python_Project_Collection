arr=[47, 12, 89, 3, 76, 54, 21, 98, 34, 65, 7, 43, 19, 82, 56, 10, 91, 28, 73, 14,
60, 37, 5, 84, 26, 69, 48, 96, 17, 52, 31, 8, 75, 40, 99, 23, 58, 11, 67, 35,
2, 87, 44, 71, 16, 93, 29, 62, 50, 6, 79, 25, 95, 18, 53, 38, 86, 13, 64, 32,
74, 45, 20, 88, 9, 57, 36, 97, 24, 68, 15, 80, 41, 94, 30, 59, 4, 72, 22, 85,
49, 61, 27, 90, 33, 70, 1, 83, 55, 39, 77, 46, 92, 63, 51, 66, 81, 78, 100, 42]

def making_half(array):
    if (len(array)<=1):
        return array
    
    half=(len(array)//2)

    first_half=making_half(array[:half])
    end_half= making_half(array[half:])

    return main_sorter(first_half,end_half)

def main_sorter(left,right):
    array=[]

    i=j=0

    while(i<len(left) and j< len(right)):
        if(left[i]< right[j]):
            array.append(left[i])
            i +=1
        else:
            array.append(right[j])
            j +=1
        
        
    array.extend(left[i:])
    array.extend (right[j:])
    return array

final_array=making_half(arr)

print(final_array)