function replaceImage() {
    var logo = document.getElementById('logo');
    var newImage = document.createElement('img');
    
    if (window.innerWidth <= 768) {  
        newImage.src = 'Elements/oauth.png';
        newImage.alt = 'GPMailbox small';
    } else {  
        newImage.src = 'Elements/logo.png';
        newImage.alt = 'GPMailbox big';
    }
    
    logo.parentNode.replaceChild(newImage, logo);
}

// Appeler la fonction au chargement de la page et lorsqu'on redimensionne la fenêtre
window.onload = replaceImage;
window.addEventListener('resize', replaceImage);

function toggleImageList(imageListId, buttonId) {
    const imageList = document.getElementById(imageListId);
    const showAllButton = document.getElementById(buttonId);

    imageList.classList.toggle('active');
    showAllButton.classList.toggle('fade-out');
    showAllButton.classList.toggle('fade-in');

    if (imageList.classList.contains('active')) {
        showAllButton.innerHTML = '<i class="fas fa-chevron-up"></i> Moins';
    } else {
        showAllButton.innerHTML = '<i class="fas fa-chevron-down"></i> Plus';
    }

    const imageGrid = document.querySelector('.image-grid');
    imageGrid.classList.toggle('hide-overflow');
}

document.addEventListener('DOMContentLoaded', function() {
    const accountIcon = document.getElementById('accountIcon');
    const dropdownContentAccount = document.querySelector('.dropdown-content-account');
    const sidebar = document.querySelector('.sidebar');

    accountIcon.addEventListener('mouseenter', () => {
        dropdownContentAccount.style.display = 'block';
    });

    sidebar.addEventListener('mouseleave', (event) => {
        const isHoveringSidebar = event.relatedTarget && event.relatedTarget.closest('.sidebar');
        if (!isHoveringSidebar) {
            dropdownContentAccount.style.display = 'none';
        }
    });
});

function toggleSearch() {
    const searchButton = document.getElementById('searchButton');
    const searchInput = document.getElementById('searchInput');

    searchButton.classList.toggle('active');
    searchInput.classList.toggle('active');

    if (searchButton.classList.contains('active')) {
        searchInput.focus();
    }
}

