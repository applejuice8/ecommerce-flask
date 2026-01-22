// Increase, decrease buttons
document.querySelectorAll('.update-quantity').forEach(btn => {
    btn.addEventListener('click', async () => {
        const productId = btn.dataset.productId;
        const action = btn.dataset.action;
        await fetch(`/cart/update/${productId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ action: action })
        });
        
        // Update frontend
        location.reload();
    })
})

// Checkout button
document.getElementById('checkout').addEventListener('click', async () => {
    await fetch('/cart/clear', { method: 'POST' });

    // Update frontend
    location.reload();
})
