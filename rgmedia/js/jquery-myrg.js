	$(document).ready(function() {
		var int = 1;

		$('input[name=type]:radio').change(function() {
			switch ($('input[name=type]:radio:checked').val()) {
				case '1':
					$('#form_table_chapters').show();
					$('#form_table_exec').hide();
					$('#form_table_recipients').hide();
					$('#form_table_newsletter').hide();
					$('#form_table_lists').hide();
					$('#newsletter_warning').hide();
					$('#html_newsletter').hide();
					$('#from_newsletter').hide();
					$('#html_normal').show();
					$('#from_normal').show();
					$('#form_status').show();
					break;
				case '2':
					$('#form_table_chapters').hide();
					$('#form_table_exec').show();
					$('#form_table_recipients').hide();
					$('#form_table_newsletter').hide();
					$('#form_table_lists').hide();
					$('#newsletter_warning').hide();
					$('#html_newsletter').hide();
					$('#from_newsletter').hide();
					$('#html_normal').show();
					$('#from_normal').show();
					$('#form_status').show();
					break;
				case '3':
					$('#form_table_chapters').hide();
					$('#form_table_exec').hide();
					$('#form_table_recipients').show();
					$('#form_table_newsletter').hide();
					$('#form_table_lists').hide();
					$('#newsletter_warning').hide();
					$('#html_newsletter').hide();
					$('#from_newsletter').hide();
					$('#html_normal').show();
					$('#from_normal').show();
					$('#form_status').show();
					break;
				case '4':
					$('#form_table_chapters').hide();
					$('#form_table_exec').hide();
					$('#form_table_recipients').hide();
					$('#form_table_newsletter').show();
					$('#form_table_lists').hide();
					$('#newsletter_warning').show();
					$('#html_newsletter').show();
					$('#from_newsletter').show();
					$('#html_normal').hide();
					$('#from_normal').hide();
					$('#form_status').hide();
					break;
				case '5':
					$('#form_table_chapters').hide();
					$('#form_table_exec').hide();
					$('#form_table_recipients').hide();
					$('#form_table_newsletter').hide();
					$('#form_table_lists').show();
					$('#newsletter_warning').hide();
					$('#html_newsletter').hide();
					$('#from_newsletter').hide();
					$('#html_normal').show();
					$('#from_normal').show();
					$('#form_status').show();
					break;
			}
		});
		$('input[name=type]:radio').change();

		$('input[name=scheduling]:radio').change(function() {
			switch ($('input[name=scheduling]:radio:checked').val()) {
				case '0':
					$('#form_table_scheduling').hide();
					break;
				case '1':
					$('#form_table_scheduling').show();
					break;
			}
		});
		$('input[name=scheduling]:radio').change();
		
		$('#id_action').change(function() {
			switch ($('#id_action').val()) {
				case '1':
					$('#inviteemail').show();
					break;
				case '2':
					$('#inviteemail').hide();
					break;
			}
		});
		$('#id_action').change();

		$('#id_importaction').change(function() {
			switch ($('#id_importaction').val()) {
				case '1':
					$('#welcomeemail').show();
					break;
				case '2':
					$('#welcomeemail').hide();
					break;
				case '3':
					$('#welcomeemail').show();
					break;
			}
		});
		$('#id_importaction').change();
		
		$('input[name=invitee_type]:radio').change(function() {
			switch ($('input[name=invitee_type]:radio:checked').val()) {
				case '5':
					$('#form_table_recipientes').show();
					break;
				default:  $('#form_table_recipientes').hide();
			}
		});
		$('input[name=invitee_type]:radio').change();
	});
