document.addEventListener('DOMContentLoaded', function() {
    // Get the button that opens the modal
    var btn = document.getElementById("loginBtn");

    // Check if the button exists and jQuery is loaded
    if (btn && typeof $ !== 'undefined') {
        btn.onclick = function() {
            $('#loginModal').modal('show'); // Use jQuery to show the modal
        }
    }
});
