// Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  // User like button
  const followButton = document.querySelector('a#follow');
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  followButton.addEventListener('click', (e) => {
    e.preventDefault();
    const { id, action } = e.target.dataset;
    const data = {
      id,
      action,
    };
    console.log(data);
    fetch('/users/follow/', {
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
            previous_action == 'follow' ? 'unfollow' : 'follow';

          // toggle follow button animation
          if (previous_action == 'follow') {
            e.target.classList.remove('btn--outline');
            e.target.classList.add('btn--danger');
          } else {
            e.target.classList.remove('btn--danger');
            e.target.classList.add('btn--outline');
          }

          // toggle inner text
          e.target.innerHTML =
            previous_action == 'follow' ? 'Unfollow' : 'Follow';

          // update total followers
          const totalFollowers = document.querySelector('span#followers');
          const previous_followers = parseInt(totalFollowers.innerHTML);

          totalFollowers.innerHTML =
            previous_action == 'follow'
              ? previous_followers + 1
              : previous_followers - 1;
        }
      });
  });
});
