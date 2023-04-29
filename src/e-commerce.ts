export interface ProductObj {
  name: string;
  id: string;
  creative: string;
  position: string;
  Url: string;
}

export default class ECommerce {
  constructor() {
    window.PromoClick = this.promoClick;

    // Call google analytics event when email field appears
    const email: HTMLElement = document.getElementById("Promo_Email");
    if (email) {
      const observer = new IntersectionObserver(
        (entries: Array<IntersectionObserverEntry>) => {
          if (entries.length && entries[0].intersectionRatio === 1) {
            // Event catched in detail view
            document.dispatchEvent(new CustomEvent("first-promo-email-show"));
            console.log("first-promo-email-show");

            // Send event only once
            observer.unobserve(email);
          }
        },
        {
          threshold: 1.0,
        }
      );
      observer.observe(email);
    }
  }

  promoClick(productObj: ProductObj) {
    window.dataLayer.push({
      event: "clickPromotion",
      ecommerce: {
        promoClick: {
          promotions: [
            {
              name: productObj.name,
              id: productObj.id,
              creative: productObj.creative || "Lien Sponsorise",
              position: productObj.position,
            },
          ],
        },
      },
      eventCallback: function () {
        if (productObj.Url !== "" && productObj.Url != undefined) {
          document.location.href = productObj.Url;
        }
      },
    });
  }
}
