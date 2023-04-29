export function decryptLink(encrypted: string): string {
  return rot13(transformEncryptionToRot13(encrypted));
}

const LETTER_REGEX = /[a-z]/gi;

function rot13(encrypted: string): string {
  return encrypted.replace(LETTER_REGEX, rotateOneLetter);
}

/** Transforms our proprietary encryption into a rot13 cypher */
function transformEncryptionToRot13(ciphertext: string): string {
  return ciphertext
    .slice(1, -1) // Remove the first and last characters
    .replace(/=pt=/g, "."); // Replace "=pt=" with "."
}

function rotateOneLetter(letter: string): string {
  const charCode = letter.charCodeAt(0);
  const isExceedsM = letter.toLowerCase() > "m";
  return String.fromCharCode(getRotatedCharCode(charCode, isExceedsM));
}

function getRotatedCharCode(charCode: number, isExceedsM: boolean): number {
  return isExceedsM ? charCode - 13 : charCode + 13;
}
