/* JavaScript for dropdown functionality */

function toggleDropdown() {
    const dropdownMenu = document.getElementById('dropdownMenu');
    if (dropdownMenu.style.display === 'none') {
        dropdownMenu.style.display = 'block'; // Show dropdown
    } else {
        dropdownMenu.style.display = 'none'; // Hide dropdown
    }
}

window.onclick = function(event) {
    if (!event.target.matches('#dropdownButton')) {
        const dropdowns = document.getElementsByClassName("dropdown-menu");
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.style.display === 'block') {
                openDropdown.style.display = 'none';
            }
        }
    }
}