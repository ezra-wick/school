$(document).ready(function(){
         console.log("Проверка загрузки документа")

         var buttonSend = document.getElementById('send_form_btn');
         buttonSend.setAttribute('disabled', true)
         var checks = [false,false,false];
         var divErrorPhone = document.createElement('div');
         divErrorPhone.style = "color:red;";
         var divErrorName = document.createElement('div');
         divErrorName.style = "color:red;";
         var divErrorEmail = document.createElement('div');
         divErrorEmail.style = "color:red;";


       function unlock_btn(){
       if (checks[0]==true && checks[1]==true && checks[2]==true){
       buttonSend.removeAttribute("disabled");
       }
       else{
       buttonSend.setAttribute('disabled', true)
       }
       };

         function error_phone (error) {
         if (error!=""){
         divErrorPhone.innerHTML = '<strong>' + error + '</strong>';
         $("#id_phone").after(divErrorPhone);
         document.getElementById("id_phone").style.borderColor="#FF0000";
         checks[0]=false;
         unlock_btn();
         }
         else{
         checks[0]=true;
         unlock_btn();
         document.getElementById("id_phone").style.borderColor="#00FF00";
         divErrorPhone.remove();
         };
         };

         $("#id_phone").on('blur', function(){
         var error = "";
         var my_str = document.getElementById('id_phone').value;
         const is_email = (str)=> /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/.test(str);
         if(!is_email(my_str)){
         error = "Некорректный Телефон!";
         error_phone(error);
         }
         else{
         $.ajax({ /// ajax модуль
         headers: {
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value /// Передаем csrf
      },
         method: 'POST',
         dataType: "html",
         data: {"email": 'none', "phone": my_str}, /// Передаем форму
//         processData: false, /// Соррян это я тебе не написал, это нужно
//         contentType: false, /// тоже
         url: `ajax/validfeeld/`,
         success: function(response){
         response = JSON.parse(response);
         console.log(response.status);
        if (response.status == "ok"){ /// Проверяем статус

           /// Выводим статус в консоль, необязательно.
          error='';
          error_phone(error);
            }
        else {
            error=response.error_phone;

            error_phone(error);
        };
        }
      })
      }
         });

         $("#id_name").on('blur', function(){
         var error = "";
         var str = document.getElementById('id_name').value;
         if (str.length<2){
         error = "Слишком короткое имя!";}
         else{
         if (str[0].match(/^[А-ЯЁ]+$/i)) {
         for (i=0; i<str.length;i++){
               if (!str[i].match(/^[А-ЯЁ]+$/i)) {
                   error = "Неверный формат ввода имени!"
               }
              }
            }
            else{
            if (str[0].match(/^[A-Z]+$/i)) {
                for (i=0; i<str.length;i++){
               if (!str[i].match(/^[A-Z]+$/i)) {
                   error = "Неверный формат ввода имени!"
               }
              }
            }
            else{error = "Неверный формат ввода имени!"}
            }
         }
         if (error!=""){
         divErrorName.innerHTML = '<strong>' + error + '</strong>';
         $("#id_name").after(divErrorName);
         checks[1]=false;
         unlock_btn();
         }
         else{
         checks[1]=true;
         unlock_btn();
         divErrorName.remove();


         }
         });

         function error_email (error) {
         if (error!=""){
         divErrorEmail.innerHTML = '<strong>' + error + '</strong>';
         $("#id_email").after(divErrorEmail);
         document.getElementById("id_email").style.borderColor="#FF0000";
         checks[2]=false;
         unlock_btn();
         }
         else{
         checks[2]=true;
         unlock_btn();
         document.getElementById("id_email").style.borderColor="#00FF00";
         divErrorEmail.remove();
         };
         };

         $("#id_email").on('blur', function(){
         var error = "";
         var my_str = document.getElementById('id_email').value;
         const is_email = (str)=> /^(.+)@(.+).(.+)$/.test(str);
         if(!is_email(my_str)){
         error = "Некорректный email!";
         error_email(error);
         }
         else{
         $.ajax({ /// ajax модуль
         headers: {
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value /// Передаем csrf
      },
         method: 'POST',
         dataType: "html",
         data: {"email": my_str, "phone": "none"}, /// Передаем форму
//         processData: false, /// Соррян это я тебе не написал, это нужно
//         contentType: false, /// тоже
         url: `ajax/validfeeld/`,
         success: function(response){
         response = JSON.parse(response);
         console.log(response.status);
        if (response.status == "ok"){ /// Проверяем статус

           /// Выводим статус в консоль, необязательно.
          error='';
          error_email(error);
            }
        else {
            error=response.error_email;

            error_email(error);
        };
        }
      })
        };





         });

});








