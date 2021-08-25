// Add to cart button functionality
let addToCartButtons = document.getElementsByClassName("update-cart");

for (let i = 0; i < addToCartButtons.length; i++){
    addToCartButtons[i].addEventListener("click", function(){
      let productId = this.dataset.product
      let action = this.dataset.action
      console.log("Product:", productId, "Action:", action)

      console.log("USER:", user)
        if (user === "AnonymousUser"){
            console.log("Not logged in")
        } else {
            updateUserCart(productId, action)
        }
    })
}

// Update Cart View (POST request)
function updateUserCart(productId, action){
    console.log("User is logged in")

    // where we want to send data to
    let url = "/cart/update_item/"

    // to send our post data
    fetch(url,{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        // data to send to the backend
        body: JSON.stringify({"Product": productId, "Action": action})
    })
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            let cartObject = document.getElementsByClassName('fa-shopping-bag')[0];
            cartObject.innerHTML = " " + data.cnt;
            console.log("data:", data)
            // reload page once our call returns successful
            //location.reload()
        })
}


// Popup views
let popupViews = document.querySelectorAll(".popup-view");
let popupButtons = document.querySelectorAll(".view-button");
let closeButtons = document.querySelectorAll(".close-btn");

// popup quick view button
let popup = function(popupClick) {
    popupViews[popupClick].classList.add("active");
}

popupButtons.forEach((popupButton, i) => {
    popupButton.addEventListener("click", () => {
        popup(i);
    });
});

// popup close button
closeButtons.forEach((closeButton) => {
    closeButton.addEventListener("click", () => {
        popupViews.forEach((popupView) => {
            popupView.classList.remove("active");
        });
    });
});
