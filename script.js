// Intersection Observer for scroll animations
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

// Observe all elements with slide-in class
document.addEventListener("DOMContentLoaded", () => {
  const slideElements = document.querySelectorAll(".slide-in");
  slideElements.forEach((el) => observer.observe(el));

  // Add staggered animation delay to checkpoint sections
  document.querySelectorAll(".checkpoint").forEach((checkpoint, index) => {
    const slideIns = checkpoint.querySelectorAll(".slide-in");
    slideIns.forEach((element, i) => {
      element.style.transitionDelay = `${i * 0.15}s`;
    });
  });
});

// Smooth scroll behavior for better checkpoint transitions
let isScrolling;
window.addEventListener("scroll", () => {
  window.clearTimeout(isScrolling);
  isScrolling = setTimeout(() => {
    // Additional scroll-based logic can be added here
  }, 66);
});

// Optional: Add scroll snap for better one-checkpoint-at-a-time viewing
// Uncomment if you want stricter one-checkpoint-at-a-time viewing
/*
const sections = document.querySelectorAll('.checkpoint, .hero-section, .tour-details');
sections.forEach(section => {
    section.style.scrollSnapAlign = 'start';
});
document.documentElement.style.scrollSnapType = 'y mandatory';
*/
