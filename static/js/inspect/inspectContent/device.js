
//var prefix = "/inspect/inspectContent/"
$(function() {
    load();
    /**
     *   平台级用户，控制部门下拉和单位下拉
     **/
    getDeptOrUnitSelect();
});

function load() {

    $('#exampleTable')
        .bootstrapTable(
            {
                method: 'get', // 服务器数据的请求方式 get or post
                url: '/inspect/inspectDevice/listByContentId', // 服务器数据的加载地址
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
                pageSize: 10, // 如果设置了分页，每页数据条数
                pageNumber: 1, // 如果设置了分布，首页页码
                pageList: [10, 20, 50, 100],//可供选择的每页的行数（*）
                search: false, // 是否显示搜索框
                showColumns: false, // 是否显示内容下拉框（选择显示的列）
                sidePagination: "server", // 设置在哪里进行分页，可选值为"client" 或者 "server"
                queryParams: function (params) {
                    return {
                        limit: params.limit,
                        offset: params.offset,
                        runMode: 0,
                        deptId: $('#deptId').val(),
                        unitId: $('#unitId').val(),
                        devType:   $('#devType').val(),
                        devStatus2: $('#devStatus').val(),
                        devId: $('#devId').val(),
                        installPosition: $('#installPosition').val(),
                        contentId: $('#contentId').val()
                    };
                },
                columns : [

                    {
                        checkbox : true,
                        align : 'center',
                        formatter: function (idx, row) {
                            if(row.devStatus == 1){
                                return {
                                    disabled: true
                                }
                            }
                            else {
                                return {
                                    checked : false
                                }
                            }
                        }
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
                            if (row.devStatus == 0) {
                                return '<span>未分配</span>';
                            }
                            else if (row.devStatus == 1) {
                                return '<span>已分配</span>';
                            }
                            else {
                                return '<span>未知</span>';
                            }
                        }
                    },

                    {
                        title: '操作',
                        field: 'id',
                        align: 'center',
                        formatter: function (value, row, index) {
                            var optButn = '';
                            if(row.devStatus == 0) {
                                optButn = '<button class="btn btn-primary btn-xs" onclick="add('
                                    + $('#contentId').val()
                                    + ','
                                    + row.id
                                    + ')"><i class="fa fa-plus" aria-hidden="true"></i>添加</button> ';
                            } else {
                                optType = 1;
                                optButn = '<button class="btn btn-warning btn-xs" onclick="remove2('
                                    + row.type1
                                    + ')"><i class="fa fa-remove" aria-hidden="true"></i>删除</button> ';
                            }
                            var taskType = $('#taskType').val();
                            if (taskType != 1){
                                return optButn;
                            }
                        }
                    }
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


function remove2(cdid) {
    $.ajax({
        url: '/inspect/inspectContentDevice/remove',
        type: "post",
        data: {
            id: cdid
        },
        success: function (resp) {
            if (resp.code == 0) {
                layer.msg(resp.msg);
                refresh();
            } else {
                layer.msg(resp.msg);
            }
        }
    });
}

function add(contentId, devId) {
    $.ajax({
        url: '/inspect/inspectContentDevice/save',
        type: "post",
        data: {
            'contentId': contentId,
            'deviceId': devId
        },
        success: function (resp) {
            if (resp.code == 0) {
                layer.msg(resp.msg);
                refresh();
            } else {
                layer.msg(resp.msg);
            }
        }
    });
}

function addAll() {
    var rows = $('#exampleTable').bootstrapTable('getSelections');
    if (rows.length == 0) {
        layer.msg("请选择要添加的设备数据");
        return;
    }
    if (rows.length > 10) {
        layer.msg("最多允许10个批量设备添加");
        return;
    }

    var ids = new Array();
    $.each(rows, function(i, row) {
        ids[i] = row['id'];
    });
    $.ajax({
        type : 'POST',
        data : {
            "ids" : ids,
            'contentId': $('#contentId').val()
        },
        url : '/inspect/inspectContentDevice/batchAdd',
        success : function(resp) {
            if (resp.code == 0) {
                layer.msg(resp.msg);
                reLoad();
            } else {
                layer.msg(resp.msg);
            }
        }
    });
    
}

