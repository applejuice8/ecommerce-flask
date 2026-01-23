const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

// Increase, decrease buttons
document.querySelectorAll('.update-quantity').forEach(btn => {
    btn.addEventListener('click', async () => {
        const productId = btn.dataset.productId;
        const action = btn.dataset.action;

        const cartTotal = document.getElementById('cart-total');
        const productCard = document.getElementById(`product-${productId}`);
        const btnGroup = productCard.querySelector('.btn-group');
        const decreaseBtn = productCard.querySelector('[data-action="decrease"]');
        const quantityBtn = productCard.querySelector('.disabled');
        const addBtn = productCard.querySelector('[data-action="add"]');

        let res, data;

        if (action == 'add') {
            res = await fetch(`/api/cart/add/${productId}`, {
                method: 'POST',
                headers: { 'X-CSRFToken': csrfToken }
            });
            data = await res.json();
        } else {
            res = await fetch(`/api/cart/update/${productId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ action })
            });
            data = await res.json();
        }

        // Update DOM
        const quantity = data.quantity;
        if (quantity > 0) {
            btnGroup.style.display = 'inline-flex';
            addBtn.style.display = 'none'
            quantityBtn.textContent = quantity;
            decreaseBtn.innerHTML = (quantity == 1) ? '<i class="fa-solid fa-trash-can"></i>' : '-';
        } else {
            btnGroup.style.display = 'none';
            addBtn.style.display = 'inline-block';
        }
        cartTotal.innerText = data.cartTotal;
    })
});
