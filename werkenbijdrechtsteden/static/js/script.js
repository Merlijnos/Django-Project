// Show spinner when a filter is applied or a page link is clicked
document.querySelector('.form-filter').addEventListener('submit', function() {
    document.getElementById('spinner').style.display = 'block';
});

document.querySelector('.pagination-buttons').addEventListener('click', function() {
    document.getElementById('spinner').style.display = 'block';
});

// Hide spinner when the results are loaded
window.addEventListener('load', function() {
    document.getElementById('spinner').style.display = 'none';
});``