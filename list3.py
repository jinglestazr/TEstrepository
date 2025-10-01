fruits=['apple','banana','cherry','date']
print(fruits)

num=[10,20,30,40,50]
print('the 1st elements are:',num[0])
print('the last elements are:',num[-1])

animals=['cat','dog','bird']
animals[1]='hamster'
print(animals)

colours=[]
colours.append('red')
colours.append('green')
colours.append('blue')
colours.remove('green')
print(colours)

names=['alice','bob','charlie','diana']
print('length of the list:', len(names))

num=[4,7,1,8,5]
total_sum=sum(num)
print('sum of elements:',total_sum)

ages=[23,45,18,34,60]
print('maximum age:',max(ages))
print('minimum age:',min(ages))

scores=[88,56,92,78,61]
scores.sort()
print('sorted list:',scores)

num=[1,3,5,7,9]
if 5 in num:
    print('found')
else:
    print('not found')

items=[1,2,2,3,4,4,4,5]
count_of_4=items.count(4)
print('count of 4:',count_of_4)
