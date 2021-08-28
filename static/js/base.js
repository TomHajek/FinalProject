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


// Set/Query user - if user is not logged in, the value will be "AnonymousUser"
let user = "{{ request.user }}"

// from django documentation for json post request
function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getToken('csrftoken');
