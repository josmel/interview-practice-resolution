// 1. *Is Unique*:

// Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures?

export default function isUnique(str: string): boolean {
    const letter = str.split("");
    for (let i = 0; i < letter.length; i++) {
      for (let j = i + 1; j < letter.length; j++) {
        if (letter[j] === letter[i]) return false;
      }
    }
    return true;
}
