def trapezoidalRule(l, r, p):

  def calcF(polynome, point):
    value = 0
    power = 1
    for i in range(len(polynome)):
      value += polynome[i]*power 
      power *= point
    return value

  result = 0

  for i in range(l, r):
    result += calcF(p, i) + calcF(p, i + 1)

  return result / 2.0
