function getDeptOrUnitSelect(){
	$('#deptId').change(function(){
		var id = $(this).val();
		if (id!==0&&id!=="") {
			$.ajax({
		        type: 'GET',
		        url: '/system/unit/datas?deptId='+ id,
		        async: false,
		        success: function (data) {
		            $('#unitId').empty();
		            var val = '<option value="">请选择...</option>';
		            if(data.length!==0){
		                $.each(data, function(i, v){
			                val+='<option value="'+ v.unitId +'">'+ v.unitName +'</option>';
		                });
		                $('#unitId').append(val);
		            }
		        }
		    });
		}else {
			$('#unitId').empty();
            $('#unitId').append('<option value="">请选择...</option>');
		}

    });

    $('#unitId').change(function(){
        var id = $(this).val();
		if (id !== 0 && id !== "") {
            $.ajax({
                type: 'GET',
                url: '/system/unit/data/'+ id,
                async: false,
                success: function (data) {
                	//var str = JSON.stringify(data);
                	$('#deptId').val(data.deptId);
                }
            });
        }else{
            return;
        }
    });

}

function isNull(val){
    var rval='';
    if (val!==null) {
        rval = val;
    }else{
        rval = '-';
    }
    return rval;
}

/**
*	根据统计类型下拉值，更改table列标题通用方法
*
**/ 
function updateField(fieldName, selectId){
	$("th[data-field='"+ fieldName +"']:first").html($('#'+ selectId).find("option:selected").text());

}
