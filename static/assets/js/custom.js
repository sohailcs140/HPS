let btnColapse = document.querySelectorAll(".collapse-btn");

btnColapse.forEach((btn) => {
  btn.addEventListener("click", () => {
    if (!document.body.classList.contains("sidebar-mini")) {
      rclas = ["light", "light-sidebar", "theme-white"];

      for (cls of rclas) {
        document.body.classList.remove(cls);
      }
    }
  });
});
const logo = document.getElementById("logo");
const changeMode = function (isLightMode) {
  classes = ["dark", "dark-sidebar", "theme-black"];
  if(isLightMode){
  for (cls of classes) {
    document.body.classList.add(cls);
  }
  if(logo){
    logo.src = "/static/assets/img/logod.png";
  }

  }else{
      for (cls of classes) {
        document.body.classList.remove(cls);
      }
      if (logo) {
        logo.src = "/static/assets/img/logo.png";
      }
  }

};
let lightMode = true
const isDark = document.getElementById("isDark");
isDark.addEventListener("click", (e) => {

if(lightMode){
  changeMode(lightMode);
  lightMode = false;
 
}else{
  changeMode(lightMode);
  lightMode = true;
}


});







function displayCharacters(text, elementId, delay) {
  var paragraph = document.getElementById(elementId);
  var index = 0;

  function addCharacter() {
    if (index < text.length) {
      paragraph.textContent += text.charAt(index);
      index++;
      setTimeout(addCharacter, delay);
    }
  }

  addCharacter();
}




