import { HashTable } from "./hashTable";

//funciton to check if one string is a permutaiton of the other
// time complexity will be O(nlogn + 2n + n) = O(nlogn + 3n) = O(nlogn)
const isPermutationOne = (string1: string, string2: string): boolean => {
  if (arguments.length !== 2) {
    console.log("This function expected only 2 arguments");
    return false;
  }
  if (string1.length !== string2.length) {
    return false;
  }
  if (string1 === string2) {
    return true;
  }

  // create an aray of characters from each string
  let string1Array = string1.split("");
  let string2Array = string2.split("");

  // sort the array of ASCII charaters
  string1Array.sort();
  string2Array.sort();

  let isPermutation: boolean = true;

  for (let i: number = 0; i < string1Array.length; i++) {
    if (string1Array[i] !== string2Array[i]) {
      isPermutation = false;
      break;
    }
  }

  return isPermutation;
};

// chack is two strings are a pemrutation of each other\
// timne complexit is O(n + n + n) = O(3n) = O(n)
const isPermutationTwo = (string1: string, string2: string): boolean => {
  if (arguments.length !== 2) {
    console.log("This function expects to have two arguments");
    return false;
  }
  if (string1.length !== string2.length) {
    return false;
  }
  if (string1 === string2) {
    return true;
  }
  let isPermutation: boolean = true;
  let myHashTable: HashTable = new HashTable();

  for (let i: number = 0; i < string1.length; i++) {
    if (myHashTable.get(string1.charAt(i)) != null) {
      myHashTable.put(
        string1.charAt(i),
        myHashTable.get(string1.charAt(i)) + 1
      );
    } else {
      myHashTable.put(string1.charAt(i), 1);
    }
  }

  for (let i: number = 0; i < string2.length; i++) {
    if (myHashTable.get(string2.charAt(i)) !== null) {
      myHashTable.put(
        string2.charAt(i),
        myHashTable.get(string2.charAt(i)) - 1
      );
    }
  }

  for (let i = 0; i < myHashTable.arr.length; i++) {
    if (myHashTable.arr[i] !== undefined) {
      if (myHashTable.arr[i].head.data[1] !== 0) {
        isPermutation = false;
        break;
      }
    }
  }
  return isPermutation;
};

let string1: string = "abcdefghijklmnopqrstuvwxyz";
let string2: string = "zyxwvutsrqponmlkjihgfedcba";
console.log(isPermutationOne(string1, string2));
console.log(isPermutationTwo(string1, string2));
