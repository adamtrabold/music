document.addEventListener('DOMContentLoaded', () => {
    // Add timestamp to CSS link to prevent caching
    const cssLink = document.querySelector('link[href="styles.css"]');
    if (cssLink) {
        cssLink.href = `styles.css?t=${Date.now()}`;
    }

    // Parallax effect
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
            const x = -offsetX * 5 * speed;
            const y = -offsetY * 5 * speed;

            layer.style.transform = `translate(${x}px, ${y}px)`;
        });
    };

    container.addEventListener('mousemove', handleParallax);
});