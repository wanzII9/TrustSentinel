var get_url = '/slave_check?plc_id=';
var inject_tmp = 0;
var divisor_tmp = 0;
var index = -1;

$(document).ready(function () {
	function select_data() {
		++index;
		if (index >= plc_arr.length) {
			index = 0;
		}
		$.getJSON(get_url + plc_arr[index], function (response) {
			for(const element of response) {
				if (element['slave_status'] == false) {
					Notify(plc_arr[index] + "에서 미등록 기기가 감지되었습니다.", null, null, 'danger');
				}
			}
		});
		return false;
	}
	var interval = setInterval(select_data, 1000);
});

