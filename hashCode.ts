export function hashCode(str: string): number {
  let hash: number = 0;
  for (let i: number = 0; i < str.length; i++) {
    hash += Math.pow(str.charCodeAt(i) * 31, str.length - i);
    hash = hash & hash; // Convert to 32bit integer
  }
  return hash;
}
