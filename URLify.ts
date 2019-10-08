// URLIfy a string by replacing spaces with %20
const URLifyOne = (sentence: string): string => {
  if (!sentence) {
    return null;
  }
  let result: string = sentence.replace(/\s/g, "%20");
  return result;
};

// time complexity is O(n)
const URLifyTwo = (sentence: string, length: number): string => {
  if (!sentence) {
    return null;
  }
  //create array
  let trimmedString: string = sentence.substring(0, length);
  let stringArray = trimmedString.split("");

  for (let i: number = 0; i < stringArray.length; i++) {
    if (stringArray[i] === " ") {
      stringArray[i] = "%20";
    }
  }
  let result = stringArray.join("");
  return result;
};
console.log(URLifyOne("mr moham       d"));
console.log(URLifyTwo("mr moham       d", 16));
