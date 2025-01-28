// Initialize order number counter with a prefix and starting number
let orderNumber = 1001; // Starting order number
const orderPrefix = "ORD"; // Order number prefix

document.getElementById('sendOtpBtn').addEventListener('click', function() {
    const phone = document.getElementById('phone').value;

    if (phone) {
        console.log(`Sending OTP to ${phone}`);
        
        document.getElementById('otpGroup').style.display = 'block';
        document.getElementById('verifyOtpBtn').style.display = 'inline-block';
        document.getElementById('message').innerText = 'OTP sent! Please check your messages.';
        
        window.otp = '123456'; // Example OTP
    } else {
        alert('Please enter a valid phone number.');
    }
});

document.getElementById('signInForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    const otpInput = document.getElementById('otp').value;

    if (otpInput === window.otp) {
        document.getElementById('message').innerText = 'OTP verified! You are signed in.';
        document.querySelector('.menu').style.display = 'block';
    } else {
        document.getElementById('message').innerText = 'Invalid OTP. Please try again.';
    }
});

// Function to show sub-menu items
function showSubMenu(menuId) {
    const subMenu = document.getElementById(menuId);
    
    // Toggle visibility of sub-menu
    if (subMenu.style.display === 'none' || subMenu.style.display === '') {
        subMenu.style.display = 'block';
    } else {
        subMenu.style.display = 'none';
    }
}

// Function to handle adding items to the cart
let cartItems = [];

function addToCart(itemName) {
    cartItems.push(itemName);
    
    updateCartSummary();
}

// Function to update the cart summary display
function updateCartSummary() {
    const cartItemsList = document.getElementById('cartItems');
    
    cartItemsList.innerHTML = ''; // Clear existing items

    cartItems.forEach((item, index) => {
        const listItem = document.createElement('li');
        
        listItem.textContent = item;

        // Create a remove button
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        
        removeButton.onclick = function() {
            removeFromCart(index);
        };

        listItem.appendChild(removeButton);
        
        cartItemsList.appendChild(listItem);
    });

    // Show checkout button if there are items in the cart
    document.getElementById('checkoutBtn').style.display = cartItems.length > 0 ? 'block' : 'none';
}

// Function to remove an item from the cart
function removeFromCart(index) {
   cartItems.splice(index, 1); // Remove item from array
   updateCartSummary(); // Update the displayed list
}

// Function to proceed to checkout
function proceedToCheckout() {
    // Hide the cart summary and show the checkout section
    document.getElementById('cartSummary').style.display = 'none';
    document.getElementById('checkoutSection').style.display = 'block';

    // Update total amount (for demonstration purposes)
    const totalAmount = cartItems.length * 10; // Example: each item costs $10
    document.getElementById('totalAmount').textContent = totalAmount.toFixed(2);
}

// Function to confirm order
function confirmOrder(event) {
    event.preventDefault(); // Prevent form submission

    // Increment order number and generate current order number
    orderNumber++;
    const currentOrderNumber = `${orderPrefix}-${orderNumber}`;
    document.getElementById('order-number').innerText = `Order Number: ${currentOrderNumber}`;

    // Hide checkout section and show order successful section
    document.getElementById('checkoutSection').style.display = 'none';
    
    // Show order successful message
    document.getElementById('orderSuccessfulSection').style.display = 'block';

    // Display order summary
    const orderSummaryList = document.getElementById('orderSummaryItems');
    
    orderSummaryList.innerHTML = ''; // Clear existing items

    cartItems.forEach(item => {
        const listItem = document.createElement('li');
        listItem.textContent = item;
        orderSummaryList.appendChild(listItem);
    });
}

// Initially hide the menu until user signs in
document.querySelector('.menu').style.display = 'none';