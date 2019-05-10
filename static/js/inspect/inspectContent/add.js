
function getDateSelect( taskType ) {
    if ( taskType == 1  ) {
        laydate.render({
            elem: '#STime' //指定元素
            , value: new Date().Format("yyyy-MM-dd")
            , min: new Date().Format("yyyy-MM-dd")
            , max: '2030-12-31'

        });
        laydate.render({
            elem: '#ETime' //指定元素
            ,value: new Date().Format("yyyy-MM-dd")
            , min: new Date().Format("yyyy-MM-dd")
            , max: '2030-12-31'
        });

        laydate.render({
            elem: '#startHour' //指定元素
            , value: '00:00:00',
            type: 'time'
        });
        laydate.render({
            elem: '#endHour' //指定元素
            , value: '23:59:59'
            ,type: 'time'
        });

    }
    else if (taskType == 2 ) {
        laydate.render({
            elem: '#STime' //指定元素
           , value: new Date().Format("yyyy-MM-dd")
            , min: new Date().Format("yyyy-MM-dd")
            , max: '2030-12-31'
        });
        laydate.render({
            elem: '#ETime' //指定元素
            ,value: new Date().Format("yyyy-12-31")
            , min: new Date().Format("yyyy-MM-dd")
            , max: '2030-12-31'
        });
    }
    else if (taskType == 3 ) {
        laydate.render({
            elem: '#STime' //指定元素
            , value: new Date().Format("yyyy-MM-dd")
            , min: new Date().Format("yyyy-MM-dd")
            , max: '2030-12-31'
        });
        laydate.render({
            elem: '#ETime' //指定元素
            ,value: new Date().Format("yyyy-12-31")
            , min: new Date().Format("yyyy-MM-dd")
            , max: '2030-12-31'
        });
    }
    else if (taskType == 4 ) {
        laydate.render({
            elem: '#STime' //指定元素
            , value: new Date().Format("yyyy-MM")
            , min:  new Date().Format("yyyy-MM")
            , max:  Date.parse('2030-12-31')
            ,type: 'month'
        });
        laydate.render({
            elem: '#ETime' //指定元素
            , value: new Date().Format("yyyy-12")
            , min:  new Date().Format("yyyy-MM")
            , max:  Date.parse('2030-12-31')
            ,type: 'month'
        });
    }
    else if (taskType == 5 ) {
        laydate.render({
            elem: '#STime' //指定元素
            , value: new Date().Format("yyyy")
            , min:  new Date().Format("yyyy")
            , max:  Date.parse('2030-12-31')
            ,type: 'year'
        });
        laydate.render({
            elem: '#ETime' //指定元素
            ,value: new Date().Format("yyyy")
            , min:  new Date().Format("yyyy")
            , max:  Date.parse('2030-12-31')
            ,type: 'year'
        });

    }
    else if (taskType == 6 ) {

        laydate.render({
            elem: '#STime' //指定元素
            , value: new Date().Format("yyyy")
            , min:  new Date().Format("yyyy")
            , max:  Date.parse('2030-12-31')
            ,type: 'year'
        });
        laydate.render({
            elem: '#ETime' //指定元素
            ,value: '2030'
            , min:  new Date().Format("yyyy")
            , max:  Date.parse('2030-12-31')
            ,type: 'year'
        });
    }
}

// function deptSelect() {
//     var uSel = document.getElementById("userId");
//     uSel.options.length = 0;
//     uSel.options.add(new Option( "请选择...",""));
//     destroy();
//
// }


// function unitSelect() {
//     var nSel = document.getElementById("unitId");
//     var unit = nSel.options[nSel.selectedIndex].value;
//    // var dSel = document.getElementById("deptId");
//     //var dept = dSel.options[dSel.selectedIndex].value;
//     var uSel = document.getElementById("userId");
//     uSel.options.length = 0;
//
//     if( unit != null && unit != '') {
//         reLoad();
//     }
//     else {
//         destroy();
//     }
//
//     if( unit != null && unit != '') {
//         $.ajax({
//             cache : false,
//             type : "GET",
//             url : "/mobile/mobileUser/inspect",
//             data : {
//                 'unitId': unit
//             },
//             async : false,
//             error : function(request) {
//                 parent.layer.alert("Connection error");
//             },
//             success : function( resp ) {
//                 var json = JSON.stringify(resp);
//                 var array = jQuery.parseJSON(json);
//                 if ( array.length <= 0 ) {
//                     uSel.options.add(new Option( "请选择...", ''));
//                 } else {
//                     uSel.options.add(new Option( "请选择...", ''));
//                     $.each(array, function (index, data) {
//                         uSel.options.add(new Option( data.realName, data.mobileId));
//                     });
//                 }
//
//             }
//         });
//     } else {
//         uSel.options.add(new Option( "请选择...",""));
//     }
// }
//
// function userSelect() {
//     var nSel = document.getElementById("userId");
//     var index = nSel.selectedIndex; // 选中索引
//     var text = nSel.options[index].text; // 选中文本
//     $("#userName").val(text);
// }

