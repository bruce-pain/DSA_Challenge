from typing import Optional


class Node:
    """
    A single node of a linked list
    """

    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    # Traversal methods
    def print_list(self, detail: str = None) -> None:
        """
        Traverse through the linked list and print out it's contents
        """
        if self.head:
            cursor: Optional[Node] = self.head

            if detail:
                print(f"\n[{detail}]")

            print("-----")

            while cursor is not None:
                print(f"[{cursor.data}]")
                cursor = cursor.next

    # Insertion methods
    def insert_at_head(self, data: int) -> None:
        """
        Insert a new node at the beginning of the linked list
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, data: int) -> None:
        """
        Insert a new node at the end of the linked list
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            cursor = self.head

            while cursor.next is not None:
                cursor = cursor.next

            cursor.next = new_node

    def insert_at_index(self, data: int, index: int) -> None:
        """
        Insert a new node at a position in the linked list
        """

        new_node = Node(data)

        if index == 0:
            self.insert_at_head(data)
        elif index < 0:
            print("InsertError: negative index")
        else:
            counter = 0
            cursor = self.head

            while cursor is not None:
                if counter == (index - 1):
                    temp_node = cursor.next
                    cursor.next = new_node
                    new_node.next = temp_node
                    return
                else:
                    cursor = cursor.next
                    counter += 1

            if counter < index:
                print("InsertError: index out of range")

    # Deletion methods

    def delete_at_head(self) -> None:
        """
        Delete the first element in a linked list
        """

        if self.head:
            self.head = self.head.next

    def delete_at_tail(self) -> None:
        """
        Delete the last element in a linked list
        """

        if self.head:
            cursor = self.head

            while (cursor.next) is not None:
                if cursor.next.next is None:
                    cursor.next = None
                else:
                    cursor = cursor.next
