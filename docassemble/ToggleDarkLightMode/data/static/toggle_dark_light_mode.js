$(document).ready(function() {
  let dark = false;
  $('#switch').on('click', function () {
    if ( dark === false ) {
      document.documentElement.setAttribute('data-bs-theme', 'dark');
      dark = true;
    } else {
      document.documentElement.setAttribute('data-bs-theme', 'light');
      dark = false;
    }
  });  // ends on #switch click
});