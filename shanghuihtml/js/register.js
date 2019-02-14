var send_uuid = ''

function uuid() {

    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "-";

    var uuid = s.join("");
    // console.log(uuid);
    return uuid;

}

function ImgCodeGet(){
    current_code = uuid()
    console.log(current_code)
    new_url = 'http://127.0.0.1:8000/pic_code/' + current_code
    $('#img_code').attr('src',new_url)
    send_uuid = current_code
    console.log(send_uuid)
}
function SendRequest(){
    var rand_str = $('#get_img').val()
    var phone = $('#phone').val()
    var send_url = 'http://127.0.0.1:8000/msg_code/' + phone + '/?uuid=' + send_uuid + '&rand_str=' +rand_str
    // 127.0.0.1:8000/msg_code/(phone)/?uuid={uuid}&rand_str={rand_str}
    $.get(send_url,function (data) {
        alert(data['alert'])
        console.log('ok')
    })
}
function SubmitRequest(){

    // ajax post:


    var username = $('#username').val()
    var password = $('#password').val()
    var password_confirm = $('#password_confirm').val()
    var email = $('#email').val()
    var phone_msg = $('#phone_msg').val()
    var phone = $('#phone').val()
    var data_json = {
        'username':username,
        'password':password,
        'email':email,
        'phone':phone,
        'password_confirm': password_confirm,
        'phone_msg': phone_msg
    }
    trans_str = JSON.stringify(data_json)
    $.ajax(
        {
            url: 'http://127.0.0.1:8000/user/submit/',
            method: 'POST',
            data: trans_str,
            contentType: 'application/json',
            dataType:'json',
            success: function (data) {
                sessionStorage.clear()
                sessionStorage.token = data.token
                alert(data.token)
                // location.href = '/login.html'
               // location.href = '/login.html'
            },
            error: function () {
                alert('failed')
            }
        })


    // serializer ajax get:

    //
    // var send_url = 'http://127.0.0.1:8000/user/submit/'
    // // 127.0.0.1:8000/msg_code/(phone)/?uuid={uuid}&rand_str={rand_str}
    // $.get(send_url,function (data) {
    //     alert(data['alert'])
    //     console.log('ok')
    // })

}
$(function () {
    ImgCodeGet()
})
