"""
Node Implementation: 
In this program, we are only allowing the value of the node to be set
upon creation. However, we want to allow updating the link of the node.
"""

class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  # Define your get_value and get_link_node methods below:
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# Add your code below:
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

dot.set_link_node(wacko)
yacko.set_link_node(dot)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)