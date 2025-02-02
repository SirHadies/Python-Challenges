for number in range(1, 100):
    if number %3 == 0 and number %5 == 0:
        print("FizzBuzz")
    elif number %5 == 0:
        print("Buzz")
    elif number %3 == 0:
        print("Fizz")
    else:
        print(number)
            
fruits = ["Apple", "Peaches", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print("do you want some " + fruit + " juice?")

men_Names = ["Michael", "Brian", "Danny", "Richard", "Bobby"]
for dudes in men_Names:
    print("My name is " + dudes + " and I am a man!!")

#Bart Simpson Generator
#bart_Simpson = ("No one is interested in my underpants.")
#for i in range(100):
#    print(bart_Simpson)

student_scores = [150, 142, 185, 120, 173, 184, 263, 233, 124, 253, 78, 92, 73, 54, 88, 93, 84, 71, 42, 35, 56, 47, 53, 12, 23, 12, 13, 10]
total_exam_score = sum(student_scores)
print(total_exam_score)
#length = len(student_scores)
#print(length)
sum = 0
for score in student_scores:
    sum += score

print(sum)

median = (sum / 28)
median = round(median, 2)
median = str(median)
print("the median score is " + median)

#let's do the max from the scores
#print(max(student_scores))

max_Score = 0
for score in student_scores:
    if score > max_Score:
        max_Score = score

print(max_Score)

#sets a variable to chech against while going through the for loop
min_Score = 500
#score will just be the placeholder as it goes through the list
for score in student_scores:
    #if the score in the list is smaller than the next number
    if score < min_Score:
        #this will set that number as the new min score until a new smaller number is checked.
        min_Score = score
print(min_Score)

numbers_Needing_Square = [1, 2, 3, 4, 5]
for squre in numbers_Needing_Square:
    squre = (squre * squre)
    print(squre)


only_Evens = [3, 8, 12, 7, 5, 10, 22 ,9]
for evens in only_Evens:
   if evens %2 ==0:
       print(evens)
       

students = ["Alice", "Bob", "Charlotte", "David", "Eleanor", "Frank"]
for names in students:
    if len(names) > 5:
        print(names)


prices = [15, 25, 30, 10, 50, 18, 40]
for approved_Prices in prices:
    if approved_Prices > 20:
        print("Discounted Price " + str(approved_Prices * .9))

loaf_counts = [5, 0, 3, 0, 8, 2, 0]
for loafs in loaf_counts:
    if loafs == 0:
        print("Sold out!")
    else:
        print("woah! there are " + str(loafs) + " loafs left")
    