import { Controller } from "@hotwired/stimulus";
export class ItWorks extends Controller {
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
