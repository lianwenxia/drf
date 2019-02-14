function ShowUser() {
    console.log(localStorage.token);
    // alert(sessionStorage.token)
    $.ajax({
        url:'http://127.0.0.1:8000/user/userinfo/',
        type:'GET',
        beforeSend: function(xhr) {
            xhr.setRequestHeader("Authorization", "JWT " + localStorage.token);
        },
        success: function (data) {
               $('#username').html(data['username'])
            str =
         '<li><label>用户名：</label>  <span><input name="" type="text" value='+data['username']+'  class="text"  disabled="disabled" id="name"/></span></li>'+
         '<li><label>真实姓名：</label>  <span><input name="" type="text" value='+data['first_name']+' class="text"  disabled="disabled" id="real_name"/></span></li>'+
          '<li><label>出身日期：</label> <span class="time" id="birth">'+data['birth']+'</span>'+
           '<div class="add_time">'+
             '<select name=""></select><select name=""></select><select name=""></select></div></li>'+
          '<li><label>用户性别：</label> <span class="sex" id="sex">男</span>'+
          '<div class="add_sex">'+
          '<input type="radio" name="sex" value="0" checked="checked">'+
                    '保密&nbsp;&nbsp;'+
                    '<input type="radio" name="sex" value="1">'+
                    '男&nbsp;&nbsp;'+
                    '<input type="radio" name="sex" value="2">'+
                  '女&nbsp;&nbsp;</div></li>'+
          '<li><label>电子邮箱：</label>  <span><input name="" type="text" value='+data['email']+'  class="text"  disabled="disabled" id="email"/></span></li>'+
          '<li><label>用户QQ：</label>  <span><input name="" type="text" value='+data['qq']+'  class="text"  disabled="disabled" id="qq"/></span></li>'+
          '<li><label>移动电话：</label>  <span><input name="" type="text" value='+data['phone']+'  class="text"  disabled="disabled" id="mobile"/></span></li>'+
          '<li><label>固定电话：</label> <span><input name="" type="text" value="455656565"  class="text"  disabled="disabled" id="fixtel"/></span></li>'+
          '<div class="bottom"><input name="" type="button" value="修改信息"  class="modify"/><input name="" type="button" value="确认修改"  class="confirm" onclick="ChangInfo()"/></div>'

        $('#xinxi').html(str)
            alert('ok')
        console.log('ok')
        console.log(data['username'])
            },
        error: function () {
                alert('failed')
            }
    })


}
function ChangInfo(){
    // $('#xinxi').removeClass('hover')
    var username = $('#name').val()
    var first_name = $('#real_name').val()
    var birth = $('#birth').val()
    var qq = $('#qq').val()
    var email = $('#email').val()
    var phone = $('#mobile').val()
    var fixtel = $('#fixtel').val()
    var id = sessionStorage.user_id
    var data_json = {
        'username':username,
        'email':email,
        'phone':phone,
        'first_name':first_name,
        'qq':qq,
        'fixtel':fixtel,
        'birth':birth,
        'id':id,
    }
    trans_str = JSON.stringify(data_json)
    console.log(trans_str)
    $.ajax(
        {
            // url: 'http://127.0.0.1:8000/user/test/',
            url: 'http://127.0.0.1:8000/user/change/',
            type: 'POST',
            beforeSend: function(xhr) {
            xhr.setRequestHeader("Authorization", "JWT " + sessionStorage.token);
            },
            data: trans_str,
            contentType: 'application/json',
            dataType:'json',
            crossDomain: true,
            success: function (data) {
               location.href = '/userinfo.html'
            },
            error: function () {
                alert('failed')
            }
        })

}
$(function () {

    ShowUser();
    $('.modify').live('click',function () {
        $('.text').attr("disabled", false);
	    $('.text').addClass("add");
	    $('#Personal').find('.xinxi').addClass("hover");

    });
})