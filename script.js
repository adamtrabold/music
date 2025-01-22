document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.parallax-container');
    const layers = document.querySelectorAll('.parallax-layer');

    const handleParallax = (e) => {
        const mouseX = e.clientX;
        const mouseY = e.clientY;
        
        const centerX = window.innerWidth / 2;
        const centerY = window.innerHeight / 2;
        
        const offsetX = (mouseX - centerX) / centerX;
        const offsetY = (mouseY - centerY) / centerY;

        layers.forEach(layer => {
            const speed = parseFloat(layer.getAttribute('data-speed'));
            const x = -offsetX * 100 * speed;
            const y = -offsetY * 100 * speed;
            
            layer.style.transform = `translate(${x}px, ${y}px)`;
        });
    };

    container.addEventListener('mousemove', handleParallax);
});
