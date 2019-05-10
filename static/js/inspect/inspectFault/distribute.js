function getDateSelect() {
    var stime = '';
    var etime = '';
    laydate.render({
        elem: '#startTime' //指定元素
        , value: new Date().Format("yyyy-MM-dd")
        , min: new Date().Format("yyyy-MM-dd")
        , max: '2030-12-31'

    });
    laydate.render({
        elem: '#endTime' //指定元素
        , value: new Date().Format("yyyy-12-31")
        , min: new Date().Format("yyyy-MM-dd")
        , max: '2030-12-31'
    });
    stime = $('#startTime').val();
    etime = $('#endTime').val();

    $('#startTime').val(stime);
    $('#endTime').val(etime);
}

$().ready(function() {
    validateRule();
    getDateSelect();
});

$.validator.setDefaults({
    submitHandler : function() {
        update();
    }
});


function distribute() {
    $.ajax({
        cache : true,
        type : "POST",
        url : "/inspect/inspectFault/updateByDistribute",
        data : $('#signupForm').serialize(),// 你的formid
        async : false,
        error : function(request) {
            parent.layer.alert("Connection error");
        },
        success : function(data) {
            if (data.code == 0) {

                var index = parent.layer.getFrameIndex(window.name); // 获取窗口索引
                parent.layer.close(index);
                parent.reLoad();
                parent.layer.msg("派发成功");

            } else {
                parent.layer.alert(data.msg)
            }

        }
    });

}
function validateRule() {
    var icon = "<i class='fa fa-times-circle'></i> ";
    $("#signupForm").validate({
        rules : {
            handleUid : {
                required : true
            },
            startTime : {
                required: true
            },
            endTime : {
                required : true
            }
        },
        messages : {
            handleUid : {
                required : icon + "请选择派发人员"
            },
            startTime : {
                required : icon + "请选择开始时间"
            },
            endTime : {
                required : icon + "请选择结束时间"
            }
        }
    })
}