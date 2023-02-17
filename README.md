HTML and js for toggling Bootstrap dark and light mode live. You'll probably have to style the switch elements to get something pretty, but this is functional.

The HTML in the footer:
```
---
default screen parts:
  footer: |
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" role="switch" id="switch">
      <label class="form-check-label" for="switch">Switch</label>
    </div>
---
```

The javascript:

```js
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
```
