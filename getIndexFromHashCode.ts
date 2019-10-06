export function getIndexFromHashcCode(hashCode: number, array: any[]): number {
  if (!Array.isArray(array)) {
    return;
  }
  let arrayLength: number = array.length;
  let indexFromHashCode: number =
    ((hashCode % arrayLength) + arrayLength) % arrayLength;
  return indexFromHashCode;
}
