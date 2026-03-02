def is_balanced(s):
    stack=[]
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack:
                return "Not balanced"
            top=stack.pop()
            if(ch=='(' and top !=')') or \
              (ch=='{' and top !='}') or \
              (ch=='[' and top!=']'):
                return "Not balanced"
            if not stack:
                return "Balanced"
            else:
                return "Not Balaced"
            
            
            
            
            
