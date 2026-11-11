document.addEventListener('DOMContentLoaded', () => {
    // Mobile viewport height adjustment
    // const setVH = () => {
    //     let vh = window.innerHeight * 0.01;
    //     document.documentElement.style.setProperty('--vh', `${vh}px`);
    // };

    // setVH();
    // window.addEventListener('resize', setVH);

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
// WebMCP: lets browser agents use this page on the visitor's behalf.
// https://webmachinelearning.github.io/webmcp/
(() => {
    const modelContext = document.modelContext || navigator.modelContext;
    if (!modelContext || typeof modelContext.registerTool !== 'function') return;

    const musicLinks = () => Array.from(document.querySelectorAll('.music-services a'))
        .map(a => ({ service: a.querySelector('img')?.alt || a.className, url: a.href }));

    modelContext.registerTool({
        name: 'get_music_links',
        description: "Lists where to listen to Adam Trabold's music (Bandcamp, Apple Music, TIDAL, Spotify, Amazon Music).",
        inputSchema: { type: 'object', properties: {} },
        annotations: { readOnlyHint: true },
        execute: async () => ({
            content: [{ type: 'text', text: JSON.stringify(musicLinks()) }]
        })
    });

    modelContext.registerTool({
        name: 'fill_email_signup',
        description: "Fills the visitor's email address into Adam Trabold's email list form. It does not subscribe them: the visitor must press JOIN themselves. Only use this when the visitor asks to join.",
        inputSchema: {
            type: 'object',
            properties: {
                email: { type: 'string', format: 'email', description: "The visitor's own email address" }
            },
            required: ['email']
        },
        execute: async ({ email }) => {
            const input = document.getElementById('mce-EMAIL');
            if (!input) throw new Error('Signup form not found');
            input.value = String(email || '').trim();
            if (!input.checkValidity()) throw new Error('That does not look like a valid email address');
            input.focus();
            input.scrollIntoView({ behavior: 'smooth', block: 'center' });
            return {
                content: [{ type: 'text', text: 'Email filled in. Ask the visitor to press JOIN to subscribe.' }]
            };
        }
    });
})();
