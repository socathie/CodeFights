def Committee(h):
    h = [k.split(":") if k[-1]==":" else k.split(": ") for k in h]
    n = [k[0] for k in h]
    l = [k[1].split(", ") if len(k)>1 else "" for k in h]
    
    while True:
        p = []
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j]!="":
                    p.append(l[i][j])
        if len(n)==3:
            print l
        r = []
        d = sorted(n,key = lambda x: p.count(x),reverse = True)
        for i in d:
            if p.count(i)>float(len(n))/2:
                r.append(n.index(i))
        if r==[]:
            break
        r = reversed(sorted(r))
        for i in r:
            del l[i]
            for j in reversed(range(len(l))):
                for k in reversed(range(len(l[j]))):
                    if l[j][k]==n[i]:
                        del l[j][k]
            del n[i]
        if len(n)<=1:
            break
    
    return sorted(n)

'''Several people have formed a committee. It turned out that some members believe that some others are incompetent and should thus be excluded. It was decided to get rid of the incompetent members by the following procedure.

Every committee member has written down a so-called "hate list" - a list of colleagues who he/she considers to be incompetent. The members who are mentioned in more than a half of the "hate lists" are fired with disgrace and their opinion is not taken into account further. The procedure is repeated for as long as the dismissals do not stop.

The committee asked for your help in order to avoid the bureaucracy. Given the hate_lists of all the committee members, find the members that will remain in it after the procedure is finished.

Return the final list of committee members sorted lexicographically.

Example

For

hate_lists = ["Hillary: Donald, Gary", 
              "Donald: Hillary, Gary, Jill", 
              "Gary: Jill", 
              "Jill: Hillary, Donald, Gary"]
the output should be
Committee(hate_lists) = ["Jill"].

In the first round of voting Hillary will be mentioned twice, Donald - twice, Gary - three times, Jill - twice. Thus, only Gary will get the votes of more than half of the committee members. After the dismissal of Gary, in the second round Hillary will receive two black marks, Donald - two, Jill - one. As a result, Hillari and Donald will be excluded and Jill will be the only final member of the committee. Thus the output should be ["Jill"].

For

hate_lists = ["b B: C c, d D, e E",
              "C c: d D, e E",
              "d D: ",
              "e E: ",
              "a A: b B, e E"]
the output should be
Committee(hate_lists) = ["C c", "a A", "b B", "d D"].

In the first round "e E" will be dismissed, and then nobody will receive more then two votes out of four. Thus the output should be ["C c", "a A", "b B", "d D"].

Input/Output

[time limit] 4000ms (py)
[input] array.string hate_lists

Each string represents the hate list written by the one of the committee members. Each list is given in the format "author_of_the_list: incompetent_person1, incompetent_person2, <...>, incompetent_personn".

Constraints:
3 ≤ hate_lists ≤ 80.

[output] array.string

List of committee members after the procedure described above is finished, sorted in lexicographical order.'''
