document.addEventListener('DOMContentLoaded', function () {
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navLinks.classList.toggle('active');
    });
  }

  const typingText = document.querySelector('.typing-text');
  if (typingText) {
    const text = 'AI & ML Developer';
    let index = 0;

    function typeCharacter() {
      if (index < text.length) {
        typingText.textContent += text.charAt(index);
        index += 1;
        setTimeout(typeCharacter, 120);
      }
    }

    typeCharacter();
  }

  const projectCards = document.querySelectorAll('.project-card');
  projectCards.forEach((card) => {
    card.addEventListener('mouseenter', () => {
      card.style.transform = 'translateY(-8px)';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
});
