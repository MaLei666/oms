
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
                url: '/inspect/inspectDevice/listByUserId', // 服务器数据的加载地址
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
                pageSize:10, // 如果设置了分页，每页数据条数
                pageNumber: 1, // 如果设置了分布，首页页码
                pageList: [10, 20, 50, 100],//可供选择的每页的行数（*）
                search: false, // 是否显示搜索框
                showColumns: false, // 是否显示内容下拉框（选择显示的列）
                sidePagination: "server", // 设置在哪里进行分页，可选值为"client" 或者 "server"
                queryParams: function (params) {
                    return {
                        //说明：传入后台的参数包括offset开始索引，limit步长，sort排序列，order：desc或者,以及所有列的键值对
                        limit: params.limit,
                        offset: params.offset,
                        userId: $('#userId').val(),
                        contentId: $('#contentId').val()
                    };
                },
                columns : [

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
                        field : 'devStatus',
                        title : '设备状态',
                        align: 'center',
                        formatter: function (value, row, index) {
                            if (row.devStatus == 0) {
                                return '<span class="label label-success">正常</span>';
                            } else if (row.devStatus == 1) {
                                return '<span class="label label-warning">故障</span>';
                            } else {
                                return '<span class="label label-info">未知</span>';
                            }
                        }

                    },


                    {
                        field : 'unitNameR',
                        title : '单位名称',
                        align: 'center'
                    },


                    {
                        field : 'installPosition',
                        title : '安装位置',
                        align: 'center'
                    },

                    {
                        field : 'createMobile',
                        title : '录入用户',
                        align: 'center'
                    },

                    {
                        field : 'createTime',
                        title : '录入时间',
                        align: 'center'
                    },


                    {
                        field : 'runMode',
                        title : '运行模式',
                        align: 'center',
                        formatter: function (value, row, index) {
                            if (row.runMode == 0) {
                                return '<span class="label label-success">启用</span>';
                            } else if (row.runMode == 1) {
                                return '<span class="label label-warning">停用</span>';
                            } else {
                                return '<span class="label label-info">未知</span>';
                            }
                        }
                    }
                ]
            });
}
function reLoad() {
    $('#exampleTable').bootstrapTable('refresh');
}

