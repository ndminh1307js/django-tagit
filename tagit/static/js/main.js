// Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  // Navigation profile option dropdown
  const option = document.querySelector('.navigation__option i');
  const optionList = document.querySelector('.navigation__option div');

  option.addEventListener('click', () => {
    if (option.classList.contains('open')) {
      option.classList.remove('open');
      optionList.style.display = 'none';
    } else {
      option.classList.add('open');
      optionList.style.display = 'block';
    }
  });

  // User like button
  const likeButtons = document.querySelectorAll('a#like');
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  likeButtons.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const { id, action } = e.target.dataset;
      const data = {
        id,
        action,
      };
      console.log(data);
      fetch('/posts/like/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data['status'] == 'ok') {
            const previous_action = action;

            // toggle data-action
            e.target.dataset.action =
              previous_action == 'like' ? 'unlike' : 'like';

            // toggle like button animation
            if (previous_action == 'like') {
              e.target.classList.add('post__reaction--liked');
            } else {
              e.target.classList.remove('post__reaction--liked');
            }

            // update total likes
            const totalLikes = e.target.childNodes[3];
            const previous_likes = parseInt(totalLikes.innerHTML);

            totalLikes.innerHTML =
              previous_action == 'like'
                ? previous_likes + 1
                : previous_likes - 1;
          }
        });
    });
  });
});