function typeSelect() {
    var nSel = document.getElementById("taskType");
    var sd = document.getElementById("dateDiv");
    var contextS = '';
    var contextE = '';
    var index = nSel.selectedIndex; // 选中索引
    var type = nSel.options[index].value; // 选中文本
    if (type == '1'){
        contextS += '开始时间: ';
        contextS += '';
        contextS += '<input style="width: 100px;text-align: center;" id="STime" name="STime"  type="text" autocomplete="off">';
        contextS += '<input style="width: 100px;text-align: center; margin-left: 10px;" id="startHour" name="startHour"  type="text" autocomplete="off">';
        contextS += '';

        contextE += '结束时间：';
        contextE += '';
        contextE += '<input style="width: 100px;text-align: center" id="ETime" name="ETime"  type="text" autocomplete="off">';
        contextE += '<input style="width: 100px;text-align: center;margin-left: 10px;" id="endHour" name="endHour" type="text" autocomplete="off">';
        contextE += '';
        sd.innerHTML = contextS + '<span style="margin-left: 50px;margin-right: 50px;"></span>' + contextE;
        getDateSelect( type );

    }else if (type == '2'){
        contextS += '开始日期：';
        contextS += '<input style="width: 100px;text-align: center;" id="STime" name="STime" type="text" autocomplete="off">';
        contextE += '结束日期：';
        contextE += '<input style="width: 100px;text-align: center;" id="ETime" name="ETime"  type="text" autocomplete="off">';
        sd.innerHTML = contextS + '<span style="margin-left: 50px;margin-right: 50px;"></span>' + contextE;
        getDateSelect( type );

    } else if (type == '3'){
        contextS += '开始日期：';
        contextS += '<input style="width: 100px;text-align: center;" id="STime" name="STime"  type="text" autocomplete="off">';
        contextE += '结束日期：';
        contextE += '<input style="width: 100px;text-align: center;" id="ETime" name="ETime"  type="text" autocomplete="off">';
        sd.innerHTML = contextS + '<span style="margin-left: 50px;margin-right: 50px;"></span>' + contextE;
        getDateSelect( type );

    } else if (type == '4'){
        contextS += '开始月份：';
        contextS += '<input style="width: 100px;text-align: center;" id="STime" name="STime"  type="text" autocomplete="off">';

        contextE += '结束月份：';
        contextE += '<input style="width: 100px;text-align: center;" id="ETime" name="ETime" type="text" autocomplete="off">';
        sd.innerHTML = contextS + '<span style="margin-left: 50px;margin-right: 50px;"></span>' + contextE;
        getDateSelect( type );

    } else if (type == '5'){
        contextS += '开始季度：';
        contextS += '<input style="width: 100px;text-align: center;" id="STime" name="STime"  type="text" autocomplete="off">';
        contextS += '<select id="startJd" name="startJd" style="width: 100px;height: 23px; text-align: center;margin-left: 10px;" >';
        contextS +=  '<option value="01-01 00:00:00">一季度</option>';
        contextS +=  '<option value="04-01 00:00:00">二季度</option>';
        contextS +=  '<option value="07-01 00:00:00">三季度</option>';
        contextS +=  '<option value="10-01 00:00:00">四季度</option>';
        contextS += '</select>';

        contextE += '结束季度：';
        contextE += '<input style="width: 100px;text-align: center;" id="ETime" name="ETime"  type="text" autocomplete="off">';
        contextE += '<select id="endJd" name="endJd" style="width: 100px; height: 23px;text-align: center;margin-left: 10px;" >';
        contextE +=  '<option value="03-31 23:59:59">一季度</option>';
        contextE +=  '<option value="06-30 23:59:59">二季度</option>';
        contextE +=  '<option value="09-30 23:59:59">三季度</option>';
        contextE +=  '<option value="12-31 23:59:59" selected>四季度</option>';
        contextE += '</select>';
        sd.innerHTML = contextS + '<span style="margin-left: 50px;margin-right: 50px;"></span>' + contextE;
        getDateSelect( type );

    } else if (type == '6'){

        contextS += '开始年份：';
        contextS += '<input  style="width: 100px;text-align: center;" id="STime" name="STime"  type="text" autocomplete="off">';
        contextE += '结束年份：';
        contextE += '<input  style="width: 100px;text-align: center;" id="ETime" name="ETime"  type="text" autocomplete="off">';

        sd.innerHTML = contextS + '<span style="margin-left: 50px;margin-right: 50px;"></span>' + contextE;
        getDateSelect( type );

    }else{
        sd.innerHTML = '';
    }
}

$().ready(function() {
	validateRule();
    getDeptOrUnitSelect();
    unitSelect();
});

