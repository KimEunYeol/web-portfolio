$(document).ready(function() {
	$('#title').focus();

	$('.guestbook-view').each(function() {
		var guestbook_post_id = $(this);
		$.ajax({
			type: "GET",
			url: "/guestbook/view/"+ $(this).data('id'),
			success: function(response) {
				guestbook_post_id.html(response);
			},
		});	
	});

	$('.guestbook-comment').each(function() {
		var comment_id = ".guestbook-comment[data-id=" + $(this).data('id') + "]";
		$.ajax({
			type: "GET",
			url: "/guestbook/comment/list/"+$(this).data('id'),
			success: function(response) {
				$(comment_id).html(response);
			},
		});	
	});

	$('.guestbook-like').each(function() {
		var like_id = ".guestbook-like[data-id=" + $(this).data('id') + "]";
		$.ajax({
			type: "GET",
			url: "/guestbook/like/"+$(this).data('id'),
			success: function(response) {
				$(like_id).html(response);
			},
		});	
	});

});

function writeSend() {
	if (!$('#title').val())
	{
		alert("제목을 입력해 주시기 바랍니다.");
		return;
	}

	if (!$('#content').val())
	{
		alert("내용을 입력해 주시기 바랍니다.");
		return;
	}

	$('#write_form').submit();	
}

function modifySend() {
	if (!$('#title').val())
	{
		alert("제목을 입력해 주시기 바랍니다.");
		return;
	}

	if (!$('#content').val())
	{
		alert("내용을 입력해 주시기 바랍니다.");
		return;
	}

	$('#modify_form').submit();	
}

function modifySend(id) {
	var guestbook_div = ".guestbook-view[data-id="+id+"]";
	var guestbook_form = "form[data-type=modify][data-id="+id+"]";

	if (!$(guestbook_form + ' input[name=title]').val())
	{
		alert("제목을 입력해 주시기 바랍니다.");
		return;
	}

	if (!$(guestbook_form + ' textarea[name=content]').val())
	{
		alert("내용을 입력해 주시기 바랍니다.");
		return;
	}

	var data = new FormData($(guestbook_form)[0]);
	data.append("img_file", $(guestbook_form + ' input[type=file]')[0].files[0]);

	$.ajax({
		type: "POST",
		url: "/guestbook/guestbook_modify_result/",
		processData: false,
		contentType: false,
		data: data,
		success: function(response) {
			$(guestbook_div).html(response);
		},
	});

}

function commentWriteSend(id) {
	var comment_div = '.guestbook-comment[data-id='+id+']';
	var comment_form = 'form[data-type=comment][data-id='+id+']';

	if (!$(comment_form + ' textarea').val())
	{
		alert("내용을 입력해 주시기 바랍니다.");
		return;
	}

	$.ajax({
		type: "POST",
		url: "/guestbook/comment_write_result/",
		data: $(comment_form).serialize(),
		success: function(response) {
			$(comment_div).html(response);
			$(comment_form + ' textarea').val('');
		},
	});
}

function commentReplySend(id, guestbook_post_id) {
	var comment_div = '.guestbook-comment[data-id='+guestbook_post_id+']';
	var comment_form = 'form[data-type=comment-reply][data-id='+id+']';

	if (!$(comment_form + ' textarea').val())
	{
		alert("내용을 입력해 주시기 바랍니다.");
		return;
	}

	$.ajax({
		type: "POST",
		url: "/guestbook/comment_write_result/",
		data: $(comment_form).serialize(),
		success: function(response) {
			$(comment_div).html(response);
			$(comment_form + ' textarea').val('');
			$('.comment-reply[data-id='+id+']').css('display','none');
		},
	});
}

function commentModifySend(id, guestbook_post_id) {
	var comment_div = ".guestbook-comment[data-id="+guestbook_post_id+"]";
	var comment_form = "form[data-type=comment-modify][data-id="+id+"]";

	if (!$(comment_form + ' textarea').val())
	{
		alert("내용을 입력해 주시기 바랍니다.");
		return;
	}

	$.ajax({
		type: "POST",
		url: "/guestbook/comment_modify_result/",
		data: $(comment_form).serialize(),
		success: function(response) {
			$(comment_div).html(response);
			$(comment_form + ' textarea').val('');
		},
	});
}

function deleteClick(id) {
	if (confirm("삭제하시겠습니까?"))
	{
		if (!id)
		{
			$('#delete_form').submit();
		} else {
			$("form[data-id="+id+"]").submit();
		}
	}
}

function modifyClick(id) {
		$.ajax({
			type: "GET",
			url: "/guestbook/modify/"+id,
			success: function(response) {
				$(".guestbook-view[data-id="+id+"]").html(response);
			},
		});	
}

function modifyCancel(id) {
		$.ajax({
			type: "GET",
			url: "/guestbook/view/"+id,
			success: function(response) {
				$(".guestbook-view[data-id="+id+"]").html(response);
			},
		});
}

function commentDeleteClick(comment_id, guestbook_post_id) {
	if (confirm("삭제하시겠습니까?"))
	{
		var comment_div = '.guestbook-comment[data-id='+guestbook_post_id+']';
		var comment_form = 'form[data-type=comment_delete][data-id='+comment_id+']';

		$.ajax({
			type: "POST",
			url: "/guestbook/comment_delete_result/",
			data: $(comment_form).serialize(),
			success: function(response) {
				$(comment_div).html(response);
				$(comment_form + ' textarea').val('');
			},
		});
	}
}

function commentModifyClick(id) {
		$.ajax({
			type: "GET",
			url: "/guestbook/comment/modify/"+id,
			success: function(response) {
				$(".comment-block[data-id="+id+"]").html(response);
			},
		});	
}

function commentClick(comment_id) {
	$('.comment-reply').each(function() {
		$(this).css('display','none');
	});

	$('.comment-reply[data-id='+comment_id+']').css('display','block');
}

var inProgress = false;

function likeClick(guestbook_post_id) {
	var like_form = 'form[data-type=like][data-id='+guestbook_post_id+']';

	if(!inProgress) {
		inProgress = true;

		$.ajax({
			type: "POST",
			url: "/guestbook/like_result/",
			data: $(like_form).serialize(),
			success: function(response) {
				if (response.like_err_msg) {
					alert(response.like_err_msg);
				}
				$.ajax({
					type: "GET",
					url: "/guestbook/like/"+response.guestbook_post_id,
					success: function(response) {
						$(".guestbook-like[data-id="+guestbook_post_id+"]").html(response);
					},
				});
				inProgress = false;
			},
		});
	}
}

