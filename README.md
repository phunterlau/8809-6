8809-6
======

a data scientist solution of the '8809=6' problem

- update: thanks to Yan Wang's comment that I realized '4' is not an available signal which should not give weight '1'.
 
a data scientist way to solve the 8809=6 problem

author: hongliang liu

problem: from Saam's email:

8809=6
7111=0
2172=0
6666=4
1111=0
3213=0
....

2581=?

answer: I know the answer since 1987 when I was 5, not to spoiler. But it becomes interesting to have a 
general solution: linear regression by frequency.

one can list the digits by its frequency, and this problem becomes a linear regression for a 10-dimension
(x0-x9) space, where:

8809=6 -> 100000021 = 6 by freq where 1,2,1 are p0,p8,p9 as parameters

thus, a linear regression can solve this problem easily.

explain the output:

the output should be:

(array([ 1.00000000e+00,   4.75790411e-24,   4.75709632e-24,
         4.75588463e-24,   1.00000000e+00,   4.75951970e-24,
         1.00000000e+00,   4.75790411e-24,   2.00000000e+00,
         1.00000000e+00]), 2)

it indicates the coeffciency for number 0 to 9 is:
1,0,0,0,1,0,1,0,2,1

which means, when number 0,4,6,9 appears, the weight is 1, and 8 gives weight two. 
Some comments from Yan Wang let me realized '4' does not exist in the list, so one should take out '4'.

thus:

--- spoiler alert --

count by circles, 0,4,6,9 have 1 circle while 8 has two circles.

one can easily make another set of problems and solve by this linear regression
