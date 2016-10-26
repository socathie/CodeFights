#def arkanum(ingredients, products, inventory):
#    results = [[inventory,[]]]
#    while 1:
#        temp = []
#        for x in results:
#            for i in range(len(ingredients)):
#                m = [a-b for a,b in zip(x[0],ingredients[i])]
#                if all(item >= 0 for item in m):
#                    temp += [[[a+b for a,b in zip(m,products[i])],x[1]+[i]]]
#                results = temp
#                k = [a[1] for a in results if a[0][0]>0]
#        if len(k) > 0:
#            return k[0]

def E(x,y):
    b = True
    for i in range(len(x)):
        if y[i]>x[i]:
            b = False
    return b

def arkanum(I, p, s):
    P = len(p)
    n = []
    for i in range(P):
        n += [[x-y for (x,y) in zip(p[i],I[i])]]
        if p[i][0]>0:
            k = i
    
    o = [[i] for i in range(P) if E(s,I[i])]
    t = []
    for O in o:
        t += [[i+j for (i,j) in zip(s,n[O[0]])]]
    s = t[:]
    
    while True:
        O = []
        S = []
        for j in range(len(s)):
            a = [[i] for i in range(P) if E(s[j],I[i])]
            A = len(a)
            if [k] in a:
                return o[j]+[k]
            b = [o[j][:] for i in range(A)]
            c = []
            for i in range(A):
                b[i] += [a[i][0]]
                c += [[x+y for (x,y) in zip(s[j],n[a[i][0]])]]
            O += b
            S += c
        o = O[:]
        s = S[:]

'''You are studying alchemy and want to create the philosopher's stone. You have a grimoire full of recipes for the transmutations. Being methodical, you numbered all ingredients starting from 0 (where 0 is the philosopher's stone), and wrote down all the transmutations in terms of ingredients required to perform them and their products. Thus, for each recipe t from the grimoire you know that it requires ingredient[t] ingredients, and that it produces product[t] ingredients after the transmutation.


You can perform a transmutation t only if you have enough ingredients in your inventory. More formally, for each ingredient i it should be true that inventory[i] ≥ ingredient[t][i].

When the transmutation is performed, the ingredients are consumed and the products are created. More formally, for each ingredient i your inventory changes as follows:

inventory[i] = inventory[i] - ingredient[t][i] + products[t][i]
You want to compute the shortest sequence of transmutations that produces the stone. Write a function that will find this number and return the the number of transmutations in the order they should be performed.

It is guaranteed that it is possible to create the philosopher's stone.
The shortest solution is guaranteed to be unique.


Example

For

ingredients = [ 
   [ 0, 8, 0, 0, 0, 0 ], 
   [ 0, 0, 3, 5, 9, 3 ], 
   [ 0, 8, 2, 5, 8, 1 ], 
   [ 0, 3, 0, 0, 4, 5 ], 
   [ 0, 0, 1, 4, 0, 0 ], 
   [ 0, 0, 0, 1, 0, 0 ]
]
,

products = [ 
   [ 0, 6, 3, 0, 4, 0 ], 
   [ 4, 4, 0, 5, 3, 9 ], 
   [ 0, 1, 4, 3, 4, 8 ], 
   [ 0, 5, 0, 9, 0, 0 ], 
   [ 0, 4, 0, 7, 0, 3 ], 
   [ 0, 0, 0, 0, 2, 7 ]
]
and inventory = [ 0, 6, 8, 4, 2, 0 ], the output should be
arkanum(ingredients, products, inventory) = [4, 0, 0, 1].

There are 6 recipes in the grimoire, which use 6 ingredients. Here's the fastest way to get the philosopher's stone:

Apply the 4th transmutation. Your inventory becomes [0, 10, 7, 7, 2, 3 ].
Apply the 0th transmutation twice. Your inventory becomes [ 0, 6, 13, 7, 10, 3 ].
Finally, apply transmutation 1 to end up with inventory [ 4, 10, 10, 7, 4, 9 ].
Input/Output

[time limit] 4000ms (py)
[input] array.array.integer ingredients

Rectangular matrix representing necessary quantity of ingredients for each transmutation.

Constraints:
2 ≤ ingredients.length ≤ 15,
ingredients[t].length = inventory.length,
0 ≤ ingredient[t][i] ≤ 30.

[input] array.array.integer products

Rectangular matrix representing quantity of each ingredient produced by each transmutation.

Constraints:
products.length = ingredients.length,
products[t].length = inventory.length,
0 ≤ products[t][i] ≤ 30.

[input] array.integer inventory

Initial quantity of each ingredient in your inventory.

Constraints:
2 ≤ inventory.length ≤ 15,
0 ≤ inventory[i] ≤ 30.

[output] array.integer

Shortest sequence of transmutations needed to produce the stone.'''
