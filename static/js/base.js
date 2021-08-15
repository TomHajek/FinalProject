// Burger-Bar Menu Functionality
$(document).ready(function () {
    $(".toggler").click(function (e) {
        e.preventDefault();
        let liItems = $("li.item");
        if (liItems.hasClass("active")) {
            liItems.removeClass("active");
        } else {
            liItems.addClass("active");
        }
    });
});

// Add item to shopping cart


/*
if item quantity > 1: on click, add item to cart

 */

