---
permalink: script
---
document.addEventListener("DOMContentLoaded", function() {
    const navItems = document.querySelectorAll('.header-nav-item--collection a'); // Adjust selector based on your nav item structure

    navItems.forEach(item => {
      const href = item.getAttribute("href");
      const tooltip = document.createElement('div');
      tooltip.classList.add('header-page-title-tooltip');
      tooltip.innerText = href; // Set the tooltip text to the href value

      const container = document.createElement('div');
      container.classList.add('header-page-title-container');

      // Wrap the nav item in the container
      item.parentNode.insertBefore(container, item);
      container.appendChild(item);
      container.appendChild(tooltip);
    });
  });
</script>