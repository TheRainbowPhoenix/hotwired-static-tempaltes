import { Controller } from "@hotwired/stimulus";

export class ItWorks extends Controller {
  // @ts-ignore
  element: HTMLElement;

  connect() {
    this.element.textContent = "It works!";
  }
}

export const definitions = [
  {
    identifier: "it-works",
    controllerConstructor: ItWorks,
  },
];