$.validator.setDefaults({
	submitHandler : function() {
		save();
	}
});
function save() {
    var stime = '';
    var etime = '';
    var nSel = document.getElementById("taskType");
    var index = nSel.selectedIndex;
    var type = nSel.options[index].value;
    if (type == '1') {
        stime = $('#STime').val() + ' ' + $('#startHour').val();
        etime = $('#ETime').val()   + ' ' + $('#endHour').val();
    }
    else if (type == '2') {
        stime = $('#STime').val() + ' 00:00:00';
        etime = $('#ETime').val()   + ' 23:59:59';
    }
    else if (type == '3') {
        stime = $('#STime').val() + ' 00:00:00';
        etime = $('#ETime').val()   + ' 23:59:59';
    }
    else if (type == '4') {
        stime = $('#STime').val() + '-01 00:00:00';
        etime = $('#ETime').val()   + '-01 23:59:59';
    }
    else if (type == '5') {
        stime = $('#STime').val() + '-' + $('#startJd').val();
        etime = $('#ETime').val()   + '-' + $('#endJd').val();
    }
    else if (type == '6') {
        stime = $('#STime').val() + '-01-01 00:00:00 ';
        etime = $('#ETime').val()   + '-12-31 23:59:59';
    }

    $('#startTime').val(stime);
    $('#endTime').val(etime);


    /*
    构建设备devids
    */
    var rows = $('#exampleTable').bootstrapTable('getSelections');
    // if (rows.length == 0) {
    //     layer.msg("新建任务至少包含一个巡检设备");
    //     return;
    // }

    var name3 = '';
    var dids = new Array();
    $.each(rows, function(i, row) {
        dids[i] = row['id'];
        name3 = name3 + row['id'] + ',';
    });
    $('#name3').val(name3);

    $.ajax({
		cache : true,
		type : "POST",
		url : "/inspect/inspectContent/save",
        data : $('#signupForm').serialize(),
		async : false,
		error : function(request) {
			parent.layer.alert("Connection error");
		},
		success : function(data) {
			if (data.code == 0) {
				parent.layer.msg("操作成功");
				parent.reLoad();
				var index = parent.layer.getFrameIndex(window.name); // 获取窗口索引
				parent.layer.close(index);

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
            deptId : {
				required : true
			},
            unitId : {
                required : true
            },
            taskName : {
                required : true
            },
            taskType : {
                required : true
            },
            startTime : {
                required : true
            },
            endTime : {
                required : true
            },
            userId: {
                required : true
            }
		},
		messages : {
            deptId : {
				required : icon + "请选择职能部门"
			},
            unitId : {
                required : icon + "请选择单位名称"
            },
            taskName : {
                required : icon + "请输入任务名称"
            },
            taskType : {
                required : icon + "请选择任务类型"
            },
            startTime : {
                required : icon + "请选择任务开始时间"
            },
            endTime : {
                required : icon + "请选择任务结束时间"
            },
            userId : {
                required : icon + "请选择任务执行人员"
            }
		}
	})
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////

function load() {
    // var deptId = $('#deptId').val();
    // var unitId = $('#unitId').val();
    // if (deptId == null || unitId == null || deptId == '' || unitId == ''){
    //         layer.msg("巡检部门或巡检单位不允许为空!");
    //         return;
    // }

    $('#exampleTable')
        .bootstrapTable(
            {
                method: 'get', // 服务器数据的请求方式 get or post
                url: '/inspect/inspectDevice/list', // 服务器数据的加载地址
                //showRefresh : true,
                cache: false,
                showToggle: false,
                //showColumns : true,
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
                pageSize: 1000, // 如果设置了分页，每页数据条数
                pageNumber: 1, // 如果设置了分布，首页页码
                pageList: [1000,1500,2000],//可供选择的每页的行数（*）
                search: false, // 是否显示搜索框
                showColumns: false, // 是否显示内容下拉框（选择显示的列）
                sidePagination: "server", // 设置在哪里进行分页，可选值为"client" 或者 "server"
                queryParams: function (params) {
                    return {
                        limit: params.limit,
                        offset: params.offset,
                        runMode: 0,
                        //deptId: $('#deptId').val(),
                        unitId: $('#unitId').val(),
                        devType:   $('#devType').val(),
                        devStatus: $('#devStatus').val(),
                        devId: $('#devId').val(),
                        installPosition: $('#installPosition').val()
                    };
                },
                columns : [

                    {
                        checkbox : true,
                        align : 'center'
                    },

                    {
                        field : 'unitName',
                        title : '单位名称',
                        align: 'center'
                    },

                    {
                        field : 'devId',
                        title : '设备编号',
                        align: 'center'
                    },

                    {
                        field : 'typeName',
                        title : '设备类型',
                        align: 'center'

                    },

                    {
                        field : 'devName',
                        title : '设备名称',
                        align: 'center'
                    },

                    {
                        field : 'installPosition',
                        title : '安装位置',
                        align: 'center'
                    },

                    {
                        field : 'devStatus',
                        title : '设备状态',
                        align: 'center',
                        formatter: function (value, row, index) {
                            if (value == 0) {
                                return '<span>正常</span>';
                            }
                            else if (value == 1) {
                                return '<span>故障</span>';
                            }
                            else {
                                return '<span>未知</span>';
                            }
                        }
                    },

                ]
            });
}

function reLoad() {
    $("#exampleTable").bootstrapTable('destroy');
    load();
}

function refresh() {
    $('#exampleTable').bootstrapTable('refresh');
}

function destroy() {
    $("#exampleTable").bootstrapTable('destroy');
}


