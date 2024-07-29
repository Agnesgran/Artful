// script.js

document.addEventListener('DOMContentLoaded', function() {
    // Scroll to Top Functionality
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

    // Dynamic Content Loading for Comments
    document.addEventListener('DOMContentLoaded', function() {
        let page = 1;
        const loadMoreButton = document.getElementById('load-more-button');
        const loadMoreContainer = document.getElementById('load-more-container');
    
        // Function to load more artworks
        function loadMoreArtworks() {
            fetch(`/gallery/load-more/?page=${page + 1}`)
                .then(response => response.json())
                .then(data => {
                    // Append new artworks to the container
                    const container = document.getElementById('art-gallery-container');
                    data.artworks.forEach(artwork => {
                        const div = document.createElement('div');
                        div.innerHTML = `
                            <h3>${artwork.title}</h3>
                            <img src="${artwork.image}" alt="${artwork.title}" />
                            <p>${artwork.description}</p>
                            <p>Price: ${artwork.price}</p>
                            <p>Artist: ${artwork.artist}</p>
                        `;
                        container.appendChild(div);
                    });
    
                    // Increment page number
                    page += 1;
    
                    // Hide button if no more artworks to load
                    if (data.has_more === false) {
                        loadMoreContainer.style.display = 'none';
                    }
                });
        }
    
        // Show Load More button when scrolled to bottom
        window.addEventListener('scroll', () => {
            if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
                loadMoreContainer.style.display = 'block';
            }
        });
    
        // Load more artworks when button is clicked
        loadMoreButton.addEventListener('click', () => {
            loadMoreArtworks();
        });
    
        // Initial load more check
        loadMoreArtworks();
    });
    