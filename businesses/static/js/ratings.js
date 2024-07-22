document.addEventListener('DOMContentLoaded', function() {
    const ratingForms = document.querySelectorAll('.rating-form');
    ratingForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const url = form.action;
            const data = new FormData(form);
            fetch(url, {
                method: 'POST',
                body: data,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': data.get('csrfmiddlewaretoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    form.innerHTML = `Rating submitted: ${data.rating}`;
                }
            });
        });
    });
});
