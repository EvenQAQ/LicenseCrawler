// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

$(document).ready(function () {
	//Datepicker
	var datepicker_default_option = { changeYear: true, changeMonth: true, yearRange: "1900:2100", showAnim: "blind" };
	$('.datepicker').datepicker(datepicker_default_option);
	$('.datepicker_past').datepicker($.extend({}, datepicker_default_option, { maxDate: 0 }));
	$('.datepicker_future').datepicker($.extend({}, datepicker_default_option, { minDate: 0 }));

	$(".timepicker").timepicker({
		timeFormat: 'g:i A',
		step: 15,
		minTime: '5:00 AM',
		maxTime: '9:00 PM',
		disableTextInput: true
	});
	$('.timepicker_range').datepair({
		timeClass: 'timepicker'
	});


	// mask and placeholder
	$('.phone_us').mask('(000) 000-0000');
	$('.date').mask("00/00/0000");
	$(".zipcode").mask("00000-9999");
	$('.md_dln').mask('S-000-000-000-000');
});