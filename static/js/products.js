// Add to cart button
let addToCartButtons = document.getElementsByClassName("update-cart");

for (let i = 0; i < addToCartButtons.length; i++){
    addToCartButtons[i].addEventListener("click", function(){
      let productId = this.dataset.product
      let action = this.dataset.action
      console.log("productId:", productId, "Action:", action)

      console.log("USER:", user)
        if (user === "AnonymousUser"){
            console.log("Not logged in")
        } else {
            console.log("User is logged in")
        }
    })
}
