import { Controller } from "@hotwired/stimulus";
import { copyAttributesAndChildren } from "./helper";
import { decryptLink } from "./obfuscator";

export class AtcController extends Controller<HTMLElement> {
  static values = {
    l: String,
    t: String,
  };
  /** L stands for Link */
  readonly lValue: string;
  /** T stands for Target */
  readonly tValue: string;

  connect(): void {
    // We add event on click to hide the action on html because of SEO issue
    this.element.addEventListener("click", this.handleClick);
  }

  disconnect(): void {
    this.element.removeEventListener("click", this.handleClick);
  }

  // We must create an arrow function to avoid binding context because of removeEventListener
  // Binding context creates a new function, it must be the same on add and remove event
  private handleClick = (event: Event): void => {
    event.stopImmediatePropagation();
    this.navigate();
  };

  private navigate(): void {
    this.tValue
      ? window.open(decryptLink(this.lValue), decryptLink(this.tValue))
      : window.open(decryptLink(this.lValue), "_self");
  }
}

export class AtcExperimentController extends Controller<HTMLElement> {
  static values = {
    l: String,
    t: String,
  };
  /** L stands for Link */
  readonly lValue: string;
  /** T stands for Target */
  readonly tValue: string;

  connect(): void {
    const decryptedLink = document.createElement("a");
    copyAttributesAndChildren(this.element, { into: decryptedLink });
    decryptedLink.dataset.controller = decryptedLink.dataset.controller.replace(
      this.identifier,
      ""
    );

    decryptedLink.href = decryptLink(this.lValue);
    if (this.tValue) {
      decryptedLink.target = decryptLink(this.tValue);
    }

    this.element.replaceWith(decryptedLink);
  }
}

window.Stimulus.register("atc", AtcController);
window.Stimulus.register("atc-experiment", AtcExperimentController);
