//scroll to top function
document.addEventListener('DOMContentLoaded', function() {
    const scrollToTopButton = document.createElement('button');
    scrollToTopButton.textContent = 'Top';
    scrollToTopButton.className = 'scroll-to-top';
    document.body.appendChild(scrollToTopButton);

    // Show or hide the button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.scrollY > 200) {
            scrollToTopButton.style.display = 'block';
        } else {
            scrollToTopButton.style.display = 'none';
        }
    });

    // Smooth scroll to top on button click
    scrollToTopButton.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});




// Dynamic content load
document.addEventListener('DOMContentLoaded', function() {
    const loadMoreButton = document.getElementById('load-more');
    let nextPage = 2;

    if (loadMoreButton) {
        loadMoreButton.addEventListener('click', function() {
            fetch(`/artworks/?page=${nextPage}`)
                .then(response => response.json())
                .then(data => {
                    const artworksContainer = document.getElementById('artworks-container');
                    data.artworks.forEach(artwork => {
                        const artworkElement = document.createElement('div');
                        artworkElement.className = 'col-md-4 mb-4';
                        artworkElement.innerHTML = `
                            <div class="card">
                                <img src="${artwork.image}" class="card-img-top" alt="${artwork.title}">
                                <div class="card-body">
                                    <h5 class="card-title">${artwork.title}</h5>
                                    <p class="card-text">${artwork.description}</p>
                                    <p class="card-text"><strong>Price:</strong> $${artwork.price}</p>
                                    <p class="card-text"><strong>Artist:</strong> ${artwork.artist}</p>
                                    <a href="/artworks/${artwork.id}" class="btn btn-primary">View Details</a>
                                </div>
                            </div>
                        `;
                        artworksContainer.appendChild(artworkElement);
                    });
                    nextPage++;
                });
        });
    }
});
