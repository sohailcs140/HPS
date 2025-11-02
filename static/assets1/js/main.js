let menuBtn = document.getElementById("menuBtn");
let closeBtn = document.getElementById("closeBtn");
let sideMenu = document.getElementById("sideMenu");

menuBtn.addEventListener("click", () => {
  sideMenu.classList.toggle("sideToggle");
});

closeBtn.addEventListener("click", () => {
  sideMenu.classList.remove("sideToggle");
});
