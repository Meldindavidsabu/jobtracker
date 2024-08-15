// static/js/custom.js
document.addEventListener("DOMContentLoaded", function() {
    const password1Field = document.getElementById("id_password1");
    const password2Field = document.getElementById("id_password2");
    const passwordMessage = document.getElementById("password-message");

    function validatePassword(password) {
        // Example validation rules
        const minLength = 8;
        const hasNumbers = /\d/.test(password);

        return password.length >= minLength && hasNumbers;
    }

    function updatePasswordMessage() {
        const password = password1Field.value;
        if (password && !validatePassword(password)) {
            passwordMessage.textContent = 'Your password must be at least 8 characters long and contain at least one number.';
            passwordMessage.style.color = 'red';
        } else {
            passwordMessage.textContent = '';
        }
    }

    password1Field.addEventListener('input', updatePasswordMessage);
});
