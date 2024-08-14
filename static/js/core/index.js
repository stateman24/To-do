let radioSvgs = document.querySelectorAll(".radio-svg");
radioSvgs.forEach(radioSvg => {
    radioSvg.addEventListener("click", function (event){
        event.target.classList.toggle("active")
    })
})