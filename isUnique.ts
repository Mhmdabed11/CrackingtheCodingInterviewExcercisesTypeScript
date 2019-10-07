import { HashTable } from "./hashTable";

// is Unique funtion which checks if a string is uniqur or not using hashTable
// time complexity O(n^2)
export const isUnique = (word: string): boolean => {
  let myHashTable: HashTable = new HashTable();
  let unique: boolean = true;

  for (let i: number = 0; i < word.length; i++) {
    if (myHashTable.get(word.charAt(i))) {
      unique = false;
      break;
    }
    myHashTable.put(word.charAt(i), 1);
  }
  return unique;
};

// is Unique functions whichn checks uniqueness of a string using typescript object
// time complexity O(n)
export const isUniqueTwo = (word: string): boolean => {
  let unique: boolean = true;
  let temp: object = {};
  for (let i: number = 0; i < word.length; i++) {
    if (temp[word.charAt(i)]) {
      unique = false;
      break;
    }
    temp[word.charAt(i)] = 1;
  }
  return unique;
};

// is Unique algorithm to determine if a string is unique by comparing all characters
// time complexity (O n^2)
const isUniqueThree = (word: string): boolean => {
  let unique = true;
  for (let i: number = 0; i < word.length; i++) {
    for (let j: number = i + 1; j < word.length; j++) {
      if (word.charAt(j) === word.charAt(i)) {
        unique = false;
        break;
      }
    }
  }
  return unique;
};

// sort asce characters and compare
const isUniqueFour = (word: string): boolean => {
  let unique: boolean = true;
  const array: string[] = word.split("");
  array.sort();
  for (let i: number = 0; i < array.length - 1; i++) {
    if (array[i] === array[i + 1]) {
      unique = false;
      break;
    }
  }
  return unique;
};

console.log(isUnique("abcdefghijklmnopqrstuvwxyz"));
console.log(isUniqueTwo("abcdefghijklmnopqrstuvwxyz123456789"));
console.log(isUniqueThree("d"));
console.log(isUniqueFour("abcdefghijklmnopqrstuvwxyz"));
console.log(isUniqueFour("abcdefghijklmnopqrstuvwxyz123456789"));
console.log(isUniqueFour("d"));
