document.addEventListener('DOMContentLoaded', function() {
    // Create floating circles for background
    const bgAnimation = document.getElementById('bgAnimation');
    for (let i = 0; i < 20; i++) {
        const circle = document.createElement('div');
        circle.classList.add('circle');
        
        // Random size between 50px and 200px
        const size = Math.random() * 150 + 50;
        circle.style.width = `${size}px`;
        circle.style.height = `${size}px`;
        
        // Random position
        circle.style.left = `${Math.random() * 100}%`;
        circle.style.top = `${Math.random() * 100}%`;
        
        // Random animation duration between 10s and 20s
        circle.style.animationDuration = `${Math.random() * 10 + 10}s`;
        
        // Random delay
        circle.style.animationDelay = `${Math.random() * 5}s`;
        
        bgAnimation.appendChild(circle);
    }
    
    // Create floating particles
    const particles = document.getElementById('particles');
    for (let i = 0; i < 50; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        
        // Random size between 2px and 6px
        const size = Math.random() * 4 + 2;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        
        // Random position
        particle.style.left = `${Math.random() * 100}%`;
        
        // Random animation duration between 5s and 15s
        const duration = Math.random() * 10 + 5;
        particle.style.animationDuration = `${duration}s`;
        
        // Random delay
        particle.style.animationDelay = `${Math.random() * 5}s`;
        
        particles.appendChild(particle);
    }
    
    // Redirect to home page after 4 seconds
     setTimeout(() => {
        window.location.href = "/"; 
    }, 4000);
});