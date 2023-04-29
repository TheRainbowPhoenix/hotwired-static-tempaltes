import { Controller } from "@hotwired/stimulus";

export class ItWorks extends Controller {
  // @ts-ignore
  element: HTMLElement;

  connect() {
    this.element.textContent = "It works!";
  }
}

export class Hello extends Controller {
  static targets = ["name"];

  nameTarget: HTMLInputElement;

  greet() {
    console.log(`Hello, ${this.name}!`);
  }

  get name() {
    return this.nameTarget.value;
  }
}

export const definitions = [
  {
    identifier: "it-works",
    controllerConstructor: ItWorks,
  },
  {
    identifier: "hello",
    controllerConstructor: Hello,
  },
];
