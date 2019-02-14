function Login() {
    var username = $('#username').val()
    var password = $('#password').val()
    var data_json = {
        'username':username,
        'password':password,
    }
    trans_str = JSON.stringify(data_json)
    $.ajax(
        {
            url: 'http://127.0.0.1:8000/user/login/',
            type: 'POST',
            data: trans_str,
            contentType: 'application/json',
            dataType:'json',
            success: function (data) {
                // sessionStorage.clear()
                // sessionStorage.token = data.token
                // sessionStorage.username = data.username
                localStorage.clear()
                localStorage.token = data.token
                localStorage.username = data.username
                alert(typeof (data.user_id))

                console.log(data.token)
                console.log(data.username)
               // location.href = '/index.html'
            },
            error: function () {
                alert('用户名或密码错误！')
            }
        })
}
// function getCookie(c_name)
// {
// if (document.cookie.length>0)
//   {
//   c_start=document.cookie.indexOf(c_name + "=")
//   if (c_start!=-1)
//     {
//     c_start=c_start + c_name.length+1
//     c_end=document.cookie.indexOf(";",c_start)
//     if (c_end==-1) c_end=document.cookie.length
//     return unescape(document.cookie.substring(c_start,c_end))
//     }
//   }
// return ""
// }
//
// function setCookie(c_name,value,expiredays)
// {
// var exdate=new Date()
// exdate.setDate(exdate.getDate()+expiredays)
// document.cookie=c_name+ "=" +escape(value)+
// ((expiredays==null) ? "" : ";expires="+exdate.toGMTString())
// }
//
// function checkCookie()
// {
// username=getCookie('username')
// if (username!=null && username!="")
//   {alert('Welcome again '+username+'!')}
// else
//   {
//   username=prompt('Please enter your name:',"")
//   if (username!=null && username!="")
//     {
//     setCookie('username',username,365)
//     }
//   }
// }
