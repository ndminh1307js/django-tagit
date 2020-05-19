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
});
