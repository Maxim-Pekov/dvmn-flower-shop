$(document).ready(function(){
    // действия, которые необходимо выполнить после загрузки документа...
    $(document).on('click', '.order__form_pay', function(e) {
        document.querySelector('#message_line').innerText = '';
        const checkout = YooMoneyCheckout('964811');
        const cardNum = document.querySelector('#cardNum').value;
        const cardCVC = document.querySelector('#cardCVC').value;
        const cardMonth = document.querySelector('#cardMonth').value;
        const cardYear = document.querySelector('#cardYear').value;

        let csrf = document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*\=\s*([^;]*).*$)|^.*$/, "$1");
        console.log(cardNum);
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
                console.log(paymentToken)
                $.ajax({
                    type: "post",
                    url: "/payment/",
                    data: {
                        payment_token: paymentToken,
                        csrfmiddlewaretoken: csrf,
                        price: payment_price,
                        title: payment_title,
                    },
                    
                    success: function(response) {
                        console.log(response);
                    }
                });
        
                return paymentToken;
            }
            if (res.status === 'error') {
                document.querySelector('#message_line').innerText = 'Данные карты невалидны';
            }
        });
        console.log(checkout);
    })
});
