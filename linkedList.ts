// class for a Linked List Node
class LinkedListNode {
  data: any;
  next: LinkedListNode;
  constructor(value: any) {
    this.data = value;
    this.next = null;
  }
}

// class for a Linkedin List
class LinkedList {
  head: LinkedListNode;
  constructor(value: any) {
    this.head = new LinkedListNode(value);
  }
  //append to the end of the linked list
  append(value: any) {
    if (this.head === null) {
      this.head = new LinkedListNode(value);
    }
    let current: LinkedListNode = this.head;
    while (current.next) {
      current = current.next;
    }
    current.next = new LinkedListNode(value);
  }

  //prepend to begining of linked list
  prepend(value: any) {
    if (this.head === null) {
      this.head = new LinkedListNode(value);
    }
    let newHead: LinkedListNode = new LinkedListNode(value);
    newHead.next = this.head;
    this.head = newHead;
  }

  delete(value: any) {
    if (this.head === null) {
      return;
    }
    if (this.head.data === value) {
      this.head = this.head.next;
      return;
    }
    let current: LinkedListNode = this.head;
    while (current && current.next) {
      if (current.next.data === value) {
        current.next = current.next.next;
        return;
      }
      current = current.next;
    }
  }
}

const MyLinkedList = new LinkedList(1);
MyLinkedList.append(2);
MyLinkedList.append(3);
MyLinkedList.delete(1);
console.log(MyLinkedList);
