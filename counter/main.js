$( document ).ready(function() {
  var initialValue = 10;
  $('.counter-value').text(initialValue);
  var stateValue = initialValue;

  $('.counter-plus').on('click', function () {
    stateValue++;
    $('.counter-value').text(stateValue);
  });

  $('.counter-minus').on('click', function () {
    if (stateValue > initialValue) {
      stateValue--;
      $('.counter-value').text(stateValue);
      console.log(stateValue)
    }
  });

  $('.counter-reset').on('click', function () {
    if (stateValue >= initialValue) {
      $('.counter-value').text(initialValue);
      stateValue = initialValue;
    }
  });
});

