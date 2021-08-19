const scrollDownImg = document.getElementById("chevron-up");
const logo = document.querySelector(".fapislogo")
const requestButton = document.getElementById("fixed_request_button")

function scrollDown(){
    let scrollValue = logo.getBoundingClientRect().top;
    // console.log("test")
    // console.log(scrollValue)
    scrollDownImg.style.display = "block"
    requestButton.style.display = "block"
    if (scrollValue < 0){
        scrollDownImg.style.display = "none";
        if (scrollValue < -1400){
            requestButton.style.display = "none"
            if (scrollValue < -4650){
                requestButton.style.display = "block"
            }
        }
    }
}