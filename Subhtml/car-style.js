// Add this JavaScript code to your car-style.js
let slideIndex = 0;
const slides = document.querySelectorAll('.slider img');

function showSlide(index) {
  if (index < 0) {
    slideIndex = slides.length - 1;
  } else if (index >= slides.length) {
    slideIndex = 0;
  }

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.transform = `translateX(${100 * (i - slideIndex)}%)`;
  }
}

function nextSlide() {
  slideIndex++;
  showSlide(slideIndex);
}

function prevSlide() {
  slideIndex--;
  showSlide(slideIndex);
}

// Initialize the slider
showSlide(slideIndex);
