// LIGHTBOX
let gallery = new SimpleLightbox(".photo_gallery a#lightbox");

// DETAILS COLLAPSIBLE BUTTON
let coll = document.getElementsByClassName("collapsible_button");

for (let i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function () {
    this.classList.toggle("active");
    let content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

// SORTING PICTURES
$(function () {
  $("#sortable").sortable();
  $("#sortable").disableSelection();
});
