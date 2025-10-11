const observerOptions = {
  root: null,
  rootMargin: "0px",
  threshold: 0.1,
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
    }
  });
}, observerOptions);

document.addEventListener("DOMContentLoaded", () => {
  const slideElements = document.querySelectorAll(".slide-in");
  slideElements.forEach((el) => observer.observe(el));

  document.querySelectorAll(".checkpoint").forEach((checkpoint, index) => {
    const slideIns = checkpoint.querySelectorAll(".slide-in");
    slideIns.forEach((element, i) => {
      element.style.transitionDelay = `${i * 0.15}s`;
    });
  });
});

let isScrolling;
window.addEventListener("scroll", () => {
  window.clearTimeout(isScrolling);
  isScrolling = setTimeout(() => {
  }, 66);
});
