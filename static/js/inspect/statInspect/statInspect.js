
var prefix = "/inspect/statInspect"

function getDateSelect() {
    var curDate = new Date();
    var stringDate = new Date(curDate.getTime() - 24*60*60*1000).Format("yyyy-MM-dd");
    laydate.render({
        elem: '#createTime' //指定元素
        ,value: stringDate
        ,max:new Date(curDate.getTime() - 24*60*60*1000).Format("yyyy-MM-dd")
        ,done: function (value, date) {
        }
    });

    $('#createTime').val(stringDate);

}


function unitSelect() {
    //var dSel = document.getElementById("deptId");
    //var dept = dSel.options[dSel.selectedIndex].value;
    var nSel = document.getElementById("unitId");
    var unit = nSel.options[nSel.selectedIndex].value;
    var uSel = document.getElementById("userId");
    uSel.options.length = 0;
    if( unit != null && unit != '') {
        $.ajax({
            cache : false,
            type : "GET",
            url : "/mobile/mobileUser/inspect",
            data : {
                'unitId': unit
            },
            async : false,
            error : function(request) {
                parent.layer.alert("Connection error");
            },
            success : function( resp ) {
                var json = JSON.stringify(resp);
                var array = jQuery.parseJSON(json);
                if ( array.length <= 0 ) {
                    uSel.options.add(new Option( "请选择...", ''));
                } else {
                    uSel.options.add(new Option( "请选择...", ''));
                    $.each(array, function (index, data) {
                        uSel.options.add(new Option( data.realName, data.mobileId));
                    });
                }
            }
        });
    } else {
        uSel.options.add(new Option( "请选择...",""));
    }
}

$(function () {
    getDeptOrUnitSelect();
    //getDateSelect();
    unitSelect();
    load();
});

function load() {
	$('#exampleTable')
        .bootstrapTable(
            {
                method: 'get', // 服务器数据的请求方式 get or post
                url: prefix + "/list", // 服务器数据的加载地址
                //showRefresh : true,
                cache: false,
                showToggle: true,
                iconSize: 'outline',
                //toolbar : '#exampleToolbar',
                striped: true, // 设置为true会有隔行变色效果
                dataType: "json", // 服务器返回的数据类型
                pagination: true, // 设置为true会在底部显示分页条
                // queryParamsType : "limit",
                // //设置为limit则会发送符合RESTFull格式的参数
                singleSelect: false, // 设置为true将禁止多选
                // contentType : "application/x-www-form-urlencoded",
                // //发送到服务器的数据编码类型
                pageSize: 20, // 如果设置了分页，每页数据条数
                pageNumber: 1, // 如果设置了分布，首页页码
                pageList: [10, 20, 50, 100],//可供选择的每页的行数（*）
                search: false, // 是否显示搜索框
                showColumns: true, // 是否显示内容下拉框（选择显示的列）
                sidePagination: "server", // 设置在哪里进行分页，可选值为"client" 或者 "server"
                queryParams: function (params) {
                    return {
                        //说明：传入后台的参数包括offset开始索引，limit步长，sort排序列，order：desc或者,以及所有列的键值对
                        limit: params.limit,
                        offset: params.offset,
                        deptId: $('#deptId').val(),
                        unitId: $('#unitId').val(),
                        userId: $('#userId').val(),
                        statType: $('#statType').val(),
                        taskType: $('#taskType').val(),
                        taskNo: $('#taskNo').val()

                    };
                },

                columns : [

                    [
                        {

                            field: 'statName',
                            title: "功能分组", //默认值
                            valign: "middle",
                            align: "center",
                            colspan: 1,
                            rowspan: 2
                        },

                        {
                            title: "任务基本情况",
                            valign: "middle",
                            align: "center",
                            colspan: 4,
                            rowspan: 1
                        },
                        {
                            title: "作业执行情况",
                            valign: "middle",
                            align: "center",
                            colspan: 7,
                            rowspan: 1
                        }

                     ],

                    [

                        {
                            field: 'taskStatus0',
                            title: '待执行',
                            align: 'center'
                        },
                        {
                            field: 'taskStatus1',
                            title: '执行中',
                            align: 'center'
                        },
                        {
                            field: 'taskStatus2',
                            title: '已过期',
                            align: 'center'
                        },

                        {
                            field: 'taskCount',
                            title: '任务个数',
                            align: 'center'
                        },
                        {
                            field: 'jobResult0',
                            title: '未完成',
                            align: 'center'
                        },
                        {
                            field: 'jobResult1',
                            title: '已完成',
                            align: 'center'
                        },
                        {
                            field: 'devStatus0',
                            title: '设备正常',
                            align: 'center'
                        },
                        {
                            field: 'devStatus1',
                            title: '设备故障',
                            align: 'center'
                        },
                        {
                            field: 'devRate1',
                            title: '故障率',
                            align: 'center',
                            formatter: function (value, row, index) {
                                return value + '%';
                            }
                        },

                        {
                            field: 'jobRate1',
                            title: '完成率',
                            align: 'center',
                            formatter: function (value, row, index) {
                                return value + '%';
                            }
                        },

                        {
                            field: 'jobCount',
                            title: '作业个数',
                            align: 'center'
                        },
                    ],

                ]

            });

}

function reLoad() {
    updateField('statName', 'statType');//列名、下拉id
    $('#exampleTable').bootstrapTable('refresh');
}
function resets() {
    $('#tjfxForm')[0].reset();
    getDateSelect();
    reLoad();
}

function excel() {
    var index = null;
    $.fileDownload(prefix +"/export",{
        httpMethod: 'POST',
        data:{
            deptId: $('#deptId').val(),
            unitId: $('#unitId').val(),
            userId: $('#userId').val(),
            statType: $('#statType').val(),
            taskType: $('#taskType').val(),
            taskNo: $('#taskNo').val()
        },
        prepareCallback:function(url){
            index = layer.load(1, {
                shade: [0.1,'#fff'] //0.1透明度的白色背景
            });
        },
        successCallback:function(url){
            layer.close(index);
            layer.msg("统计成功,请下载!");
        },
        failCallback: function (html, url) {
            layer.close(index);
            layer.msg("统计失败,请稍后重试或者与管理员联系!");
        }
    });
}
