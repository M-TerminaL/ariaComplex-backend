function addPackageToOrder(button, packageId) {
    const row = button.closest('tr');
    const packageCountElement = row.querySelector('.package-count');
    const value = packageCountElement.value;
    fetch('/order/add-to-order?package_id=' + packageId + '&count=' + value).then(res => res.json()).then(data => {

        Swal.fire({
            title: "اعلان",
            text: data.text,
            icon: data.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: data.confirm_button_text
        })
    });
}


function removeOrderDetail(detailId) {
    fetch('/user/remove-order-detail?detail_id=' + detailId).then(res => res.json()).then(data => {
        if (data.status === 'success') {
            const elemContent = document.getElementById('order-detail-content')
            console.log(elemContent)
            elemContent.innerHTML = data.body
        }
    })
}


function changeOrderDetailCount(detailId, state) {
    fetch('/user/change-order-detail?detail_id=' + detailId + '&state=' + state).then(res => res.json()).then(data => {
        if (data.status === 'success') {
            const elemContent = document.getElementById('order-detail-content')
            console.log(elemContent)
            elemContent.innerHTML = data.body
        }
    })
}

// function calculateTotalPriceWithDiscountCode() {
//     const discountInputElement = document.getElementById('discount-code')
//     const discountValue = discountInputElement.value
//     const invoiceBox = document.getElementById('invoice-box')
//
//     fetch('/user/calculate-discount-code?discount_value=' + discountValue).then(res => res.json()).then(data => {
//         const elemContent = document.getElementById('order-detail-content')
//         elemContent.innerHTML = data.body
//     })
//     invoiceBox.style.display = 'block'
// }


function calculateTotalPriceWithDiscountCode() {
    const discountInputElement = document.getElementById('discount-code')
    const discountValue = discountInputElement.value

    fetch('/user/calculate-discount-code?discount_value=' + discountValue)
        .then(res => res.json())
        .then(data => {
            const elemContent = document.getElementById('order-detail-content')
            elemContent.innerHTML = data.body
        })
}
