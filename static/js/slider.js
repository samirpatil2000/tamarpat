const sliderCtx = document.getElementById('slide-ctx');

const count = 6;
let currCount = 2;
const nextBtn = document.getElementById('btn-next');
const prevBtn = document.getElementById('btn-prev');

const nextSlide = () => {
  // for (let i = 1; i <= 3; i++) {
  //   document.getElementById(`slide-${i}`).classList.remove('slide-img');
  // }
  if (currCount === count) {
    currCount = 1;
  } else {
    currCount++;
  }
  document.getElementById(`slide-2`).src = `/media/banner-${currCount}.jpeg`;
  document.getElementById(`slide-1`).src = `/media/banner-${
    currCount - 1 === 0 ? count : currCount - 1
  }.jpeg`;
  document.getElementById(`slide-3`).src = `/media/banner-${
    currCount + 1 > count ? 1 : currCount + 1
  }.jpeg`;
};

const prevSlide = () => {
  if (currCount === 1) {
    currCount = count;
  } else {
    currCount--;
  }

  document.getElementById(`slide-1`).src = `/media/banner-${
    currCount === count ? 1 : currCount + 1
  }.jpeg`;
  document.getElementById(`slide-2`).src = `/media/banner-${currCount}.jpeg`;
  document.getElementById(`slide-3`).src = `/media/banner-${
    currCount - 1 === 0 ? count : currCount - 1
  }.jpeg`;
};

nextBtn.addEventListener('click', nextSlide);
prevBtn.addEventListener('click', prevSlide);

setInterval(() => {
  nextSlide();
  // for (let i = 1; i <= 3; i++) {
  //   document.getElementById(`slide-${i}`).classList.add('slide-img');
  // }
}, 3000);

const navBtn = document.getElementById('nav-btn');
const navMobile = document.getElementById('nav-content');
const navOpen = navMobile.style.display;

navBtn.addEventListener('click', () => {
  console.log(navOpen);
});
