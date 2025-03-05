/* Start Form Validation */


const fname = document.getElementById('name')
const lname = document.getElementById('lname')
const mobile = document.getElementById('phoneNum1')


const nameAlert = document.querySelector('.name-alert-form')
const lnameAlert = document.querySelector('.lname-alert-form')
const phoneAlert = document.querySelector('.phone-alert-form')

function fnameValidationCheck () {

    let fnameValue = fname.value;
    if (fnameValue.trim() === '' || fnameValue.length == 0 || !just_persian(fnameValue)) {
        nameAlert.style.display = 'inline-block'
        fname.style.border = '1px solid red'
    }
    else {
        nameAlert.style.display = 'none'
         fname.style.border = '1px solid #01ff01'
    }
}


function lnameValidationCheck () {
    let lnameValue = lname.value;
    if (lnameValue.trim() === '' || lnameValue.length == 0 || !just_persian(lnameValue)) {
        lnameAlert.style.display = 'inline-block'
        lname.style.border = '1px solid red'
    }
    else {
        lnameAlert.style.display = 'none'
        lname.style.border = '1px solid #01ff01'
    }
}



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





fname.addEventListener('blur', fnameValidationCheck)
lname.addEventListener('blur', lnameValidationCheck)
mobile.addEventListener('blur', phoneValidationCheck)




function just_persian(str) {
    var p = /^[\u0600-\u06FF\s]+$/;
    if (!p.test(str)) {
        return false
    }
    return true;
 }


/* End Form Validation */