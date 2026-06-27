const page = document.body.dataset.page;

document.querySelectorAll("[data-nav]").forEach((link) => {
  if (link.dataset.nav === page) {
    link.classList.add("active");
  }
});

const revealItems = document.querySelectorAll(".reveal");

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.16 }
);

revealItems.forEach((item) => revealObserver.observe(item));

const typingTarget = document.querySelector(".typing-text");
const typingWords = [
  "\"Open to Full-Time Roles\"",
  "\"Available for Freelance Work\"",
  "\"Building with Code and Data\"",
];
let wordIndex = 0;
let charIndex = 0;
let deleting = false;

function typeLoop() {
  if (!typingTarget) {
    return;
  }

  const currentWord = typingWords[wordIndex];

  if (!deleting) {
    typingTarget.textContent = currentWord.slice(0, charIndex + 1);
    charIndex += 1;
    if (charIndex === currentWord.length) {
      deleting = true;
      setTimeout(typeLoop, 1200);
      return;
    }
  } else {
    typingTarget.textContent = currentWord.slice(0, charIndex - 1);
    charIndex -= 1;
    if (charIndex === 0) {
      deleting = false;
      wordIndex = (wordIndex + 1) % typingWords.length;
    }
  }

  setTimeout(typeLoop, deleting ? 45 : 80);
}

typeLoop();
