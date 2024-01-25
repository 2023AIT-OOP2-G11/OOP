document.addEventListener('DOMContentLoaded', function () {
	const triggerButton = document.getElementById('yuusya-id');
	const popupMessage = document.getElementById('yuusya-message');

	triggerButton.addEventListener('mouseenter', function () {
		popupMessage.style.display = 'block';
	});

	triggerButton.addEventListener('mouseleave', function () {
		popupMessage.style.display = 'none';
	});
});