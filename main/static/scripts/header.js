document.addEventListener("DOMContentLoaded", () => {
  const header = document.getElementById("header");
  let isHeaderHidden = false;

  document.body.addEventListener("click", (event) => {
    if (!header.contains(event.target)) {
      if (isHeaderHidden) {
        header.classList.remove("hidden");
      } else {
        header.classList.add("hidden");
      }
      isHeaderHidden = !isHeaderHidden;
    }
  });

  window.addEventListener("scroll", () => {
    if (window.scrollY === 0 && isHeaderHidden) {
      header.classList.remove("hidden");
      isHeaderHidden = false;
    }
  });
});


  document
    .querySelector(".profile-link")
    .addEventListener("click", function (event) {
      event.preventDefault();
      const dropdownMenu = document.querySelector(".menu");
      dropdownMenu.classList.toggle("show");
    });

  document.addEventListener("click", function (event) {
    const dropdownMenu = document.querySelector(".menu");
    if (!event.target.closest(".dropdown-menu-container")) {
      dropdownMenu.classList.remove("show");
    }
  });