document.addEventListener('scroll', function(){
    console.log("test")
    const currentScrollValue = document.documentElement.scrollTop
    const scrolldown = document.querySelector(".chevron-up");
    if (currentScrollValue>300){
        scrolldown.style.display = "none"
    }
})