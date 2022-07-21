var check_form = function () { /// сама функция

    var form = document.forms['taskitem_form'] /// Подгружаем форму из шаблона
    var formData = new FormData(form) /// Преобразуем форму с помощью FormData для дальнейшей отправки
    $.ajax({ /// ajax модуль
      headers: {
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value /// Передаем csrf
      },
      method: 'POST',
      data: formData, /// Передаем форму
      processData: false, /// Соррян это я тебе не написал, это нужно
      contentType: false, /// тоже
      url: `check/form/`,
      success: function(response){
        if (response.status == 'success'){ /// Проверяем статус
          console.log('success') /// Выводим статус в консоль, необязательно. 
          location.reload() /// Всё хорошо, перезагружаем страницу
            }
        else {
            document.getElementById(`FeedBack`).innerHTML = response /// Вставляем отрендеренный шаблон формы с ошибками в модал
        }
        }
      })}


var options = {
  byRow: false,
  property: 'min-height',
  target: null,
  remove: false
}

$( document ).ready(function() {
  $("div[name='site-card']").matchHeight(options);
  console.log('done')
})
$(window).resize(function() {
  $("div[name='site-card']").matchHeight(options);
  console.log('done')
})
