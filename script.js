document.addEventListener('DOMContentLoaded', () => {
    // Mobile viewport height adjustment
    const setVH = () => {
        let vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty('--vh', `${vh}px`);
    };

    setVH();
    window.addEventListener('resize', setVH);

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