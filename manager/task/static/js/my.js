
function Completed(taskId) {
    fetch(`/completed/${taskId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        }
    }).then(response => {
        if (response.ok) {
            window.location.href = '/history/';
        }
    });
}
