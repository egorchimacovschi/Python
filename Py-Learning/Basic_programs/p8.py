
def listSum(arr):
    #code here
    length = len(arr)
    sum = 0
    i = 0
    
    while length > 0:
        i = length - 1
        sum += int(arr[i])
        length -= 1
        
    return sum
array = [54, 43, 2, 1, 5]
print(listSum(array))

string = "egor"
print(string.upper())