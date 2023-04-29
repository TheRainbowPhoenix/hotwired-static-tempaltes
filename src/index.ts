import { Application, Controller } from "@hotwired/stimulus";
import { definitions } from "./controllers";
import * as Turbo from "@hotwired/turbo";
import type { ProductObj } from "./e-commerce";
import ECommerce from "./e-commerce";

declare global {
  interface Window {
    Stimulus: Application;
    dataLayer: Array<object>;
    PromoClick: (object: ProductObj) => void;
  }
}

// application.load(definitionsFromContext(context));

window.Stimulus = Application.start();
window.Stimulus.load(definitions);

window.Stimulus.debug = true;

//   scroller();
new ECommerce();
//   initialiseComponents();
//   notifyMount();
console.debug("index::DOMContentLoaded");
Turbo.session.drive = false;
