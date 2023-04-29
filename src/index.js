import { Application } from "@hotwired/stimulus";
import { definitions } from "./controllers";
// application.load(definitionsFromContext(context));
window.Stimulus = Application.start();
window.Stimulus.load(definitions);
window.Stimulus.debug = true;
// Turbo.session.drive = false;
