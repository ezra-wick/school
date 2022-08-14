subBtn.addEventListener("click", check_form, false);

function check_form (event) { /// сама функция
    event.preventDefault();
    console.log("Вызов")
    var form = document.forms['taskitem_form'] /// Подгружаем форму из шаблона
    var formData = new FormData(form) /// Преобразуем форму с помощью FormData для дальнейшей отправки
    if (window.jQuery){
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
                console.log('success'); /// Выводим статус в консоль, необязательно.
                location.reload(); /// Всё хорошо, перезагружаем страницу
            }
            else {
                document.getElementById(`FeedBack`).innerHTML = response /// Вставляем отрендеренный шаблон формы с ошибками в модал
            }
            }
        })
    }
    else{
    var request = new XMLHttpRequest();
    request.open("POST", 'check/form/', true);
    request.setRequestHeader('X-CSRFToken', document.getElementsByName('csrfmiddlewaretoken')[0].value /// Передаем csrf
);
    request.addEventListener("readystatechange", ()=>{
        if (request.readyState === 4 && request.status=='success'){
        console.log('success'); /// Выводим статус в консоль, необязательно.
        location.reload();
        } ;
        if (request.readyState === 4 && request.status!='success'){
        document.getElementById(`FeedBack`).innerHTML = request.response;
        };
    });
    request.send(formData);
    }
}


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


$( document ).ready(function() {
  $("div[name='bot-card']").matchHeight(options);
  console.log('done')
})
$(window).resize(function() {
  $("div[name='bot-card']").matchHeight(options);
  console.log('done')
})
