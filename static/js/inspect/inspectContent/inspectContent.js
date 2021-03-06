    var prefix = "/inspect/inspectContent";


    Date.prototype.Format = function (fmt) { //author: meizz
        var o = {
            "M+": this.getMonth() + 1, //月份
            "d+": this.getDate(), //日
            "h+": this.getHours(), //小时
            "m+": this.getMinutes(), //分
            "s+": this.getSeconds(), //秒
            "q+": Math.floor((this.getMonth() + 3) / 3), //季度
            "S": this.getMilliseconds() //毫秒
        };
        if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
        for (var k in o)
            if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
        return fmt;
    };

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

    $(function() {
        load();
        unitSelect();
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
                        taskName: $('#taskName').val(),
                        taskType: $('#taskType').val(),
                        userId: $('#userId').val()
                    };
                },
                columns: [
                    /*{
                        field: 'contentId',
                        title: '任务编号',
                        align: 'center'
                    },*/
                    {
                        field: 'taskName',
                        title: '任务名称',
                        align: 'center'
                    },

                    {
                        field: 'taskType',
                        title: '任务类型',
                        align: 'center',
                        formatter: function (value, row, index) {
                            if (row.taskType == 1) {
                                return '<span class="label label-info">临检</span>';
                            } else if (row.taskType == 2) {
                                return '<span class="label label-info">日检</span>';
                            }  else if (row.taskType == 3) {
                                return '<span class="label label-info">周检</span>';
                            }  else if (row.taskType == 4) {
                                return '<span class="label label-info">月检</span>';
                            }  else if (row.taskType == 5) {
                                return '<span class="label label-info">季检</span>';
                            }  else if (row.taskType == 6) {
                                return '<span class="label label-info">年检</span>';
                            }
                            else {
                                return '<span class="label label-info">未知</span>';
                            }
                        }

                    },

                    {
                        field: 'unitName',
                        title: '单位名称',
                        align: 'center'
                    },

                    {
                        field: 'userName',
                        title: '执行用户',
                        align: 'center'
                    },


                    {
                        field: '',
                        title: '执行时间',
                        align: 'center',
                        formatter: function (value, row, index) {
                            var sdate = new Date(row.startTime.replace(/\-/g, "/"));
                           //alert(sdate);
                            var edate = new Date(row.endTime.replace(/\-/g, "/"));
                            //alert(edate);
                            if (row.taskType == 1) {
                                return sdate.Format("yyyy/MM/dd hh") + " ~ " + edate.Format("yyyy/MM/dd hh");
                            }
                            else {
                                return  sdate.Format("yyyy/MM/dd") + " ~ " + edate.Format("yyyy/MM/dd");
                            }
                        }
                    },

                    {
                        field: 'deviceCount',
                        title: '设备个数',
                        align: 'center',
                        formatter: function (value, row, index) {
                            if (row.deviceCount == null){
                                return '0个';
                            }else{
                                return ''+ row.deviceCount + '个';
                            }
                        }

                    },

                    {
                        field: 'type1',
                        title: '任务模式',
                        align: 'center',
                        formatter: function (value, row, index) {
                            if (row.type1 == 0) {
                                return '<span>启用</span>';
                            } else if (row.type1 == 1) {
                                return '<span>停用</span>';
                            } else {
                                return '<span>未知</span>';
                            }
                        }

                    },

                    {
                        field: 'createUser',
                        title: '创建用户',
                        align: 'center'
                    },

                    {
                        field: 'createTime',
                        title: '创建时间',
                        align: 'center'

                    },



                    {
                        title: '操作',
                        field: 'id',
                        align: 'center',
                        formatter: function (value, row, index) {

                            var r = '<button class="btn btn-success btn-xs '+s_device_h+'" onclick="device(\''
                                + row.contentId
                                + '\')">设备</button> ';
                            var s = '<button class="btn btn-info btn-xs '+s_show_h+'" onclick="show(\''
                                + row.contentId
                                + '\')">详情</button> ';
                            var e = '<button class="btn btn-primary btn-xs '+s_edit_h+'" onclick="edit(\''
                                + row.contentId
                                + '\')">编辑</button> ';
                            var d = '<button class="btn btn-warning btn-xs '+s_remove_h+'" onclick="remove2(\''
                                + row.contentId
                                + '\')">删除</button> ';
                            return s + r + e + d;
                        }
                    }
                    ]
            });
    }

    function reLoad() {
        $('#exampleTable').bootstrapTable('refresh');
    }

    function show(contentId) {
        layer.open({
            type: 2,
            title: '<i class="fa fa-binoculars">&nbsp;任务管理</i>&nbsp; /&nbsp; 详情',
            // maxmin : true,
            shadeClose: false, // 点击遮罩关闭层
            area: ['95%', '95%'],
            content: prefix + '/show' + '/' + contentId // iframe的url
        });
    }

    function device(contentId) {
        layer.open ({
            type: 2,
            title: '<i class="fa fa-binoculars">&nbsp;任务管理</i>&nbsp; /&nbsp; 添加设备',
            maxmin : true,
            shadeClose: false, // 点击遮罩关闭层
            area: ['95%', '95%'],
            content: prefix + '/device' + '/' + contentId,
            end: function () {
                reLoad();
            }
        });
    }

    function add() {
        layer.open({
            type: 2,
            title: '巡检监督 / 任务管理 / 新增任务',
            maxmin: true,
            shadeClose: false, // 点击遮罩关闭层
            area: ['95%', '95%'],
            content: prefix + '/add' // iframe的url
        });
    }

    function edit(id) {
        layer.open({
            type: 2,
            title: '编辑',
            maxmin: true,
            shadeClose: false, // 点击遮罩关闭层
            area: ['95%', '95%'],
            content: prefix + '/edit/' + id // iframe的url
        });
    }

    function remove2(id) {
        layer.confirm('确定要删除选中的记录？', {
            btn: ['确定', '取消']
        }, function () {
            $.ajax({
                url: prefix + "/remove",
                type: "post",
                data: {
                    'contentId': id
                },
                success: function (resp) {
                    if (resp.code == 0) {
                        layer.msg(resp.msg);
                        reLoad();
                    } else {
                        layer.msg(resp.msg);
                    }
                }
            });
        })
    }
