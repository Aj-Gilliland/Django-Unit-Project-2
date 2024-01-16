function toggleIcon(button) {
    button.classList.toggle('active');
}

$(document).ready(function () {
    $('#id_picture').change(function () {
        console.log('File input changed');
        $('#hiddenSubmitButton').click();
    });
});

          