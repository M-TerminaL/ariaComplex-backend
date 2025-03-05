let num1 = document.getElementById('n1')
let num2 = document.getElementById('n2')
let num3 = document.getElementById('n3')
let num4 = document.getElementById('n4')
let num5 = document.getElementById('n5')


window.onload = () => num1.focus()


function moveNum2(event) {
    let nOne = event.target.value
    if (nOne == '1' || nOne == '2' || nOne == '3' || nOne == '4' || nOne == '5' || nOne == '6' || nOne == '7' || nOne == '8' || nOne == '9' || nOne == '0') {
        num2.focus()
    }
}
function moveNum3(event) {
    let nTwo = event.target.value
    if (nTwo == '1' || nTwo == '2' || nTwo == '3' || nTwo == '4' || nTwo == '5' || nTwo == '6' || nTwo == '7' || nTwo == '8' || nTwo == '9' || nTwo == '0') {
        num3.focus()
    }
}
function moveNum4(event) {
    let nThree = event.target.value
    if (nThree == '1' || nThree == '2' || nThree == '3' || nThree == '4' || nThree == '5' || nThree == '6' || nThree == '7' || nThree == '8' || nThree == '9' || nThree == '0') {
        num4.focus()
    }
}
function moveNum5(event) {
    let nFour = event.target.value
    if (nFour == '1' || nFour == '2' || nFour == '3' || nFour == '4' || nFour == '5' || nFour == '6' || nFour == '7' || nFour == '8' || nFour == '9' || nFour == '0') {
        num5.focus()
    }
}


num1.addEventListener('keyup', moveNum2)
num2.addEventListener('keyup', moveNum3)
num3.addEventListener('keyup', moveNum4)
num4.addEventListener('keyup', moveNum5)


