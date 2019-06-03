// 以下为官方示例
$().ready(function() {
    validateRule();
});

$.validator.setDefaults({
    // submitHandler : function() {
    //     alert(7);
    //     //update();
    // }
});

$("#pwd_save").click(function () {
    if($("#signupForm").valid()){
        $.ajax({
            cache : true,
            type : "POST",
            url : "/sys/user/modPwd",
            data : $('#signupForm').serialize(),// 你的formid
            async : false,
            error : function(request) {
                layer.msg("系统错误，联系管理员",{
                    title : '密码修改',
                    maxmin : false,
                    shadeClose : false, // 点击遮罩关闭层
                    area : [ '300px', '200px' ],
                    time: 20000,
                    btn: ['确定']
                });
            },
            success : function(data) {
                if (data.code == 0) {
                    layer.msg("更新密码成功",{
                        title : '密码修改',
                        maxmin : false,
                        time: 3000
                    });

                    $("#pwdOld").val("");
                    $("#pwdNew").val("");
                    $("#confirm_password").val("");

                } else {
                    layer.msg(data.msg,{
                        title : '密码修改',
                        maxmin : false,
                        shadeClose : false, // 点击遮罩关闭层
                        area : [ '300px', '200px' ],
                        time: 20000,
                        btn: ['确定']
                    });
                }
            }
        });
    }

});


function validateRule() {
    var icon = "<i class='fa fa-times-circle'></i> ";
    $("#signupForm").validate({
        rules : {
            pwdOld : {
                required : true,
                minlength : 6
            },
            pwdNew : {
                required : true,
                minlength : 6
            },
            confirm_password : {
                required : true,
                minlength : 6,
                equalTo : "#pwdNew"
            },
        },

        messages : {
            pwdOld : {
                required : icon + "请输入旧密码",
                minlength : icon + "密码必须6个字符以上"
            },
            pwdNew : {
                required : icon + "请输入新密码",
                minlength : icon + "密码必须6个字符以上"
            },
            confirm_password : {
                required : icon + "请再次输入密码",
                minlength : icon + "密码必须6个字符以上",
                equalTo : icon + "两次输入的密码不一致"
            },
        },

    })
}
