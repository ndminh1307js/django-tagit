// Document Loaded
document.addEventListener('DOMContentLoaded', function () {
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

  // POST

  const closeLikesListButtons = document.querySelectorAll('.post__likes span');

  // Close post likes list
  closeLikesListButtons.forEach((closeBtn) => {
    closeBtn.addEventListener('click', (e) => {
      const postId = parseInt(e.target.id.split('-').pop());
      const postLikesList = document.querySelector(`#post-likes-${postId}`);
      postLikesList.style.display = 'none';
    });
  });

  // Open post likes list
  const openLikesListOptions = document.querySelectorAll('a#open-likes-list');

  openLikesListOptions.forEach((openLikesListOption) => {
    openLikesListOption.addEventListener('click', (e) => {
      e.preventDefault();
      const postId = parseInt(e.target.dataset.id);
      const postLikesList = document.querySelector(`#post-likes-${postId}`);
      postLikesList.style.display = 'block';
    });
  });

  // Toggle post options dropdown

  const postOptionButtons = document.querySelectorAll('.post__options i');

  postOptionButtons.forEach((postOptionBtn) => {
    postOptionBtn.addEventListener('click', (e) => {
      const postId = parseInt(e.target.id.split('-').pop());
      const postOptions = document.querySelector(`#post-options-${postId}`);
      const postOptionsItems = document.querySelectorAll(
        `#post-options-list-${postId} ul li`
      );

      postOptionsItems.forEach((postOptionsItem) => {
        postOptionsItem.addEventListener('click', () => {
          postOptions.classList.remove('post__options--open');
        });
      });

      if (postOptions.classList.contains('post__options--open')) {
        postOptions.classList.remove('post__options--open');
      } else {
        postOptions.classList.add('post__options--open');
      }
    });
  });
});
