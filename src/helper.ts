export function copyAttributesAndChildren(
  source: HTMLElement,
  { into }: { into: HTMLElement }
): void {
  // We avoid using slow serialisation to copy the content using append
  const attributes = Array.from(source.attributes);
  for (const attribute of attributes) {
    into.setAttribute(attribute.name, attribute.value);
  }
  const childNodes = Array.from(source.childNodes);
  into.append(...childNodes);
}
