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
    let url = "/update_view/"

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
            console.log("data:", data)
            // reload page once our call returns successful
            location.reload()
        })
}
