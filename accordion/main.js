var multiply = true; // Эти переменные относятся к Аккордиону - переси их в тело функции accordion
var titleSelector = $('.accordion-title');

function accordion(mode) {
  if (mode == multiply) { // Используй тройное равно для сравнения
    titleSelector.on('click', function () {
      if($(this).parent().hasClass('active')) { // У тебя по коду несколько раз повторяется $(this).parent() . Закешируй это в переменную с понятным именем и используй ее. А то непонятно что это за элемент да и дублируется код
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

// тебе нужно передавать не переменную, а строку (и в функции сравнивать со строкой)
accordion(multiply);
