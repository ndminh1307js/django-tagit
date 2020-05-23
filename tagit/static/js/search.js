const searchTabs = document.querySelectorAll(".search__tab");
const searchResults = document.querySelectorAll(".search__results");

searchTabs.forEach((tab) => {
  tab.addEventListener("click", (e) => {
    const tabName = e.target.id.split("-")[0];
    // Change tab active
    searchTabs.forEach((tab) => {
      if (tab.id == `${tabName}-tab`) {
        if (!tab.classList.contains("search__tab--active")) {
          tab.classList.add("search__tab--active");
        }
      } else {
        if (tab.classList.contains("search__tab--active")) {
          tab.classList.remove("search__tab--active");
        }
      }
    });

    // Display tab content
    searchResults.forEach((result) => {
      if (result.id == `search-${tabName}`) {
        result.style.display = "block";
      } else {
        result.style.display = "none";
      }
    });
  });
});
