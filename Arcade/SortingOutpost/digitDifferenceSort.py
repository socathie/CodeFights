def digitDifferenceSort(a):
    diff = [list(str(i)) for i in a]
    for i in range(len(diff)):
        diff[i] = [int(j) for j in diff[i]]
        diff[i] = max(diff[i])-min(diff[i])
    indices = [i for i in range(len(a))]
    combined = [list(i) for i in zip(diff,a,indices)]
    combined = sorted(combined,key = lambda x: (x[0],-x[2]))
    a = [x[1] for x in combined]
    return a

'''Given an array of integers, sort its elements by the difference of their largest and smallest digits. In the case of a tie, that with the larger index in the array should come first.

Example

For a = [152, 23, 7, 887, 243], the output should be
digitDifferenceSort(a) = [7, 887, 23, 243, 152].

Here are the differences of all the numbers:

152: difference = 5 - 1 = 4;
23: difference = 3 - 2 = 1;
7: difference = 7 - 7 = 0;
887: difference = 8 - 7 = 1;
243: difference = 4 - 2 = 2.
23 and 887 have the same difference, but 887 goes after 23 in a, so in the sorted array it comes first.

Input/Output

[time limit] 4000ms (py)
[input] array.integer a

An array of integers.

Constraints:
0 ≤ sequence.length ≤ 104,
1 ≤ sequence[i] ≤ 105.

[output] array.integer

Array a sorted as described above.'''
