# Artful

Artful is a web application designed for art enthusiasts to explore and manage art collections. It features a gallery of artworks, artist profiles, and allows users to interact through comments. The site emphasizes a user-friendly experience with a focus on showcasing art and facilitating interactions between artists and visitors.

![Responsive Mockup](https://github.com/YourUsername/Artful/blob/main/assets/readme_images/landingmockup.png)

## Features

### Home
- **Landing Page**: Showcases a collection of featured artworks with a brief introduction to Artful.
- **Search Functionality**: Users can search for artworks and artists.

### Art Gallery
- **Art Listings**: Displays a grid of artworks with basic information and image thumbnails.
- **Pagination**: For navigating through multiple pages of artworks.

### Art Detail
- **Art Description**: Detailed view of individual artwork including title, description, price, availability, and artist.
- **Comments Section**: Users can read and post comments on artworks.
- **Leave a Comment**: Authenticated users can submit comments.

### Profile
- **User Profile**: Displays user information and allows updates.
- **Profile Update**: Users can update their profile details including name, location, and preferred medium.

### Upload Art
- **Art Submission**: Authenticated users can upload new artworks to the gallery.

### Authentication
- **Login**: Secure login functionality for users.
- **Logout**: Users can log out of their accounts.



![Home Page](https://github.com/YourUsername/Artful/blob/main/assets/readme_images/homepage.png)
![Art Gallery](https://github.com/YourUsername/Artful/blob/main/assets/readme_images/artgallery.png)
![Art Detail](https://github.com/YourUsername/Artful/blob/main/assets/readme_images/artdetail.png)
![Profile](https://github.com/YourUsername/Artful/blob/main/assets/readme_images/profile.png)
![Upload Art](https://github.com/YourUsername/Artful/blob/main/assets/readme_images/uploadart.png)

## Technologies

- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Version Control**: Git
- **Deployment**: GitHub Pages / Heroku 

## UX Design

### Navigation
- **Navigation Bar**: Consistent across all pages with links to Home, Art Gallery, Profile, and Contact pages.

### Responsiveness
- **Mobile-Friendly**: Designed to be responsive across devices including smartphones, tablets, and desktops.
- **Accessible**: Adheres to accessibility standards for users with disabilities.

### Aesthetics
- **Modern Design**: Clean and minimalistic design focusing on artwork presentation.
- **User-Centric**: Easy-to-use interface with intuitive navigation.

## Testing

### Manual Testing

| Test Case                         | Description                                      | Result         |
|-----------------------------------|--------------------------------------------------|----------------|
| **Homepage Load**                 | Verify homepage loads correctly and all elements are displayed. | Pass           |
| **Art Gallery Pagination**        | Check if pagination works and correctly displays artworks. | Pass           |
| **Art Detail Availability**       | Ensure availability status displays as "Yes" or "No". | Pass           |
| **Profile Update Form**           | Test profile update form for valid and invalid inputs. | Pass           |
| **Comment Submission**            | Verify users can submit comments and see them reflected. | Pass           |
| **Login Functionality**           | Ensure login works with correct credentials and error handling for invalid ones. | Pass           |
| **Responsive Design**             | Check layout on various devices and screen sizes. | Pass           |
| **Error Handling**                | Test for proper error messages and handling on invalid actions. | Pass           |

### Validator Testing

- **HTML**: No errors were found using the [W3C HTML Validator](https://validator.w3.org/).
- **CSS**: No errors were found using the [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/).

### Performance Testing

- **Lighthouse Scores**: 
  - **Desktop**: 
    - Performance: 90+
    - Accessibility: 90+
    - Best Practices: 90+
    - SEO: 90+
  - **Mobile**: 
    - Performance: 85+
    - Accessibility: 90+
    - Best Practices: 90+
    - SEO: 90+

## Deployment

1. **Deploying to Heroku**:
   - Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
   - Navigate to your project directory and run `heroku create`.
   - Commit your changes and push to Heroku with `git push heroku main`.
   - Visit the live application at the URL provided by Heroku.

2. **Deploying to GitHub Pages**:
   - Push your code to the `main` branch of your GitHub repository.
   - In the repository settings, go to the "Pages" section and select the `main` branch as the source.
   - Access your live site via the GitHub Pages URL.

## References

- **Django Documentation**: [Django Official Documentation](https://docs.djangoproject.com/)
- **Bootstrap**: [Bootstrap Documentation](https://getbootstrap.com/docs/)
- **W3C Validator**: [W3C Markup Validation Service](https://validator.w3.org/)
- **CSS Validator**: [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

## Credits

### Content
- Icons and images used from [Font Awesome](https://fontawesome.com/) and [Pexels](https://www.pexels.com/).
- Color palette from [Coolors](https://coolors.co/).

### Media
- Background images sourced from [Pexels](https://www.pexels.com/).

### Reference Material
- Inspiration and best practices drawn from various open-source projects and Django documentation.

