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
    function loadComments(artId) {
        fetch(`/gallery/art/${artId}/comments/`) // Adjust URL based on your route
            .then(response => response.json())
            .then(data => {
                updateCommentsSection(data.comments);
            })
            .catch(error => {
                console.error('Error loading comments:', error);
            });
    }

    function updateCommentsSection(comments) {
        const commentsContainer = document.getElementById('comments-section');
        commentsContainer.innerHTML = ''; // Clear existing comments

        comments.forEach(comment => {
            const commentElement = document.createElement('div');
            commentElement.className = 'comment';
            commentElement.innerHTML = `
                <p><strong>${comment.user__username}</strong> - ${comment.created_at}</p>
                <p>${comment.text}</p>
            `;
            commentsContainer.appendChild(commentElement);
        });
    }

    // Handle form submission via AJAX
    const commentForm = document.getElementById('comment-form');
    if (commentForm) {
        commentForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(this);
            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => {
                if (response.ok) {
                    loadComments(document.body.dataset.artId); // Reload comments
                    this.reset(); // Clear the form
                } else {
                    console.error('Failed to post comment.');
                }
            })
            .catch(error => {
                console.error('Error posting comment:', error);
            });
        });
    }

    // Initialize comments section if the artId is present
    const artId = document.body.dataset.artId;
    if (artId) {
        loadComments(artId);
    }
});
