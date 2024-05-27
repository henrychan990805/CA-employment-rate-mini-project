document.addEventListener('DOMContentLoaded', function() {
    let zoomLevel = 1;

    const content = document.body;
    const zoomInBtn = document.getElementById('zoomIn');
    const zoomOutBtn = document.getElementById('zoomOut');
    const resetZoomBtn = document.getElementById('resetZoom');

    if (zoomInBtn && zoomOutBtn && resetZoomBtn) {
        zoomInBtn.addEventListener('click', function() {
            zoomLevel += 0.1;
            content.style.transform = 'scale(' + zoomLevel + ')';
            content.style.transformOrigin = '0 0';
        });

        zoomOutBtn.addEventListener('click', function() {
            zoomLevel -= 0.1;
            content.style.transform = 'scale(' + zoomLevel + ')';
            content.style.transformOrigin = '0 0';
        });

        resetZoomBtn.addEventListener('click', function() {
            zoomLevel = 1;
            content.style.transform = 'scale(' + zoomLevel + ')';
            content.style.transformOrigin = '0 0';
        });
    } else {
        console.error('Zoom buttons not found in the DOM');
    }
});
