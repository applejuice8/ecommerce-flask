// Checkout button
document.getElementById('checkout').addEventListener('click', async () => {
    await fetch('/cart/clear', { method: 'POST' });

    // Update frontend
    location.reload();
})