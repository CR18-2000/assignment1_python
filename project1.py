#Write a function number2base_rep(n, b) that takes two integers 
#and returns (n)b as a string.

def number2base_rep(n, b):
    #string in which I append reminders
    s = ""
    #I use a boolean to know when to stop the cycle
    fine = False
    while not fine:
        #I compute the reminder of the division of n by b
        reminder = n % b
        #I concatenate the old string with the new reminder
        s = s + str(int(reminder))
        #I stop to do divisions when I reach a reminder that is equal to n, otherwise I divide n-reminder by b
        if reminder == n:
            fine = True
        else:
            n = (n-reminder)/b  
    #All the reminder must be read on reverse order
    return s[::-1]



#Write a function admissible(n, b) that takes two integers 
#and returns if n is b-admissible.

def admissible(n, b):
    #I write the number n in base b using the previous function
    num = number2base_rep(n, b)
    #length of the substring
    for i in range(1,len(num)//2+1):
        #starting index of the subsequence
        for j in range(0,len(num)-i-i+1):
            #I check if the substring of length i starting in position j is equal
            #to the substring of length i starting in poition j+i
            if num[j:j+i] == num[j+i:j+i+i]:
                return False
    return True



#Write a function count_admissible(b, start, end) that takes three integers 
# and returns the number of b-admissible numbers n with start ≤ n < end.

def count_admissible(b, start, end):
    counter = 0
    for number in range(start, end):
        #if the previous function return true I increment the counter
        if admissible(number, b):
            counter += 1
    return counter



#Write a function count_admissible_width(b, width) that takes two integers 
# and returns the number of b-admissible numbers n 
# whose b-representation has exactly width digits.

def count_admissible_width(b, width):
    #the smallest number in base b with width digits is b followed by (width-1) zeros
    #so the corresponding integer is b^(width-1)
    if width != 1:
        start = b**(width-1)
        end = 0
        #the greatest number in base b on length width is the string composed by b (b-1)
        #then the corresponding integer is (b-1)*b^(width-1)+(b-1)*b^(width-2)+..+(b-1)*b^(width-width)
        for j in range(width):
            end = end + b**j
        end = (b-1)*end
    else:
        start = 0
        end = b-1
    #I apply the previous function with the just said start and end 
    return count_admissible(b, start, end+1)



#Write a function largest_multi_admissible(L, start, end) that takes 
# a list L and two integers and returns the largest integer n with 
# start ≤ n < end that is b-admissible for all b ∈ L. 
# The function must return None if no such number exists.

def largest_multi_admissible(L, start, end):
    #since I have to look for the greatest integer between start and end (not included)
    #I can use the range in reverse order, from end-1 (since end is not included) to start-1 (since start is included)
    for n in range(end-1, start-1, -1):
        adm = True
        for b in L:
            if not admissible(n,b):
                #if I find a basis b for which n is not admissible I change tha value of the boolean variable
                adm = False
        #if the boolean variable is true I return n since it is the biggest
        if adm:
            return n
    #if it does not return anything I return none
    return None
