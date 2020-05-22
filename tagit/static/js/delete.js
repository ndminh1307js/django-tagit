// Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  // Delete post
  const deleteButton = document.querySelector('#post-delete-btn');
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  deleteButton.addEventListener('click', (e) => {
    e.preventDefault();

    const postId = parseInt(e.target.dataset.id);

    fetch(`/posts/delete/${postId}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data['status'] == 'ok') {
          window.open('/posts/newsfeed/');
        }
      })
      .catch((err) => console.log(err));
  });
});
