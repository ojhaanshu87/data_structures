#PROBLEM
''' 
There are people standing in a circle waiting to be executed. 
The counting out begins at some point in the circle and 
proceeds around the circle in a fixed direction. In each step,
a certain number of people are skipped and the next person 
is executed. The elimination proceeds around the circle 
(which is becoming smaller and smaller as the executed people
are removed), until only the last person remains, who is given freedom.
'''

#ALGORITHM
'''
When the Number of Participants is a Power of Two :

The elimination process works like this: the first pass starts at person 1 and proceeds clockwise, 
and each new pass starts every time person 1 is reached.
 The people eliminated on a pass are crossed out,
  and are marked to indicate the order in which they were eliminated.
   Eliminated people are then omitted in subsequent diagrams.

Three passes are required to determine the winner:

    Pass 1 eliminates four people: 2, 4, 6, 8.
    Pass 2 eliminates two people: 3, 7.
    Pass 3 eliminates one person: 5.

This leaves person 1 the winner.
Regardless of the number of participants n,
 person 1 survives the first pass. Since n is even,
  as every positive power of two is, person 1 survives the second pass as well. 
  In the first pass, the process goes like this: person 1 is skipped, person 2 is eliminated, 
  person 3 is skipped, person 4 is eliminated, person n-1 is skipped, person n is eliminated. 
  The second pass starts by skipping person 1.

As long as the number of participants per pass is even, 
as it will be for a power of two starting point, the same pattern is followed: 
person 1 is skipped each time. Therefore, for any power of two, person 1 always wins.

When the Number of Participants is NOT Power of Two :

we know this much as person 1 can not be the winner. 
This is because at least one pass will have an odd number of participants.
 Once the first odd participant pass is complete, 
 person 1 will be eliminated at the start of the next pass.

So is there an easy way to determine who is the winner? 
Lets step back and take a closer look at the elimination process in the 13 person example

Four passes are required to determine the winner:

    Pass 1 eliminates six people: 2, 4, 6, 8, 10, 12.
    Pass 2 eliminates four people: 1, 5, 9, 13.
    Pass 3 eliminates one person: 7.
    Pass 4 eliminates one person: 3.

This leaves person 11 the winner.
'''

#APPROCH
'''
The Equations
We can solve both cases or in other words, 
for an arbitrary number of participants we have to use a little math.

Write n as n = 2m + k, 
where 2m is the largest power of two less than or equal to n.
 k people need to be eliminated to reduce the problem to a power of two,
  which means 2k people must be passed over. The next person in the circle,
   person 2k + 1, will be the winner. In other words, the winn
   er w is w = 2k + 1.

Lets apply these equations to a few examples

    n = 8: The equations still apply, although using them is unnecessary:
     n = 8 + 0, so k = 0 and w = 0 + 1 = 1.
    n = 13: n = 8 + 5, so k = 5 and w = 2*5 + 1 = 11.
    n = 1000:
     n = 1000 = 512 + 488, so k = 488 and w = 2*488 + 1 = 977.

The Formula

We can combine the equations n = 2m + k and w = 2k + 1 to get a single formula for w

    Rearrange n is equals 2m plus k to isolate k as  k equals n minus 2m.
    Substitute this expression for k into w = 2k + 1.

    w equals 2 times of n minus 2m plus 1  (where 2m is largest power of two <=n)
'''

#IMPEMENTATION
def largest_pow_of_two_less_than_num(num):
    assert num > 0
    last = num
    num &= num - 1
    while num:
        last = num
        num &= num - 1
    return last

#the person who survive last
def winner_person(number_of_persons):
	largest_pow_less_than_num = largest_pow_of_two_less_than_num(number_of_persons)
	winner = 2 *(number_of_persons-largest_pow_less_than_num) +1
	return winner

