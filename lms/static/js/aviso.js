$('')
  .focus(function() { $(this).css('background', 'none') })
  .blur(function() { if ($(this)[0].value == '') { $(this).css('background', '#7796ce center center no-repeat') } });

function myFunction() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}