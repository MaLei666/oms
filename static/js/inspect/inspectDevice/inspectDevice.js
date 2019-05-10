
var prefix = "/inspect/inspectDevice"
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
                        unitId: $('#unitId').val(),
                        devType: $('#devType').val(),
                        installPosition: $('#installPosition').val(),
                        devId: $('#devId').val()

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
                                        return '<span>启用</span>';
                                    } else if (row.runMode == 1) {
                                        return '<span>停用</span>';
                                    } else {
                                        return '<span>未知</span>';
                                    }
                                }
                            },

							{
									title : '操作',
									field : 'id',
									align : 'center',
									formatter : function(value, row, index) {
                                        var e = '<button class="btn btn-primary btn-xs '+s_edit_h+'" onclick="edit(\''
                                            + row.id
                                            + '\')">编辑</button> ';

                                        var d = '<button class="btn btn-warning btn-xs '+s_remove_h+'" onclick="remove2(\''
                                            + row.id
                                            + '\')">删除</button> ';

                                        var s = '<button class="btn btn-info btn-xs '+s_show_h+'" onclick="show(\''
                                            + row.id
                                            + '\')">详情</button> ';
										return  s + e + d;
									}
								}
							]
					});
}
function reLoad() {
	$('#exampleTable').bootstrapTable('refresh');
}

function show(id) {
    layer.open({
        type : 2,
        title: '<i class="fa fa-binoculars">&nbsp;设备管理</i>&nbsp; /&nbsp; 详情',
        // maxmin : true,
        shadeClose : false, // 点击遮罩关闭层
        area: ['100%', '100%'],
        content : prefix + '/show' + '/' + id // iframe的url
    });

}

function edit(id) {
	layer.open({
		type : 2,
        title: '<i class="fa fa-binoculars">&nbsp;设备管理</i>&nbsp; /&nbsp; 编辑',
		maxmin : true,
		shadeClose : false, // 点击遮罩关闭层
		area : [ '800px', '520px' ],
		content : prefix + '/edit/' + id // iframe的url
	});
}
function remove2(id) {
	layer.confirm('确定要删除选中的记录？', {
		btn : [ '确定', '取消' ]
	}, function() {
		$.ajax({
			url : prefix+"/remove",
			type : "post",
			data : {
				'id' : id
			},
			success : function(resp) {
				if (resp.code==0) {
					layer.msg(resp.msg);
					reLoad();
				}else{
					layer.msg(resp.msg);
				}
			}
		});
	})
}


function batchRemove() {
	var rows = $('#exampleTable').bootstrapTable('getSelections'); // 返回所有选择的行，当没有选择的记录时，返回一个空数组
	if (rows.length == 0) {
		layer.msg("请选择要删除的数据");
		return;
	}
	layer.confirm("确认要删除选中的'" + rows.length + "'条数据吗?", {
		btn : [ '确定', '取消' ]
	// 按钮
	}, function() {
		var ids = new Array();
		// 遍历所有选择的行数据，取每条数据对应的ID
		$.each(rows, function(i, row) {
			ids[i] = row['id'];
		});
		$.ajax({
			type : 'POST',
			data : {
				"ids" : ids
			},
			url : prefix + '/batchRemove',
			success : function(resp) {
				if (resp.code == 0) {
					layer.msg(resp.msg);
					reLoad();
				} else {
					layer.msg(resp.msg);
				}
			}
		});
	}, function() {

	});
}