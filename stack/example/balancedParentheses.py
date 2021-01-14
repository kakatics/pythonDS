from Stack import Stack

def isMatch(p1, p2):
  if p1 == "(" and p2 == ")":
    return True
  elif p1 == "[" and p2 == "]":
    return True
  elif p1 == "{" and p2 == "}":
    return True
  else:
    return False


def isParenthesesBalanced(string):
  s = Stack()
  isBalanced = True

  for letter in string:
    if letter in "([{":
      s.push(letter)
      print("Stack push:", letter)
    else:
      if s.isEmpty():
        isBalanced = False
        break
      else:
        top = s.pop()
        print("Stack pop:", top, "Letter:", letter, end=" ")
        if not isMatch(top, letter):
          isBalanced = False
          print("Don't match")
          break
        print("Match")
  if s.isEmpty() and isBalanced:
    return True
  else:
    return False
