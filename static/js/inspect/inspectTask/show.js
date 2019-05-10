
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
                url: '/inspect/inspectJob/list', // 服务器数据的加载地址
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
                        taskId: $('#taskId').val()
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
                        field : 'installPosition',
                        title : '安装位置',
                        align: 'center'
                    },

                    {
                        field : 'execTime',
                        title : '预计执行时间',
                        align: 'center'
                    },

                    {
                        field : 'realTime',
                        title : '实际执行时间',
                        align: 'center'
                    },


                    {
                        field : 'jobResult',//0待执行1已完成2已过期
                        title : '巡检执行结果',
                        align: 'center',
                        formatter: function (value, row, index) {
                            if (row.jobResult == 0) {
                                return '<span>待执行</span>';
                            } else if (row.jobResult == 1) {
                                return '<span>已完成</span>';
                            } else if (row.jobResult == 2) {
                                return '<span>已过期</span>';
                            } else {
                                return '<span>未知</span>';
                            }
                        }
                    }



                ]
            });
}
function reLoad() {
    $('#exampleTable').bootstrapTable('refresh');
}

