// Initialize cart as an empty array
let cart = [];

// Function to add an item to the cart
function addToCart(item) {
    // Check if the item already exists in the cart
    const existingItem = cart.find(cartItem => cartItem.name === item.name);
    if (existingItem) {
        // Increase quantity if the item exists
        existingItem.quantity += 1;
    } else {
        // Add a new item with quantity 1
        cart.push({ ...item, quantity: 1 });
    }
    updateCartDisplay();
}

// Function to update the cart display
function updateCartDisplay() {
    const cartContainer = document.getElementById('cart-items');
    cartContainer.innerHTML = ''; // Clear previous cart items

    // Display each item in the cart
    cart.forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.innerHTML = `
            ${item.name} - ₹${item.price} x ${item.quantity}
            <button onclick="removeFromCart('${item.name}')">Remove</button>
        `;
        cartContainer.appendChild(cartItem);
    });

    // Update total price
    const totalPrice = cart.reduce((total, item) => total + item.price * item.quantity, 0);
    document.getElementById('total-price').innerText = `Total: ₹${totalPrice}`;
}

// Function to remove an item from the cart
function removeFromCart(itemName) {
    // Remove the item by filtering it out of the cart
    cart = cart.filter(item => item.name !== itemName);
    updateCartDisplay();
}

// Function to handle checkout
function checkout() {
    if (cart.length === 0) {
        alert('Your cart is empty!');
        return;
    }

    const checkoutForm = document.getElementById('checkout-form');
    checkoutForm.style.display = 'block'; // Show the checkout form
}

// Function to submit the checkout form
function submitCheckout(event) {
    event.preventDefault(); // Prevent page reload on form submission

    // Get user details from the form
    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;

    if (name && address) {
        alert(`Thank you for your order, ${name}! Your food will be delivered to ${address}.`);
        cart = []; // Clear the cart
        updateCartDisplay();
        document.getElementById('checkout-form').style.display = 'none'; // Hide the checkout form
    } else {
        alert('Please fill out all fields.');
    }
}

// Example menu items (replace with your backend data if necessary)
const menuItems = [
    { name: 'Pizza', price: 8.99 },
    { name: 'Burger', price: 9.99 },
    { name: 'icecream', price: 10.99 }
];

// Populate the menu dynamically
function populateMenu() {
    const menuContainer = document.getElementById('menu-container');

    menuItems.forEach(item => {
        const menuItem = document.createElement('div');
        menuItem.className = 'menu-item';
        menuItem.innerHTML = `
            <img src="https://via.placeholder.com/200" alt="${item.name}" class="menu-image" />
            <div class="menu-details">
                <h3>${item.name}</h3>
                <p>Price: ₹${item.price}</p>
                <button onclick="addToCart(${JSON.stringify(item)})">Add to Cart</button>
            </div>
        `;
        menuContainer.appendChild(menuItem);
    });
}

// Populate the menu when the page loads
window.onload = populateMenu;
