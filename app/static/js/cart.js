// Increase, decrease buttons
document.querySelectorAll('.update-quantity').forEach(btn => {
    btn.addEventListener('click', async () => {
        const productId = btn.dataset.productId;
        const action = btn.dataset.action;
        
        const cartTotal = document.getElementById('cart-total');
        const productCard = document.getElementById(`product-${productId}`);
        const decreaseBtn = productCard.querySelector('[data-action="decrease"]');
        const quantityBtn = productCard.querySelector('.disabled');

        const res = await fetch(`/api/cart/update/${productId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ action })
        });
        const data = await res.json();
        const quantity = data.quantity;
        if (quantity < 1) {
            productCard.remove();
        }

        decreaseBtn.innerHTML = (quantity == 1) ? '<i class="fa-solid fa-trash-can"></i>' : '-';
        quantityBtn.innerText = quantity;
        cartTotal.innerText = data.cartTotal;
    })
})

// Checkout button
document.getElementById('checkout').addEventListener('click', async () => {
    await fetch('/cart/clear', { method: 'POST' });

    // Update frontend
    location.reload();
})