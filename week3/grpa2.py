def EvaluateExpression(exp):
    s=[]
    for x in exp.split():
       if x.isdigit():
          s.insert(0,str(x))
       else:
          s.insert(0,str(eval(s.pop(1)+x+s.pop(0))))
    return s[0]
