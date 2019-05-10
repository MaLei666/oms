
var prefix = "/inspect/inspectJob"

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

function getDateSelect() {
    var BdefDate = new Date().Format("yyyy-MM") + "-01";
    var EdefDate = new Date().Format("yyyy-MM-dd");
    laydate.render({
        elem: '#BcreateTime' //指定元素
        ,value: BdefDate
        ,max:new Date().Format("yyyy-MM-dd")
        ,done: function (value, date) {
        }
    });
   laydate.render({
        elem: '#EcreateTime' //指定元素
        ,value:EdefDate
        ,max:new Date().Format("yyyy-MM-dd")
        ,done: function (value, date) {
         }
      });
    $('#BcreateTime').val(BdefDate);
    $('#EcreateTime').val(EdefDate);
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
                        installPosition: $('#installPosition').val(),
                        jobStatus: $('#jobStatus').val(),
                        devType: $('#devType').val(),
                        jobResult: $('#jobResult').val(),
                        taskType: $('#taskType').val(),
                        taskNo: $('#taskNo').val()

                    };
                },
						columns : [

                            {
                                field : 'taskNo',
                                title : '任务编号',
                                align: 'center'
                            },
                            {
                                field : 'taskType',
                                title : '任务类型',
                                align: 'center',
                                formatter: function (value, row, index) {
                                    if (row.taskType == 1) {
                                        return '<span class="label label-info">临检</span>';
                                    } else if (row.taskType == 2) {
                                        return '<span class="label label-info">日检</span>';
                                    } else if (row.taskType == 3) {
                                        return '<span class="label label-info">周检</span>';
                                    } else if (row.taskType == 4) {
                                        return '<span class="label label-info">月检</span>';
                                    } else if (row.taskType == 5) {
                                        return '<span class="label label-info">季检</span>';
                                    } else if (row.taskType == 6) {
                                        return '<span class="label label-info">年检</span>';
                                    }
                                    else {
                                        return '<span class="label label-info">未知</span>';
                                    }
                                }

                            },
                            {
                                field : 'taskName',
                                title : '任务名称',
                                align: 'center'
                            },

                            {
                                field : 'unitName',
                                title : '单位名称',
                                align: 'center'
                            },
                            {
                                field : 'userName',
                                title : '执行用户',
                                align: 'center'
                            },

                            {
                                field : 'devId',
                                title : '设备编号',
                                align: 'center'
                            },

                            {
                                field : 'devName',
                                title : '设备名称',
                                align: 'center'

                            },


                            {
                                field : 'devStatus',
                                title : '设备状态',
                                align: 'center',
                                formatter: function (value, row, index) {
                                    if (row.devStatus == 0) {
                                        return '<span>正常</span>';
                                    } else if (row.devStatus == 1) {
                                        return '<span>故障</span>';
                                    } else {
                                        return '<span>未知</span>';
                                    }
                                }
                            },

                            {
                                field : 'jobStatus',
                                title : '作业状态',
                                align: 'center',
                                formatter: function (value, row, index) {
                                    if (row.jobStatus == 0) {
                                        if (row.jobResult == null || row.jobResult == 0) {
                                            return '<span class="label label-info">待执行,未完成</span>';
                                        }
                                        else if (row.jobResult == 1) {
                                            return '<span class="label label-warning">待执行,已完成</span>';
                                        }
                                    }
                                    else if (row.jobStatus == 1) {
                                        if (row.jobResult == 0) {
                                            return '<span class="label label-info">执行中,未完成</span>';
                                        }
                                        else if (row.jobResult == 1) {
                                            return '<span class="label label-warning">执行中,已完成</span>';
                                        }
                                        else if (row.jobResult == 2) {
                                            return '<span class="label label-warning">执行中,已删除</span>';
                                        }
                                    }
                                    else if (row.jobStatus == 2) {
                                        if (row.jobResult == 0) {
                                            return '<span class="label label-info">已过期,未完成</span>';
                                        }
                                        else if (row.jobResult == 1) {
                                            return '<span class="label label-warning">已过期,已完成</span>';
                                        }
                                        else if (row.jobResult == 2) {
                                            return '<span class="label label-warning">已过期,任务已删除</span>';
                                        }
                                    }
                                    else {
                                        return '<span>未知</span>';
                                    }
                                }
                            },



                            {
                                field : '',
                                title : '巡检时间',
                                align: 'center',
                                formatter: function (value, row, index) {
                                    var sdate = new Date(row.startTime.replace(/\-/g, "/"));
                                    var edate = new Date(row.endTime.replace(/\-/g, "/"));
                                    if (row.taskType == 1) {
                                        return sdate.Format("yyyy/MM/dd HH") + " ~ " + edate.Format("yyyy/MM/dd HH");
                                    }
                                    else {
                                        return sdate.Format("yyyy/MM/dd") + " ~ " + edate.Format("yyyy/MM/dd");
                                    }
                                }

                            },

                            {
                                field : 'realTime',
                                title : '完成时间',
                                align: 'center',
                                formatter: function (value, row, index) {
                                   return row.realTime;

                                }

                            },


                            {
                                title: '操作',
                                field: 'jobId',
                                align: 'center',
                                formatter: function (value, row, index) {

                                    var s = '<button class="btn btn-info btn-xs" onclick="show(\''
                                        + row.jobId
                                        + '\')">详情</button> ';
                                    return s;
                                }
                            }


]
					});
}
function reLoad() {
	$('#exampleTable').bootstrapTable('refresh');
}
function resets() {
    $('#tjfxForm')[0].reset();
    getDateSelect();
    reLoad();
}
function show(jobId) {
    layer.open({
        type: 2,
        title: '<i class="fa fa-binoculars">&nbsp;&nbsp;巡检监督&nbsp;/&nbsp;作业查询</i>&nbsp;/&nbsp;详情',
        // maxmin : true,
        shadeClose: false, // 点击遮罩关闭层
        area: ['95%', '95%'],
        content: prefix + '/show' + '/' + jobId // iframe的url
    });
}