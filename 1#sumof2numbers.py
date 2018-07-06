'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''
# bruteforce - n^2
def find2nums(sum, numbers):
    for i in range(0,len(numbers)):
        for j in range(i+1, len(numbers)):
            if sum == (numbers[i] + numbers[j]) :
                return [numbers[i],numbers[j]]

# sort and search - nlogn - issue same number repeats if sum exactly half can fix if using index
def find2nums2(sum,numbers):
    numbers2 = sorted(numbers)
    for i in numbers2:
        if sum-i in numbers2:
            return ([i, sum-i]) 

#check for sum-i of hash if exists return else continue
#hash function dependent
def usehash(sum, numbers):
    h = {}
    for i in numbers:
        if sum-i in h:
            return ([i,sum-i])
        h[i] = 1    

print (usehash(14, [10 ,15, 3, 7]))
print (usehash(17, [10 ,15, 3, 7]))
print (usehash(14, [7 ,15, 3, 7]))
