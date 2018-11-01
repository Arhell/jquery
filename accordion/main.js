var multiply = true;
var titleSelector = $('.accordion-title');

function accordion(mode) {
  if (mode == multiply) {
    titleSelector.on('click', function () {
      if($(this).parent().hasClass('active')) {
        $(this).parent().removeClass('active');
      }

      else {
        $(this).parent().addClass('active');
      }
    })
  }

  else {
    titleSelector.on('click', function () {
      $(this).next().toggle();
    })
  }
};

accordion(multiply);