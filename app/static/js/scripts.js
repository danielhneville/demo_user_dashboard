$(document).ready(function(){

	$('#remove').click(function(){
		alertify.confirm('Are you sure you want to delete this user?', function(e){
			if (e) {
				var user_id = $('#delete').val();
				var route = '/admin/destroy/' + user_id;
				$.get(route, function(res){
					// $('#all_users').html(function(){

					// })
				})
			} else {
				return false;
			}
		});

	});


})