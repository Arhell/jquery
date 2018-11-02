function accordion(mode) {

  var titleSelector = $('.accordion-title');

  mode = mode || 'single';

  if (mode === 'multiply') {
    titleSelector.on('click', function () {

      var itemWrapper = $(this).parent();

      if(itemWrapper.hasClass('active')) {
        itemWrapper.removeClass('active');
      }

      else {
        itemWrapper.addClass('active');
      }
    });
  }

  else if(mode === 'single'){
    titleSelector.on('click', function () {
      $(this).next().toggle();
    });
  }
};

accordion('multiply');
