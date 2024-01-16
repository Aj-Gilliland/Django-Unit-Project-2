function toggleIcon(button) {
    button.classList.toggle('active');
}

$(document).ready(function () {
    $('#id_picture').change(function () {
        console.log('File input changed');
        // Trigger the click event of the hidden submit button
        $('#hiddenSubmitButton').click();
    });
});

          