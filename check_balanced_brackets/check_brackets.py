def brackets_ok(input_string)->bool:
  stack = []
  for i in input_string:
    if(i == "("):
        stack.append(i)
    else:
      if(stack == []):
        return False
      else:
        if(stack != [] and i == ")"):
          top = stack.pop()
          if(top == "(" and i != ")"):
            return False
  if stack:
    return False
  else:
    return True
if __name__ == "__main__":  
  if brackets_ok("(()"):
    print("Syntax is correct!\n")
  else:
    print("Syntax incorrect!\n")
