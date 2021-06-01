const scrollDownImg = document.getElementById("chevron-up");
const logo = document.querySelector(".fapislogo")

function scrollDown(){
    let scrollValue = logo.getBoundingClientRect().top;
    scrollDownImg.style.display = "block"
    if (scrollValue < 0){
        scrollDownImg.style.display = "none";
    }
}
