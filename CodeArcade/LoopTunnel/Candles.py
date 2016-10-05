'''When a candle finishes burning it leaves a leftover. makeNew leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.

You have several candles in your possession. What's the total number of candles you can burn, assuming that you create new candles as soon as you have leftovers?

Example

For candles = 5 and makeNew = 2, the output should be
candles(candles, makeNew) = 9.

Here is what you can do to burn 9 candles:

burn 5 candles, obtain 5 leftovers;
create 2 more candles, using 4 leftovers (1 leftover remains);
burn 2 candles, end up with 3 leftovers;
create another candle using 2 leftovers (1 leftover remains);
burn the created candle, which gives another leftover (2 leftovers in total);
create a candle from the remaining leftovers;
burn the last candle.
Thus, you can burn 5 + 2 + 1 + 1 = 9 candles, which is the answer.

Input/Output

[time limit] 4000ms (py)
[input] integer candles

Constraints:
1 ≤ candles ≤ 15.

[input] integer makeNew

Constraints:
2 ≤ makeNew ≤ 5.

[output] integer'''

def candles(candles, makeNew):
    total = 0
    leftover=0
    while candles:
        total += candles
        leftover += candles
        candles = leftover//makeNew
        leftover -= candles*makeNew
    return total
