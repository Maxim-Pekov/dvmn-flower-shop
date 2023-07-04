$(document).ready(function(){
    $(document).on('click', '.order__form_pay', function(e) {
        let btnPay = e.target;
        btnPay.style.opacity = 0.2;
        btnPay.disable = true;
        document.querySelector('#message_line').innerText = '';
        const checkout = YooMoneyCheckout('964811');
        const cardNum = document.querySelector('#cardNum').value;
        const cardCVC = document.querySelector('#cardCVC').value;
        const cardMonth = document.querySelector('#cardMonth').value;
        const cardYear = document.querySelector('#cardYear').value;

        let csrf = document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*\=\s*([^;]*).*$)|^.*$/, "$1");
        checkout.tokenize({
            number: cardNum,
            cvc: cardCVC,
            month: cardMonth,
            year: cardYear
        }).then(res => {
            if (res.status === 'success') {
                const { paymentToken } = res.data.response;
                const payment_price = document.querySelector('#payment_price').innerText;
                const payment_title = document.querySelector('#payment_title').innerText;
                const orderNumber = document.querySelector('#order_number').value;
                $.ajax({
                    type: "post",
                    url: "/payment/",
                    data: {
                        payment_token: paymentToken,
                        csrfmiddlewaretoken: csrf,
                        price: payment_price,
                        title: payment_title,
                        order_number: orderNumber, 
                    },
                    
                    success: function(response) {
                        btnPay.disable = false;
                        btnPay.style.opacity = 1;
                        window.location.href = response;
                    },

                    error: function(response) {
                        btnPay.disable = false;
                        btnPay.style.opacity = 1;
                        document.querySelector('#message_line').innerText = 'Ошибка платежа';
                    },
                });
        
            }
            if (res.status === 'error') {
                btnPay.disable = false;
                btnPay.style.opacity = 1;
                document.querySelector('#message_line').innerText = 'Данные карты невалидны';
            }
        });
    })
});
