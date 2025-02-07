document.addEventListener("DOMContentLoaded", function() {
    const docBtn = document.getElementById('documentation-btn');
    const modal = document.getElementById('documentation-modal');
    const closeBtn = document.querySelector('.close-btn');

    docBtn.addEventListener('click', function() {
        modal.style.display = 'flex';
    });

    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };
});
