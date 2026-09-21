'use strict';
const form = document.getElementById('preview-form');
const result = document.getElementById('preview-result');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  form.reset();
  form.hidden = true;
  result.hidden = false;
  result.focus();
});
