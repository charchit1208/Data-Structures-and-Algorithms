from Linked_List_Implementation import Node, LinkedList

# nth last node
def nth_last_node(linked_list, n):
  current = None
  tail_pointer = linked_list.head_node
  count = 0
  while tail_pointer:
    tail_pointer = tail_pointer.get_next_node()
    count += 1
    if count >= n+1:
      if current is None:
        current = linked_list.head_node
      else:
        current = current.get_next_node()  
  return current

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Test code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)
