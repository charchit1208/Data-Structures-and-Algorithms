from Linked_List_Implementation import Node, LinkedList

def list_nth_last(linked_list, n):
  linked_list_as_list = []
  current_node = linked_list.head_node
  while current_node:
    linked_list_as_list.append(current_node)
    current_node = current_node.get_next_node()
  print(len(linked_list_as_list))
  return linked_list_as_list[-n-1]

ll = LinkedList(5)
for i in range(10):
  ll.insert_beginning(new_value=i)

#print(ll.stringify_list())
nth_last = list_nth_last(ll, 2)
print(nth_last.value)