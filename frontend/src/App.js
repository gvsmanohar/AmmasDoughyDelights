import React from 'react';
import './styles.css';

function App() {
    const handleContactFormSubmit = (event) => {
        event.preventDefault();
        const name = event.target.name.value;
        const email = event.target.email.value;
        const message = event.target.message.value;

        const data = { name, email, message };
        console.log('Sending data:', data);

        fetch('http://localhost:8080/api/contact', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                alert('Message sent successfully!');
                event.target.reset();
            })
            .catch(error => {
                alert('Error sending message');
                console.error('Error:', error);
            });
    };

    return (
        <div className="App">
            <header>
                <h1>Amma's Doughy Delights</h1>
                <nav>
                    <ul>
                        <li><a href="#home">Home</a></li>
                        <li><a href="#menu">Menu</a></li>
                        <li><a href="#contact">Contact</a></li>
                    </ul>
                </nav>
            </header>
            <section id="home">
                <h2>Welcome to Amma's Doughy Delights</h2>
                <p>Your go-to place for delicious homemade doughy treats!</p>
            </section>
            <section id="menu">
                <h2>Our Menu</h2>
                <div id="products">
                    {/* Display products here */}
                </div>
            </section>
            <section id="contact">
                <h2>Contact Us</h2>
                <form id="contactForm" onSubmit={handleContactFormSubmit}>
                    <input type="text" name="name" placeholder="Your Name" required />
                    <input type="email" name="email" placeholder="Your Email" required />
                    <textarea name="message" placeholder="Your Message" required></textarea>
                    <button type="submit">Send</button>
                </form>
            </section>
        </div>
    );
}

export default App;
