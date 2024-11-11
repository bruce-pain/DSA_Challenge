from linked_list import LinkedList

my_list = LinkedList()

my_list.insert_at_tail(56)
my_list.insert_at_tail(89)
my_list.insert_at_tail(123)

my_list.print_list()
my_list.insert_at_index(777, 1)
my_list.print_list()

my_list.delete_at_head()

my_list.print_list()
