// static/script.js
function subscribe() {
    const name = document.getElementById('name').value;
    fetch('/subscribe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name }),
    })
    .then(response => response.json())
    .then(data => {
        const notifications = document.getElementById('notifications');
        notifications.innerHTML += `<p>${data.message}</p>`;
    });
}

function publish() {
    const message = document.getElementById('message').value;
    fetch('/publish', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    })
    .then(response => response.json())
    .then(data => {
        const notifications = document.getElementById('notifications');
        notifications.innerHTML += `<p>${data.message}</p>`;
    });
}
