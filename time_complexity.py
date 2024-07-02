

#Constant

x = 10 #assignment operations

y = x * 2 #math operations

if y > 5:
    print('yes')

def double_even(x): #Accepts and in, if it is even double it
    if x%2==0:
        return x * 2
    else:
        print('nothing')

print(double_even(100))

#Logrithmic:

#Binary Search Stay tuned for Wed/Mon
    

#Linear: Operations for each piece of data pumped in


def double_evens(alist):
    output = []

    for num in alist: #This for loop requires my solution to do an operation for each piece of data I input
        if num%2 == 0:
            output.append(num*2)
    
    return output

nums = [1,2,3,4,5,6,7,8,9,10]

print(double_evens(nums))

def double_split(alist): #Stacked for loops/ linear operations have a negligible effect on time complexity
 
    evens =[]
    odds = []

    for num in alist:
        if num%2 == 0:
            evens.append(num*2)

    for num in alist:
        if num%2 == 1:
            odds.append(num*2)
    
    return (evens, odds)

def searcher(alist, target): #Time complexity is determined by the worse-case scenario
    for num in alist:
        if num == target:
            return "Target Aquired"
        
alist = [1,2,3,4,5]
target = 1

print(searcher(alist,target))


#Linear Logrithmic O(n logn)

def largest(alist):
    sorted_list = sorted(alist) #automatically becomes a O(n logn) solution
    largest = sorted_list[-1]

    return largest

print(largest([23,12,65,37,81,3]))

#Quadratic

def quad(alist):

    for num1 in alist:
        print(f'Pass #{num1}')
        for num2 in alist:  #Obvious Quads (nested for loops)
            print(num2)


alist = [1,2,3,4,5,6,7,8,9,0]

quad(alist)


#BE CAREFUL OF NESTING A LINEAR BUIL-IN INSIDE A FOR LOOP

def highest_count(alist):
    highest_counter = 0
    high_num = 0
    for num in alist:
        if my_count(alist, num) > highest_counter:
            high_num = num
            highest_counter = my_count(alist, num)

    return high_num

alist = [1,1,1,1,2,2,3,3,3,4,5]
print(highest_count(alist))


def my_count(self, target):
    count = 0
    for num in self:
        if num == target:
            count += 1
    return count
