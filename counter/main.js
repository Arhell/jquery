$( document ).ready(function() {
  var initialValue = $('.counter-value').text();

  $('.counter-plus').on('click', function () {
    var plusCount = initialValue++ + 1;
    var countValue = plusCount;
    $('.counter-value').text(countValue);
  })

  $('.counter-minus').on('click', function () {
    if (initialValue >= initialValue) {
      var minusCount = initialValue-- - 1;
      var countValue = minusCount;
      $('.counter-value').text(countValue);
    }
  })

  $('.counter-reset').on('click', function () {
    initialValue = initialValue;
  })

});

