import { hashCode } from "./hashCode";
import { getIndexFromHashcCode } from "./getIndexFromHashCode";
import { LinkedList, LinkedListNode } from "./linkedList";

export class HashTable {
  arr: LinkedList[] = new Array(10);

  // put in hashtable
  put(key: string, value: any): void {
    const keyHashCode: number = hashCode(key);
    const indexFromHashCode: number = getIndexFromHashcCode(
      keyHashCode,
      this.arr
    );

    if (!this.arr[indexFromHashCode]) {
      this.arr[indexFromHashCode] = new LinkedList([key, value]);
    } else {
      let currentLinkedList: LinkedList = this.arr[indexFromHashCode];
      let current: LinkedListNode = currentLinkedList.head;
      let found: boolean = false;
      if (current.data[0] == key) {
        current.data[1] = value;
        found = true;
        return;
      }
      while (current.next) {
        if (current.next.data[0] === key) {
          found = true;
          current.next.data[1] = value;
          return;
        }
        current = current.next;
      }
      if (found === false) {
        currentLinkedList.append([key, value]);
      }
    }
  }

  // get value from hsashtable by key
  get(key: string): any {
    const keyHashCode = hashCode(key);
    const indexFromHashCode: number = getIndexFromHashcCode(
      keyHashCode,
      this.arr
    );
    let linkedListAtIndex = this.arr[indexFromHashCode];
    if (!linkedListAtIndex) {
      return null;
    }
    let found: boolean = false;
    let current: LinkedListNode = linkedListAtIndex.head;
    if (current.data[0] === key) {
      found = true;
      return current.data[1];
    } else {
      while (current.next) {
        if (current.next.data[0] === key) {
          found = true;
          return current.next.data[1];
        } else {
          current = current.next;
        }
      }
    }
    if (found === false) {
      return null;
    }
  }
}

const MyHashTable = new HashTable();
MyHashTable.put("mohamad1", 2010);
MyHashTable.put("mohamad", 1996);
MyHashTable.put("mohamaddd", 2018);
MyHashTable.put("mohamaddd", 202000);
MyHashTable.put("mohamadddd", 2018);
