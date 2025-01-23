// Cache busting mechanism
function updateCSSVersion() {
    const timestamp = new Date().getTime();
    const cssLinks = document.querySelectorAll('link[rel="stylesheet"]');
    cssLinks.forEach(link => {
        const href = link.href.split('?')[0];
        link.href = `${href}?v=${timestamp}`;
    });
}

// Add development tools
function addDevTools() {
    const devTools = document.createElement('div');
    devTools.style.position = 'fixed';
    devTools.style.bottom = '24px';
    devTools.style.right = '24px';
    devTools.style.zIndex = '9999';

    const reloadButton = document.createElement('button');
    reloadButton.textContent = 'Reload CSS';
    reloadButton.style.padding = '8px 16px';
    reloadButton.style.cursor = 'pointer';
    reloadButton.addEventListener('click', updateCSSVersion);

    devTools.appendChild(reloadButton);
    document.body.appendChild(devTools);
}

document.addEventListener('DOMContentLoaded', () => {
    // Update CSS version on page load
    updateCSSVersion();
    addDevTools();

    // Existing parallax code
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

// Add periodic CSS refresh
setInterval(updateCSSVersion, 5000); // Check for CSS updates every 5 seconds