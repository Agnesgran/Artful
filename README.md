# Artful

Artful is a web application designed for art enthusiasts to explore and manage art collections. It features a gallery of artworks, artist profiles, and allows users to interact through comments. The site emphasizes a user-friendly experience with a focus on showcasing art and facilitating interactions between artists and visitors.

![Responsive Mockup](https://github.com/YourUsername/Artful/blob/main/assets/readme_images/landingmockup.png)

## Features

### Home
- **Landing Page**: Showcases a collection of featured artworks with a brief introduction to Artful.
- **Search Functionality**: Users can search for artworks and artists.

### Art Gallery
- **Art Listings**: Displays a grid of artworks with basic information and image thumbnails.

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



## Technologies

- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Backend**: Django (Python)
- **Database**: PostgreSQL
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

| Test Case                         | Description                                                | Result         |
|------------------------------|-----------------------------------------------------------------|----------------|
| **Homepage Load**            | Verify homepage loads correctly and all elements are displayed. | Pass           |
| **Art Detail Availability**  | Ensure availability status displays as "Yes" or "No".           | Pass           |
| **Profile Update Form**      | Test profile update form for valid and invalid inputs.          | Pass           |
| **Comment Submission**       | Verify users can submit comments and see them reflected.        | Pass           |
| **Login Functionality**      | Verify login with valid credentials and error handling.         | Pass           |
| **Responsive Design**        | Check layout on various devices and screen sizes.               | Pass           |
| **Error Handling**           | Test for proper error messages and handling on invalid actions. | Pass           |

### Responsiveness Testing

| Device/Screen Size       | Test Case Description                                 | Result |
|--------------------------|-------------------------------------------------------|--------|
| **Desktop Lenovo Yoga 530**  | Verify layout and content scaling.                | Pass   |
| **Mobile Iphone 15 pro**     | Ensure content is mobile-friendly and touchable.  | Pass   |

### Browser Compatibility Testing

| Browser             | Test Case Description                                     | Result |
|---------------------|-----------------------------------------------------------|--------|
| **Google Chrome**   | Ensure correct display and behavior of features.          | Pass   |
| **Mozilla Firefox** | Ensure correct display and behavior of features.          | Pass   |
| **Safari**          | Ensure correct display and behavior of features.          | Pass   |
| **Microsoft Edge**  | Ensure correct display and behavior of features.          | Pass   |

### Bugs Resolved

| Issue Description                         | Resolution                                                           |
|-------------------------------------------|----------------------------------------------------------------------|
| **Debug Toolbar Import Error**            | Removed `debug_toolbar` from `settings.py` and updated requirements. |
| **Application Crashing on Heroku**        | Corrected middleware settings, cleared Heroku cache, and redeployed. |
| **ModuleNotFoundError for Debug Toolbar** | Removed `debug_toolbar` references from code and configuration.      |

### Bugs Unresolved

- No known bugs left unresolved

### Lighthouse Testing Outcome

| Metric            | Desktop Score | Mobile Score |
|-------------------|---------------|--------------|
| **Performance**   | 72            | 69           |
| **Accessibility** | 98            | 98           |
| **Best Practices**| 100           | 100          |
| **SEO**           | 91            | 91           |

### Code Validation

| Validator        | Results                                                          |
|------------------|------------------------------------------------------------------|
| **HTML**         | No errors, 1 warning found using [W3C HTML Validator]            |
| **CSS**          | No errors found using [Jigsaw CSS Validator]                     |
| **JavaScript**   | No errors, and 9 ES6 warnings found using [JSHint].              |
| **Python**       | No major issues detected using [CI Linter].                      |

### User Story Testing

| User Story                                                                 | Test Case Description                                                            | Result |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------|
| **As a user, I want to register and create an account so that I can log in and access the gallery features.** | Verify that users can successfully register and create an account, and then log in to access the gallery features. | Pass   |
| **As a user, I want to update my profile so that I can keep my information up to date.** | Ensure that users can update their profile information and that changes are saved and displayed correctly. | Pass   |
| **As a visitor, I want to browse through the art gallery so that I can view the available artworks.** | Check if visitors can navigate through the art gallery and see a list of available artworks. | Pass   |
| **As a visitor, I want to view details of a specific artwork so that I can learn more about it.** | Test that visitors can view detailed information about a specific artwork by selecting it from the gallery. | Pass   |
| **As a registered user, I want to leave comments on artworks so that I can share my thoughts and feedback.** | Verify that registered users can submit comments on artworks and that these comments are displayed correctly. | Pass   |
| **As an artist, I want to upload my artworks to the gallery so that they can be displayed and sold.** | Ensure that artists can upload new artworks to the gallery and that the artworks appear correctly in the gallery. | Pass   |
| **As a visitor, I want to search for artworks by title or artist so that I can find specific pieces easily.** | Test the search functionality to confirm that visitors can find artworks by searching for titles or artist names. | Pass   |


### Features Testing

| Feature                | Test Case Description                                                       | Result |
|------------------------|-------------------------------------------------------------------------------|--------|
| **Home - Landing Page** | Verify that the landing page showcases a hero section with a brief introduction. | Pass   |
| **Home - Search Functionality** | Test the search functionality to ensure users can search for artworks and artists effectively. | Pass   |
| **Art Gallery - Art Listings** | Check that the art gallery displays a grid of artworks with basic information and image thumbnails. | Pass   |
| **Art Detail - Art Description** | Confirm that the detailed view of an artwork includes the title, description, price, availability, and artist. | Pass   |
| **Art Detail - Comments Section** | Verify that the comments section displays user comments and allows posting of new comments. | Pass   |
| **Art Detail - Leave a Comment** | Test that authenticated users can submit comments on artworks and that comments are properly displayed. | Pass   |
| **Profile - User Profile** | Ensure the user profile page displays user information correctly and allows updates. | Pass   |
| **Profile - Profile Update** | Confirm that users can update their profile details, including name, location, and preferred medium. | Pass   |
| **Upload Art - Art Submission** | Verify that authenticated users can upload new artworks to the gallery and that the artworks appear correctly. | Pass   |


### Development

#### Forking GitHub Repository

Forking allows you to make a copy of a chosen repository to your own GitHub account. This allows you to test and edit the project without making changes to the original. Forking is done by following these steps.

1. Whilst logged into your GitHub account, navigate to the repository you would like to fork.
2. Click on the **Fork** button at the top right of the page.
3. Choose a name to give the repository. It will be intially named as the same as the original repository.
4. Click the **Create Fork** button.

#### Cloning GitHub Repository

Cloning allows you to download a local version of a chosen repository. Cloning can be done by following these steps.

1. Whilst logged into your GitHub account, navigate to the repository you would like to clone.
2. Click the green **<> Code** button.
3. Click on the **Local** tab.
4. Select **HTTPS** and copy the url.
5. Open your chosen IDE and ensure Git is installed.
5. In your IDE terminal type **git clone (url link that you copied)** and hit enter.

#### Requirements

The requirements for this particular project are as follows:<br>

asgiref==3.8.1
dj-database-url==0.5.0
Django==4.2.14
django-allauth==0.63.6
django-bootstrap4==24.3
django-heroku==0.3.1
gunicorn==20.1.0
pillow==10.4.0
psycopg2==2.9.9
PyJWT==2.8.0
sqlparse==0.5.1
whitenoise==5.3.0

You can update your requirements file using the command in your IDE terminal:<br>
`pip freeze > requirements.txt`<br>
This is handy command to know for when you install any new components which would then be needed to be added to your requirements.

You can install all requirement packages using the following command in your IDE terminal:<br>
`pip3 install -r requirements.txt`<br>
*Disclaimer: Please check Python documentation for the correct terminal command as it may differ depending on the system you are using*

### Deployment

This project was deployed using [Heroku](https://www.heroku.com "Heroku") by following the steps detailed below.

1. Navigate to Heroku website and sign up or log in.
2. Navigate to your dashboard, select **New** and then **Create New App**.
3. Assign a unique name to your project, select your region and click **Create app**.
4. Navigate to **Settings** tab.
5. You need to add specific config vars to be able to deploy the project properly on Heroku. This is done by clicking on **Reveal Config Vars**, and adding them here. The config vars needed are listed below: <br>
DISABLE_COLLECTSTATIC = 1 - This is needed so that it will not time out on deployment. Collect static must be completed in your IDE terminal each time a change is made to static files. Do this by running the command `python3 manage.py collectstatic`.<br>

#### Deploying from a Github Repository

1. Navigate to **Deploy** tab.
2. Select **GitHub - Connect** for deployment method and connect your GitHub account by logging in with your GitHub details in the prompt.
3. Select your GitHub account from the dropdown list if not already preselected.
4. Search for your GitHub repository that you would like to deploy and click **Connect** on the respository in the search list.
5. Deployment options are found further down the **Deploy** tab with options for **Automatic Deploys** and **Manual Deploy**. Automatic deploys all for heroku to update your app everytime your GitHub is updated.
6. Choose your deployment option and the branch from which you would like to deploy.
7. If **Automatic deploys** is chosen, click on **Enable Automatic Deploys**. If **Manual deploy** chosen, click on **Deploy Branch**.
8. Heroku should now start the deployment process. Once successfully deployed, a message will appear saying **Your app was successfully deployed.** with a button to view your deployed application.


## Credits

### Media
- All images in Artworks page were found on [Pexels](https://www.pexels.com/).
- Image to display responsiveness in README taken from (https://techsini.com/multi-mockup/index.php)

### Reference Material
- (https://docs.djangoproject.com/en/5.0/)
- (https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- (https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- (https://www.w3schools.com/)
- (https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- (https://stackoverflow.com/)
- Code Institute learning material for all technologies used in the project.
