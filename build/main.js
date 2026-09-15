(function () {
  "use strict";
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var isOpen = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", isOpen ? "false" : "true");
      toggle.setAttribute("aria-expanded", isOpen ? "false" : "true");
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }
})();
