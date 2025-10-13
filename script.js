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

// Navigation active state observer
const navObserverOptions = {
  root: null,
  rootMargin: "-50% 0px -50% 0px",
  threshold: 0,
};

const navObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const id = entry.target.getAttribute("id");
      const navLinks = document.querySelectorAll(".nav-link");
      navLinks.forEach((link) => {
        link.classList.remove("active");
        if (link.getAttribute("href") === `#${id}`) {
          link.classList.add("active");
        }
      });
    }
  });
}, navObserverOptions);

document.addEventListener("DOMContentLoaded", () => {
  const slideElements = document.querySelectorAll(".slide-in");
  slideElements.forEach((el) => observer.observe(el));

  document.querySelectorAll(".checkpoint").forEach((checkpoint, index) => {
    const slideIns = checkpoint.querySelectorAll(".slide-in");
    slideIns.forEach((element, i) => {
      element.style.transitionDelay = `${i * 0.15}s`;
    });
  });

  // Observe all sections for navigation
  const sections = document.querySelectorAll("section[id]");
  sections.forEach((section) => navObserver.observe(section));

  // Smooth scroll for navigation links
  document.querySelectorAll(".nav-link").forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const targetId = link.getAttribute("href");
      const targetSection = document.querySelector(targetId);
      if (targetSection) {
        targetSection.scrollIntoView({ behavior: "smooth" });
      }
    });
  });
});

let isScrolling;
window.addEventListener("scroll", () => {
  window.clearTimeout(isScrolling);
  isScrolling = setTimeout(() => {}, 66);
});
