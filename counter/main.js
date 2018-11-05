$( document ).ready(function() {
  var initialValue = $('.counter-value').text();
  var changeValue = initialValue;

  $('.counter-plus').on('click', function () {
    var plusCount = changeValue++ + 1;
    var countValue = plusCount;
    $('.counter-value').text(countValue);
  })

  $('.counter-minus').on('click', function () {
    if (initialValue >= initialValue) {
      var minusCount = changeValue-- - 1;
      var countValue = minusCount;
      $('.counter-value').text(countValue);
    }
  })

  $('.counter-reset').on('click', function () {
    initialValue = initialValue;
  })

});

