var prefix = "/sys/user"
$(function() {
	var deptId = '';
	load(deptId);
});

function load(deptId) {
	$('#exampleTable')
		.bootstrapTable(
			{
                cache : false,
				method : 'get', // 服务器数据的请求方式 get or post
				url : prefix + "/list", // 服务器数据的加载地址
				// showRefresh : true,
				showToggle : true,
				showColumns : true,
				iconSize : 'outline',
				toolbar : '#exampleToolbar',
				striped : true, // 设置为true会有隔行变色效果
				dataType : "json", // 服务器返回的数据类型
				pagination : true, // 设置为true会在底部显示分页条
				singleSelect : false, // 设置为true将禁止多选
				pageSize : 20, // 如果设置了分页，每页数据条数
				pageNumber : 1, // 如果设置了分布，首页页码
                pageList: [10, 20, 50, 100],//可供选择的每页的行数（*）
				// search : true, // 是否显示搜索框
				sidePagination : "server", // 设置在哪里进行分页，可选值为"client" 或者
				// "server"
				queryParams : function(params) {
					return {
						// 说明：传入后台的参数包括offset开始索引，limit步长，sort排序列，order：desc或者,以及所有列的键值对
						limit : params.limit,
						offset : params.offset,
                        username : $('#searchName').val(),
						deptId : deptId
					};
				},
				columns : [
                    {
                        field : 'userId',
                        title : '用户ID',
                        align : 'center'
                    },
                    {
                        field : 'username',
                        title : '登录账号',
                        align : 'center',
                        formatter : function(value, row, index) {
                            if ( row.deptId == -1 ) {
                                return '******';
                            }
                            else if (row.parentUser != null && (row.roleLevel < row.parentUser.roleLevel)) {
                                return '******';
                            }
                            else {
                                return row.username;
                            }
                        }
                    },
                    {
                        field : 'name',
                        title : '真实姓名',
                        align : 'center',
                        formatter : function(value, row, index) {
                            if ( row.deptId == -1 ) {
                                return '******';
                            }
                            else if (row.parentUser != null && (row.roleLevel < row.parentUser.roleLevel)) {
                                return '******';
                            }
                            else {
                                return row.name;
                            }
                        }
                    },
                    {
                        field : 'roleName',
                        title : '用户角色',
                        align : 'center',
                        formatter : function(value, row, index) {
                            if ( row.deptId == -1 ) {
                                return '******';
                            }
                            else if (row.parentUser != null && (row.roleLevel < row.parentUser.roleLevel)) {
                                return '******';
                            }
                            else {
                                return row.roleName;
                            }
                        }
                    },
                    {
                        field : 'deptName',
                        title : '职能部门',
                        align : 'center',
                        formatter : function(value, row, index) {
                            if ( row.deptId == -1 ) {
                                return '******';
                            }
                            else if (row.parentUser != null && (row.roleLevel < row.parentUser.roleLevel)) {
                                return '******';
                            }
                            else {
                                return row.deptName;
                            }
                        }
                    },
                    {
                        field : 'unitName',
                        title : '单位名称',
                        align : 'center',
                        formatter : function(value, row, index) {
                            if ( row.deptId == -1 ) {
                                return '******';
                            }
                            else if (row.parentUser != null && (row.roleLevel < row.parentUser.roleLevel)) {
                                return '******';
                            }
                            else {
                                return row.unitName;
                            }
                        }
                    },
                    {
                        field : 'mobile',
                        title : '联系方式',
                        align : 'center',
                        formatter : function(value, row, index) {
                            if ( row.deptId == -1 ) {
                                return '******';
                            }
                            else if (row.parentUser != null && (row.roleLevel < row.parentUser.roleLevel)) {
                                return '******';
                            }
                            else {
                                return row.mobile;
                            }
                        }
                    },
					{
						field : 'email',
						title : '邮箱地址',
                        align : 'center',
                        formatter : function(value, row, index) {
                            if ( row.deptId == -1 ) {
                                return '******';
                            }
                            else if (row.parentUser != null && (row.roleLevel < row.parentUser.roleLevel)) {
                                return '******';
                            }
                            else {
                                return row.email;
                            }
                        }
					},
					{
						field : 'status',
						title : '用户状态',
						align : 'center',
						formatter : function(value, row, index) {
                            if ( row.deptId == -1 ) {
                                return '******';
                            }
                            else if (row.parentUser != null && (row.roleLevel < row.parentUser.roleLevel)) {
                                return '******';
                            }
                            else if (value == '0') {
								return '<span class="label label-danger">禁用</span>';
							} else if (value == '1') {
								return '<span class="label label-primary">正常</span>';
							}
						}
					},
                    {
                        field : 'gmtCreate',
                        title : '创建时间',
                        align : 'center',
                        formatter : function(value, row, index) {
                            if ( row.deptId == -1 ) {
                                return '******';
                            }
                            else if (row.parentUser != null && (row.roleLevel < row.parentUser.roleLevel)) {
                                return '******';
                            }
                            else {
                                return row.gmtCreate;
                            }
                        }

                    },
					{
						title : '操作',
						field : 'id',
						align : 'center',
						formatter : function(value, row, index) {
							var userId = $('#userId').val();
							var e = '';
                            var d = '';
                            var f = '';

                            //modify
							if ( row.deptId != null && row.deptId == -1 ) {
                                e = '';
                            }
                            else if (row.userId == userId) {
							    e = '<a  class="btn btn-primary btn-xs ' + s_edit_h + '" href="#" mce_href="#" title="编辑" onclick="edit(\''
                                    + row.userId
                                    + '\')"><i class="fa fa-edit "></i></a> ';
                            }
							else if (row.parentUser != null && (row.roleLevel > row.parentUser.roleLevel)) {
							    e = '<a  class="btn btn-primary btn-xs ' + s_edit_h + '" href="#" mce_href="#" title="编辑" onclick="edit(\''
                                    + row.userId
                                    + '\')"><i class="fa fa-edit "></i></a> ';
							} else {
							    e = '';
                            }

                            //delete
                            if (row.deptId != null && row.deptId == -1) {
                                d = '';
                            }
                            else if (row.userId == userId) {
                                d = '';
                            }
                            else if (row.parentUser != null && (row.roleLevel > row.parentUser.roleLevel)) {
                                d = '<a class="btn btn-warning btn-xs ' + s_remove_h + '" href="#" title="删除"  mce_href="#" onclick="remove2(\''
                                    + row.userId
                                    + '\')"><i class="fa fa-remove"></i></a> ';
                            } else {
                                d ='';
                            }

                            //password
                            if ( row.deptId != null && row.deptId == -1 ) {
                                f = '';
                            }
                            else if (row.userId == userId) {
                                f = '';
                            }
                            else if (row.parentUser != null && (row.roleLevel > row.parentUser.roleLevel))
                            {
                                f = '<a class="btn btn-success btn-xs ' + s_resetPwd_h + '" href="#" title="重置密码"  mce_href="#" onclick="resetPwd(\''
                                    + row.userId
                                    + '\')"><i class="fa fa-key"></i></a> ';
                            } else {
							    f = '';
                            }
							return e + d + f;
						}
					} ]
			});
}
function reLoad() {
	$('#exampleTable').bootstrapTable('refresh');
}
function add() {
	// iframe层
	layer.open({
		type : 2,
		title : '系统管理/增加',
		maxmin : false,
		shadeClose : false, // 点击遮罩关闭层
		area : [ '400px', '260px' ],
        id: 'uer_add0',
        btn: ['下一步','取&nbsp;消'],
        btnAlign: 'c',
        moveType: 1,
        content : prefix + '/add',
        btn1: function(index, layero){
            var body = layer.getChildFrame('body', index);
            var roleId = body.find('#roleId').val();
            if (roleId == '' || roleId == 'null') {
                layer.msg('用户角色不允许为空!', {
                    area : [ '400px', '260px' ],
                    time: 5000,
                    btn: ['确定']
                });
            } else {
                layer.closeAll();
                add1(roleId);
                return;
			}
        },
        btn2: function(index, layero){
            layer.closeAll();
            return;
        },
    });
}

function add1(roleId) {
    layer.open({
        type : 2,
        title : '系统管理/增加',
        maxmin : true,
        shadeClose : false, // 点击遮罩关闭层
        area : [ '800px', '520px' ],
        content : prefix + '/add1/' + roleId
    });
}

function remove2(id) {
	layer.confirm('确定要删除选中的记录？', {
		btn : [ '确定', '取消' ]
	}, function() {
		$.ajax({
			url : "/sys/user/remove",
			type : "post",
			data : {
				'id' : id
			},
			success : function(r) {
				if (r.code == 0) {
					layer.msg(r.msg);
					reLoad();
				} else {
					layer.msg(r.msg);
				}
			}
		});
	})
}
function edit(id) {
	layer.open({
		type : 2,
		title : '系统管理/修改',
		maxmin : true,
		shadeClose : false,
		area : [ '800px', '520px' ],
		content : prefix + '/edit/' + id
	});
}
function resetPwd(id) {
	layer.open({
		type : 2,
		title : '系统管理/密码重置',
		maxmin : false,
		shadeClose : false,
		area : [ '400px', '260px' ],
		content : prefix + '/resetPwd/' + id
	});
}
