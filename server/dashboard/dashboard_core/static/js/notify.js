Notify = function(text, callback, close_callback, style) {
	var $container = $('#notifications');
	var icon = '<i class="fa fa-exclamation-triangle" aria-hidden="true" style="padding-right: 0.5rem"></i>';
 
	if (typeof style == 'undefined' ) style = 'warning'
  
	var html = $('<div id="main_alert" class="alert alert-dismissible alert-' + style + '">' + icon + text + '</div>');
  
	$('<button>',{
		class: 'btn-close',
		style: 'padding-left: 10px;',
		click: function(e){
			e.preventDefault()
			close_callback && close_callback()
			remove_notice()
		}
	}).prependTo(html)

	if($('#main_alert').length) return false;
	else {
		$container.prepend(html)
		html.removeClass('hide').hide().fadeIn('slow')
	}
	function remove_notice() {
		html.stop().fadeOut('slow').remove()
	}

	html.on('click', function () {
		callback && callback()
		remove_notice()
	});
}
