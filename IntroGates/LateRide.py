'''One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.

When you finally decide to head back, you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.

Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.

Example

For n = 240, the output should be
lateRide(n) = 4.

Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.

For n = 808, the output should be
lateRide(n) = 14.

808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.

Input/Output

[time limit] 4000ms (py)
[input] integer n

The duration of your ride, in minutes. It is guaranteed that you've been riding for less than a day (24 hours).

Constraints:
0 ≤ n < 60 · 24.

[output] integer

The sum of the digits the digital timer would show.'''

def lateRide(n):
    sec = n%60
    minu = (n-sec)/60
    temp = 0
    while sec:
        temp += sec%10
        sec //= 10
    while minu:
        temp += minu%10
        minu //=10
    return temp
