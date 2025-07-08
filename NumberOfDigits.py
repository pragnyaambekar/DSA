'''Ninja want to add coding to his skill set so he started learning it. On the first day, he stuck to a problem in which he has given a long integer ‘X’ and had to count the number of digits in it.
Ninja called you for help as you are his only friend. Help him to solve the problem.
EXAMPLE:
Input: 'X' = 2

Output: 1

As only one digit is ‘2’ present in ‘X’ so answer is ‘1’.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= 'T' <= 1000
1 <= ‘X’ <= 10^18
Time Limit: 1 sec'''


def countDigit(n: int) -> int:
   num = n
   count = 0
   while(num>0):
      count = count + 1
      num = num//10
   return count
