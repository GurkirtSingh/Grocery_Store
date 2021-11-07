var logout = document.getElementById('logout')

logout.addEventListener('click', function(){
    console.log('logging out..')
    fetch('/accounts/logout')
    .then(function(response){
        location.href = response.url;
    });
})

$(document).ready(function(){
    var csrftoken = Cookies.get('csrftoken');
    $('.item').click(function(){
        var productId = $(this).data('productid')
        location.href = '/product/'+productId;
    })

    $('.update-cart').click(function(event){
        event.stopPropagation();
        event.target.classList.toggle('is-active');
        let id = $(this).data('id');
        let isAdd = this.classList.contains('is-active');
        if(isAdd){
            updateCart(id, 1, 'PUT');
        }else{
            updateCart(id, 1, 'REMOVE');
        }
    })

    $('#cart-button-up').click(function(){
        var currentVal = parseInt($('#cart-input').val());
        $('#cart-input').val(currentVal+1);
    })
    $('#cart-button-down').click(function(){
        var currentVal = parseInt($('#cart-input').val());
        var newVal = currentVal <= 1 ? currentVal: currentVal-1;
        $('#cart-input').val(newVal);
    })
    $('#addToCart').click(function(){
        var currentVal = $('#cart-input').val();
        var productId = $(this).data('id');
        updateCart(productId, currentVal, 'PUT')
    })

    function updateCart(id, quantity, action){
        $.post({
            url: 'http://127.0.0.1:8000/cart',
            data: {'csrfmiddlewaretoken':csrftoken,'id': id, 'quant':quantity, 'action':action},
            success: function(response){
                console.log(response)
            }
        })
    }
});
