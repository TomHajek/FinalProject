// Burger-Bar Menu Functionality
$(function() {
    $(".toggler").on("click", function() {
        if ($(".item").hasClass("active")) {
            $(".item").removeClass("active");
        } else {
            $(".item").addClass("active");
        }
    });
});



// Add item to shopping cart

