#this is not my code,I copied it
def reverse(root):
  if (root.isEmpty()):
    return root
  temp = root
  prev = None
  while (temp):
    next, temp.next = temp.next, prev
    prev, temp = temp, next
  return prev
