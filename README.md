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

## Authentication and User Capabilities

### Authentication

- **Login**: Users can securely log in to their accounts using their credentials.
- **Logout**: Users can log out of their accounts to end their session.
- **Sign Up**: New users can create an account by signing up with their details.

### User Capabilities (Logged In)

- **Upload Art**: Logged-in users can upload artwork to the gallery.
- **Delete Uploaded Art**: Users can remove artwork they have previously uploaded.
- **Comment**: Users can leave comments on artworks.
- **Delete a Posted Comment**: Users can delete comments they have made on artworks.
- **Edit Profile**: Users can update their profile information, including personal details and preferences.

### Flow Diagram

Here is a basic flow of user interactions with authentication and capabilities:

```plaintext
+----------------+       +----------------+       +----------------+       +----------------+
|  Sign Up Page  | ----> |    Login Page  | ----> |  User Dashboard| ----> |   Upload Art   |
+----------------+       +----------------+       +----------------+       +----------------+
                                                          |                             |
                                                          |                             |
                                                          v                             v
                                                 +----------------+       +----------------+
                                                 |  Commenting    |       |   Delete Art   |
                                                 |   Feature      |       +----------------+
                                                 +----------------+       +----------------+
                                                          |                              |
                                                          |                              v
                                                          v               +----------------+
                                                 +----------------+       | Edit Profile   |
                                                 | Delete Comment |       +----------------+
                                                 +----------------+
## Technologies

- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Version Control**: Git
- **Deployment**: GitHub Pages / Heroku 

## UX Design

### Navigation
- **Navigation Bar**: Consistent across all pages with links to Home, Artworks, Profile, log in/ log out and upload art.

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

### Responsiveness Testing

| Device/Screen Size       | Test Case Description                              | Result |
|--------------------------|---------------------------------------------------|--------|
| **Desktop (1920x1080)**  | Verify layout and content scaling.                | Pass   |
| **Tablet (800x1280)**    | Check content readability and touch interactions. | Pass   |
| **Mobile (375x667)**     | Ensure content is mobile-friendly and touchable.  | Pass   |

### Browser Compatibility Testing

| Browser          | Test Case Description                                      | Result |
|------------------|-----------------------------------------------------------|--------|
| **Google Chrome**| Check for layout and functionality consistency.           | Pass   |
| **Mozilla Firefox** | Verify proper rendering and interactive elements.       | Pass   |
| **Safari**       | Ensure correct display and behavior of features.         | Pass   |
| **Microsoft Edge** | Test for consistency and responsiveness.                | Pass   |

### Bugs Resolved

| Issue Description                       | Resolution                                      |
|----------------------------------------|-------------------------------------------------|
| **Debug Toolbar Import Error**         | Removed `debug_toolbar` from `settings.py` and updated requirements. |
| **Application Crashing on Heroku**     | Corrected middleware settings, cleared Heroku cache, and redeployed. |
| **ModuleNotFoundError for Debug Toolbar** | Removed `debug_toolbar` references from code and configuration. |

### Bugs Unresolved

| Issue Description                       | Current Status                       |
|----------------------------------------|--------------------------------------|
| **[Describe the unresolved issue]**    | [Current status of the issue]        |

### Lighthouse Testing Outcome

| Metric          | Desktop Score | Mobile Score | Key Insights                              |
|-----------------|---------------|--------------|-------------------------------------------|
| **Performance** | 90+           | 85+          | Image optimization needed.                |
| **Accessibility** | 90+           | 90+          | Ensure all interactive elements are accessible via keyboard. |
| **Best Practices** | 90+           | 90+          | Consider using HTTPS for all resources.  |
| **SEO**         | 90+           | 90+          | Improve meta descriptions and alt attributes. |

### Code Validation

| Validator        | Results                                      |
|------------------|----------------------------------------------|
| **HTML**         | No errors found using [W3C HTML Validator](https://validator.w3.org/). |
| **CSS**          | No errors found using [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/). |
| **JavaScript**   | No errors found using [JSHint or ESLint].   |
| **Python**       | No major issues detected using [Pylint or flake8]. |

### User Story Testing

| User Story                           | Test Case Description                        | Result |
|-------------------------------------|----------------------------------------------|--------|
| **[Brief description of User Story]** | [Description of test case]                  | Pass   |

### Features Testing

| Feature                | Test Case Description                            | Result |
|------------------------|-------------------------------------------------|--------|
| **[Brief description of Feature]** | [Description of test case]                  | Pass   |

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
