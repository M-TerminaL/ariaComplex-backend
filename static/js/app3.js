const mobile = document.getElementById('phoneNum1')
const phoneAlert = document.querySelector('.phone-alert-form')


function phoneValidationCheck () {
    let phoneValue = mobile.value;
    if (phoneValue.length !== 11 || phoneValue[0] !== '0' || phoneValue[1] !== '9') {
        phoneAlert.style.display = 'inline-block'
        mobile.style.border = '1px solid red'
    }
    else {
        phoneAlert.style.display = 'none'
        mobile.style.border = '1px solid #01ff01'
    }
}


mobile.addEventListener('blur', phoneValidationCheck)