const status_1 = document.querySelector(".status_1")
const status_2 = document.querySelector(".status_2")
const status_3 = document.querySelector(".status_3")
const status_4 = document.querySelector(".status_4")
const status_5 = document.querySelector(".status_5")

const gucci_bag = document.querySelector(".gucci-bag")
const balenciaga_shoes = document.querySelector(".balenciaga-shoes")
const gucci_shoes = document.querySelector(".gucci-shoes")
const gucci_mini_bag = document.querySelector(".gucci-mini-bag")
const dior_bag = document.querySelector(".dior-bag")

function change_image_gucci_bag(){
    if (status_1.innerText === "Before"){
        status_1.innerText = "After"
        gucci_bag.src = "static/img/gucci_bag_after.png"
    }else if(status_1.innerText === "After"){
        status_1.innerText = "Before"
        gucci_bag.src = "static/img/gucci_bag_before.png"
    }
}

function change_image_balenciaga_shoes(){
    if (status_2.innerText === "Before"){
        status_2.innerText = "After"
        balenciaga_shoes.src = "static/img/balenciaga_shoes_after.png"
    }else if(status_2.innerText === "After"){
        status_2.innerText = "Before"
        balenciaga_shoes.src = "static/img/balenciaga_shoes_before.png"
    }
}

function change_image_gucci_shoes(){
    if (status_3.innerText === "Before"){
        status_3.innerText = "After"
        gucci_shoes.src = "static/img/gucci_shoes_after.png"
    }else if(status_3.innerText === "After"){
        status_3.innerText = "Before"
        gucci_shoes.src = "static/img/gucci_shoes_before.png"
    }
}

function change_image_gucci_mini_bag(){
    if (status_4.innerText === "Before"){
        status_4.innerText = "After"
        gucci_mini_bag.src = "static/img/gucci_mini_bag_after.png"
    }else if(status_4.innerText === "After"){
        status_4.innerText = "Before"
        gucci_mini_bag.src = "static/img/gucci_mini_bag_before.png"
    }
}

function change_image_dior_bag(){
    if (status_5.innerText === "Before"){
        status_5.innerText = "After"
        dior_bag.src = "static/img/dior_bag_after.png"
    }else if(status_5.innerText === "After"){
        status_5.innerText = "Before"
        dior_bag.src = "static/img/dior_bag_before.png"
    }
}