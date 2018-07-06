'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

# bruteforce with corner cases
def getarray(nums):
    pro = 1
    count = 0
    for i in nums:
        if i != 0:
            pro = pro*i
        else:
            count = count  + 1
    ans = []
    
    if count > 1:
        for i in nums:
            ans.append(0)
    else:
        for i in nums:
            if i != 0:
                if count == 0:
                    ans.append(pro//i)
                else:
                    ans.append(0)
            else:
                ans.append(pro)
    return ans

#make a left and right array and multiple them
def getarray2(nums):
    left = []
    right = []

    pro = 1
    for i in nums:
        left.append(pro)
        pro = pro * i

    pro = 1
    for j in nums[::-1]:
        right.append(pro)
        pro = pro * j
    
    right = right[::-1]


    #print (left, right)
    ans = []
    ans = [left[i]*right[i] for i in range(0,len(left))]
    return ans

print (getarray([1,2,3,4,5]))
print (getarray([3,2,1]))
print (getarray([0,1]))
print (getarray([0,0]))
print (getarray2([1,2,3,4,5]))
print (getarray2([3,2,1]))
print (getarray2([0,1]))
print (getarray2([0,0]))