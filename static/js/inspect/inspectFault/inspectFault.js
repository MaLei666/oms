
var prefix = "/inspect/inspectFault"

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
    var startDate=laydate.render({
        elem: '#BcreateTime',
        value: BdefDate,
        max:EdefDate,
        done:function(value,date){
            if(value!=""){
                date.month=date.month-1;
                endDate.config.min=date;
            }else{
                endDate.config.min=startDate.config.min;
            }
        },
    });
    var endDate=laydate.render({
        elem: '#EcreateTime',
        value: EdefDate,
        min:BdefDate,
        done:function(value,date){
            if(value!=""){
                date.month=date.month-1;
                startDate.config.max=date;
            }else{
                startDate.config.max=endDate.config.max;
            }
        }
    });

    $('#BcreateTime').val(BdefDate);
    $('#EcreateTime').val(EdefDate);
}


$(function() {
    getDeptOrUnitSelect();
    getDateSelect();
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
                        handleUid: $('#userId').val(),
                        installPosition: $('#installPosition').val(),
                        taskType: $('#taskType').val(),
                        devType: $('#devType').val(),
                        handleResult: $('#handleResult').val(),
                        devId: $('#devId').val(),
                        name3: $('#name3').val(),
                        BcreateTime: $('#BcreateTime').val(),
                        EcreateTime: $('#EcreateTime').val()

                    };
                },
						columns : [

                            [
                                {
                                    title: "故障编号",
                                    valign: "middle",
                                    align: "center",
                                    field : 'faultId',
                                    colspan: 1,
                                    rowspan: 2,
                                    formatter: function(value,row,index){
                                        return 'F' + ((Array(9).join('0') + value).slice(-9));
                                    }

                                },

                                {
                                    title: "巡检任务作业",
                                    valign: "middle",
                                    align: "center",
                                    colspan: 6,
                                    rowspan: 1
                                },
                                {
                                    title: "故障处理结果",
                                    valign: "middle",
                                    align: "center",
                                    colspan: 5,
                                    rowspan: 1
                                }
                            ],

                            [
                                /*{
                                    field : 'faultId',
                                    title : '任务名称',
                                    align : 'center'
                                },*/

                            {
                                field : 'taskName',
                                title : '任务名称',
                                align : 'center'
                            },

                            {
                                field : 'taskType',
                                title : '任务类型',
                                align : 'center',
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
                                    field : 'unitName',
                                    title : '单位名称',
                                    align : 'center'
                                },

                            {
                                field : 'devId',
                                title : '设备编号',
                                align : 'center'
                            },

                            {
                                field : 'devName',
                                title : '设备名称',
                                align : 'center'
                            },

                                {
                                    field : 'createTime',
                                    title : '巡检时间',
                                    align : 'center'
                                },

                            {
                                field : 'handleUname',
                                title : '指派用户',
                                align : 'center'
                            },
                            {
                                field : 'handleUphone',
                                title : '联系电话',
                                align : 'center'
                            },

                            {
                                field : 'handleTime',
                                title : '处理时间',
                                align : 'center'
                            },

                            {
                                field : 'handleResult',
                                title : '故障状态',
                                align : 'center',
                                formatter: function (value, row, index) {
                                    if (row.handleResult==null || row.handleResult == 0) {
                                        return '<span>未派发,未处理</span>';
                                    }
                                    else if (row.handleResult == 1) {
                                        return '<span>已派发,未处理</span>';
                                    }
                                    else if (row.handleResult == 2) {
                                        return '<span>已处理</span>';
                                    }
                                    else {
                                        return '<span>未知</span>';
                                    }
                                }
                            },

                            {
									title : '操作',
									field : 'id',
									align : 'center',
									formatter : function(value, row, index) {
                                        var d = '<button class="btn btn-success btn-xs '+s_distribute_h+'" onclick="distribute (\''
                                            + row.faultId
                                            + '\')">派发</button> ';

                                        var f = '<button class="btn btn-xs '+s_distribute_h+'" onclick="javascript:parent.layer.msg(\'' +

                                            '故障编号:' +  row.name3 + '<br/>' + row.comment + '<br/>' + '故障已派发至 ' +row.handleUname + ' 处理'

                                            +'\', {time: 10000, area:[\'600px\'],btn: [\'知道了\'] })">已派</button> ';

                                        var s = '<button class="btn btn-info btn-xs" onclick="show(\''
                                            + row.faultId
                                            + '\')">详情</button> ';

                                        if (row.handleResult ==  null || row.handleResult < 1) {
                                            return s + d;
                                        }
                                        else {
                                            return s + f;
                                        }
									}
								}

								]

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

function show(faultId) {
    layer.open({
        type: 2,
        title: '<i class="fa fa-binoculars">&nbsp;巡检监督&nbsp;/&nbsp;故障处理</i>&nbsp;/&nbsp;详情',
        // maxmin : true,
        shadeClose: false, // 点击遮罩关闭层
        area: ['95%', '98%'],
        content: prefix + '/show' + '/' + faultId // iframe的url
    });
}

function distribute(faultId) {
    layer.open({
        type: 2,
        title: '<i class="fa fa-binoculars">&nbsp;巡检监督 &nbsp;/&nbsp;故障处理</i>&nbsp;/&nbsp;派发',
        // maxmin : true,
        shadeClose: false, // 点击遮罩关闭层
        area: ['95%', '97%'],
        content: prefix + '/distribute' + '/' + faultId // iframe的url
    });
}
