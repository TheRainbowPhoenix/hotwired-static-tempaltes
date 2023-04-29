import { Application, Controller } from "@hotwired/stimulus";
import { definitions } from "./controllers";
import * as Turbo from "@hotwired/turbo";

declare global {
  interface Window {
    Stimulus: Application;
  }
}

// application.load(definitionsFromContext(context));

window.Stimulus = Application.start();
window.Stimulus.load(definitions);

window.Stimulus.debug = true;

// Turbo.session.drive = false;
