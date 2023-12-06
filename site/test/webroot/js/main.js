document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Add a click event on each of them
  $navbarBurgers.forEach( el => {
    el.addEventListener('click', () => {

      // Get the target from the "data-target" attribute
      const target = el.dataset.target;
      const $target = document.getElementById(target);

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');

    });
  });

});


   fetch('/search_index.json')
        .then(response => response.json())
        .then(pages => {
            // pages is now the array of page data from the JSON file

            document.getElementById('searchButton').addEventListener('click', search);
            document.getElementById('searchBox').addEventListener('keyup', function(e) {
                if (e.key === 'Enter') {
                    search();
                }
            });

            function search() {
                // Clear out the previous results
                const resultsDiv = document.getElementById('searchResults');
                resultsDiv.innerHTML = '';

                // Get the user's query
                const query = document.getElementById('searchBox').value.toLowerCase();

                // Search each page's text for the query
                for (let i = 0; i < pages.length; i++) {
                    if (pages[i].body.toLowerCase().includes(query)) {
                        // If the page's text includes the query, add a link to the results
                        const resultLink = document.createElement('a');
                        resultLink.href = pages[i].url;
                        resultLink.textContent = pages[i].title;
                        resultsDiv.appendChild(resultLink);

                        // Add a line break after each result for better readability
                        resultsDiv.appendChild(document.createElement('br'));
                    }
                }
            }
        });





// При загрузке страницы проверьте, была ли ранее выбрана темная тема
if (localStorage.getItem('dark-theme') === 'true') {
  document.body.classList.add('dark-theme');
  document.getElementById('footer').classList.add('dark-theme');
  document.getElementById('theme-icon').classList.remove('fa-moon');
  document.getElementById('theme-icon').classList.add('fa-sun');
}

document.getElementById('color-switcher').addEventListener('click', function () {
  document.body.classList.toggle('dark-theme');
  document.getElementById('footer').classList.toggle('dark-theme');

  // меняем иконку в зависимости от темы
  let themeIcon = document.getElementById('theme-icon');
  if (document.body.classList.contains('dark-theme')) {
    themeIcon.classList.remove('fa-moon');
    themeIcon.classList.add('fa-sun');
    localStorage.setItem('dark-theme', 'true');
  } else {
    themeIcon.classList.remove('fa-sun');
    themeIcon.classList.add('fa-moon');
    localStorage.setItem('dark-theme', 'false');
  }
});






document.querySelectorAll('.copy-code-button').forEach(function(button) {
  button.addEventListener('click', function(e) {
    var pre = e.target.nextElementSibling;
    var code = pre.innerText;
    navigator.clipboard.writeText(code);
  });
});


