# Recipe Blog Project
### Introduction 
**Recipe Blog** is an interactive online platform that brings together food enthusiasts from around the world to share, discover, and celebrate culinary creations. The app allows users to create, edit, and manage their own recipes while exploring those shared by others. It also includes a rating and review system, enabling users to share feedback and discover top-rated recipes. With personalised profiles and an intuitive design, Recipe Blog offers a user-friendly experience for anyone looking to document their culinary adventures, try new dishes, and connect with a like-minded community. """Live Link"""

"""Website Preview Display"""

## Table of Contents
- [User Experience Design](#user-experience-design)
  - [The Strategy](#the-strategy)
    - [Site Goals](#site-goals)
    - [Agile Planning](#agile-planning)
    - [Epics](#epics)
    - [User Stories](#user-stories)
  - [Scope](#the-scope)
  - [Structure](#structure)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
    - [Potential Future Features to Implement](#potential-future-features-to-implement)


  - [Skeleton](#the-skeleton)
    - [Wireframes](#wireframes)
    - [Database Design](#database-design)
    - [Security](#security)
  - [Surface](#surface)
    - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
- [Technologies](#technologies)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Version Control](#version-control)
  - [Heroku Deployment](#heroku-deployment)
  - [Run Locally](#run-locally)
  - [Fork Project](#fork-project)
- [Credits](#credits)

---

## User Experience Design

### The Strategy

#### Site Goals
The **Recipe Blog** aims to provide a vibrant and engaging platform for users to share their culinary creations, explore new recipes, and connect with other food enthusiasts. The primary goals of the site include:

- **User-Friendly Experience**: To create an intuitive, accessible platform where users of all skill levels can easily navigate, share, and discover recipes. A streamlined design ensures that users can quickly find the features they need, whether they’re adding a new recipe, leaving a review, or browsing the latest dishes.

- **Recipe Sharing and Management**: To empower users to create, edit, and manage their own recipes. Each recipe entry is designed to be intuitive, allowing users to share their unique methods. Personal profile pages allow users to view and organize their recipes in one place, making it easy to revisit or modify their content.

- **Discovery and Exploration**: To inspire culinary discovery by enabling users to explore a wide variety of recipes shared by others. The platform offers filtering, allowing users to find recipes that match their preferences. A rating system allows users to provide feedback.

- **Community Interaction**: To foster a sense of community by allowing users to rate each other’s recipes. The platform encourages positive interactions, creating a collaborative space where users can learn, improve, and connect over shared culinary interests.

Through these goals, **Recipe Blog** aims to cultivate a welcoming environment where food enthusiasts can document their culinary journeys, discover new flavors, and engage in a meaningful community dedicated to the art of cooking.

#### Agile Planning
# Agile Approach

My Agile approach for this project followed a structured, iterative process that ensured flexibility, ongoing feedback, and regular progress evaluations. Below is an outline of the Agile methodology applied, including the planning, development, and deployment phases:

## 1. Project Planning and Requirement Gathering
- **Initial Requirements**: The project began by identifying key requirements, dividing them intoepics that align with core functionalities.
- **User Stories**: Each epic was broken down into user stories.
- **Prioritization**: User stories were prioritized based on their impact on the overall user experience and project timeline.

## 2. Sprint Planning
- **Defining Sprints**: The project was divided into manageable sprints, each focusing on completing a set of related user stories within an epic.
- **Sprint Goals**: Each sprint had a clear goal to deliver a specific feature or enhancement.
- **Task Estimation**: Tasks within each sprint were estimated for time and complexity, balancing workload to ensure steady progress without overloading.

## 3. Development and Iterative Testing
- **Incremental Development**: Features were developed incrementally, with individual tasks tackled in small, manageable units.
- **Regular Testing**: After each sprint, features were thoroughly tested to ensure they met the acceptance criteria. Testing included unit testing, integration testing, and user acceptance testing for specific functionality.
- **Feedback Loop**: Regular feedback from testing allowed the team to identify and address bugs, usability issues, and performance improvements early on.

## 6. Final Testing and Deployment
- **Comprehensive Testing**: The project underwent comprehensive testing, covering functionality, responsiveness, and cross-browser compatibility.
- **Production Preparation**: Deployment tasks included setting up static file handling, configuring environment variables, and preparing database settings.
- **Deployment**: The final version was deployed to a live server (heroku).

### Sprints 

The development process for **Recipe Blog** was organized into four sprints, each planned and tracked using Jira. Each sprint focused on specific epics, allowing for a structured, iterative approach to completing the project’s key features and documentation.

#### Sprint Overview
![Sprints Overview](/docs/agile/agile_images/sprints.webp)

#### Sprint 1: Epics 1 and 2 (October 24th - 27th)
The first sprint focused on laying the foundation of the project, covering **Epic 1** and **Epic 2**.

- **Sprint 1 Backlog**  
  ![Sprint 1 Backlog](/docs/agile/agile_images/sprint_one.webp)

- **Sprint 1 Kanban Board**  
  ![Sprint 1 Board](/docs/agile/agile_images/sprint_one_board.webp)

- **Sprint 1 Completed Tasks**  
  ![Sprint 1 Done](/docs/agile/agile_images/sprint_one_done.webp)

#### Sprint 2: Epics 3 and 4 (October 28th - 30th)
The second sprint focused on **Epic 3** and **Epic 4**, covering key user functionality such as user registration, login, and CRUD operations for the menu items by staff.

- **Sprint 2 Progress**  
  ![Sprint 2](/docs/agile/agile_images/sprint_two.webp)

#### Sprint 3: Epics 5 and 6 (November 1st - 2nd)
In the third sprint, **Epic 5** (Booking) and **Epic 6** (Deployment) were the focus. This included implementing booking functionality, allowing users to create and manage reservations, and preparing the project for deployment to Heroku.

- **Sprint 3**  
  ![Sprint 3](/docs/agile/agile_images/sprint_three.webp)

#### Sprint 4: Epic 7 and README (November 3rd - 5th)
The final sprint was dedicated to **Epic 7** (Documentation) and final touches on the README. This ensured all documentation, including project details, user stories, and testing processes, was complete and aligned with the finished product.

- **Sprint 4**  
  ![Sprint 4](/docs/agile/agile_images/sprint_four.webp)

## Finished Timeline 
![Finished Timeline](/docs/agile/agile_images/agile_board.webp)

#### Epics
## Epic 1 - Base Setup
Set up the foundational project structure, including environment configuration, static files, and reusable templates for consistent design and functionality across the site.

## Epic 2 - User Account and Authentication
Implement user account creation, login, logout, and email verification features to ensure secure user authentication and access to personalized features.

## Epic 3 - Recipes and Profile Management
Enable users to create and view recipes and access a personalized profile page displaying their information and recipe submissions.

## Epic 4 - Recipe Management Features and Enhancements
Add editing, deleting, and reviewing features for recipes, along with meal type categorization, to enhance user interaction with recipes.

## Epic 5 - Home Page and Styling
Design and style the home page, navbar, and other static elements for visual consistency, usability, and responsiveness across all devices.

## Epic 6 - Refinements and Additional Features
Make final adjustments and add small features, such as recipe filtering, custom error pages, and data presentation enhancements.

## Epic 7 - Deployment
Prepare the project for deployment by configuring static file handling, setting up the production environment, and deploying to a live server.

#### User Stories

## Epic 1 - Base Setup
## User Story 1: Set up the Project Environment
As a developer, I need to set up the project environment to ensure that the core features can be built on a stable foundation.

**Tasks:**
1. Install and configure Django for the project.
2. Set up a virtual environment and install required dependencies (Django, Whitenoise, etc.).
3. Create initial project and app structure.
4. Configure settings for database, static files, and templates.
5. Set up version control using Git and create a GitHub repository for the project.

**Acceptance Criteria:**
- The Django project and app structure is correctly initialized.
- The virtual environment is activated, and all required dependencies are installed.
- Database configuration is correct and connected to the app.
- Git is initialized and version control is set up with proper commits and a remote repository.
- The project can run locally without errors, serving static files and loading templates.

## User Story 2: Create the `base.html` Page and Structure
As a developer, I need to create the `base.html` page and structure to ensure all pages share a consistent layout.

**Tasks:**
1. Set up the `base.html` template with placeholders for dynamic content.
2. Add blocks for common sections like header, footer, and main content.
3. Include the main CSS and JavaScript files in `base.html` for consistent styling and functionality across pages.
4. Create a reusable template for the site’s title, meta tags, and favicon.

**Acceptance Criteria:**
- The `base.html` file contains reusable blocks for all other pages.
- Common elements like the navbar, footer, and static assets (CSS, JS) are loaded on all pages.
- Templates extend from `base.html` and properly display dynamic content.
- Website structure is responsive and works well across different devices.

## User Story 3: Create Static Resources for Images, CSS, and JavaScript
As a developer, I need to create static resources for images, CSS, and JavaScript so the site functions and looks visually appealing.

**Tasks:**
1. Set up a static folder structure for images, CSS, and JavaScript files.
2. Write CSS styles for consistent typography, color schemes, and layout.
3. Include JavaScript for any interactive elements (e.g., carousel, search bar functionality).
4. Add sample images for testing design and functionality.
5. Link the CSS and JavaScript files to `base.html` and other templates.

**Acceptance Criteria:**
- A static directory structure is in place (`static/images`, `static/css`, `static/js`).
- CSS styling is applied to ensure the site is visually consistent with the design plan.
- JavaScript functionality is implemented for interactive components.
- All pages load the necessary static resources correctly without errors.

## User Story 4: Create the Footer with Social Media Links and Contact Information
As a developer, I need to create the footer with social media links and contact information.

**Tasks:**
1. Design the footer layout with placeholders for contact information and social media icons.
2. Add links to social media accounts (e.g., Facebook, Instagram, Twitter).
3. Include an email address and/or phone number in the footer for user inquiries.
4. Ensure the footer is responsive and looks good on all screen sizes.
5. Integrate the footer into `base.html` so that it appears on all pages.

**Acceptance Criteria:**
- The footer contains social media icons with functioning links to external sites.
- The footer includes correct contact information (email, phone number).
- The footer is displayed consistently across all pages and is responsive on different devices.
- Footer elements are styled in line with the overall site design.

## User Story 5: Create the Navbar with a Search Bar
As a developer, I need to create the navbar with a search bar so users can search for specific recipes or ingredients easily.

**Tasks:**
1. Design the navbar layout with links to key sections (Home, Recipes, etc.).
2. Add a functional search bar with a placeholder for searching recipes/ingredients.
3. Implement responsiveness so the navbar collapses into a menu on smaller screens.
4. Include a user account dropdown or link for login/logout functionality.
5. Ensure the search bar is linked to a placeholder view or future search functionality.

**Acceptance Criteria:**
- The navbar contains links to all important sections and works across all pages.
- The search bar is displayed prominently in the navbar and is responsive on mobile devices.
- Navbar collapses into a menu or hamburger icon on smaller screens.
- User account links (sign-in/register or profile) are visible and functional.
- The search bar is implemented and will trigger search functionality (even if stubbed for now).

## Epic 2 - User Account and Authentication
## User Story 1: Account Creation
As a user, I want to create an account so I can interact with the website.

**Tasks:**
1. Set up user registration form using Django Allauth.
2. Add validation checks for username, email, and password.
3. Create a user registration page with the necessary fields (username, email, password).
4. Redirect users to a success page or profile page after successful registration.
5. Add error handling for invalid input (e.g., missing fields).

**Acceptance Criteria:**
- The registration form includes fields for username, email, and password.
- User can register an account successfully after filling in valid details.
- Registration fails with appropriate error messages if the details are invalid.
- After registration, the user is automatically logged in or redirected to a login page.

## User Story 2: Login and Logout
As a user, I want to be able to log in and out of my account to access personal features securely.

**Tasks:**
1. Create a login form using Django Allauth.
2. Implement secure login functionality using user credentials (email/username and password).
3. Create a logout feature that securely logs the user out of their account.
4. Ensure that login errors (e.g., incorrect password) are handled and appropriate messages are shown.

**Acceptance Criteria:**
- Users can successfully log in with their username or email and password.
- Invalid login attempts (e.g., wrong password) show appropriate error messages.
- After logging in, users are redirected to a dashboard or home page.
- Users can securely log out, and session data is cleared upon logout.

## User Story 3: Email Verification
As a site owner, I want users to verify their email when registering to ensure that valid accounts are being used.

**Tasks:**
1. Configure email verification in Django Allauth settings.
2. Set up an email template for verification emails.
3. Ensure that users are prompted to verify their email after registering.
4. Create a view to handle email verification and confirmation processes.
5. Redirect users to the appropriate page after email verification (e.g., login page).

**Acceptance Criteria:**
- After registration, users receive a verification email with a link.
- Clicking the verification link successfully activates the user’s account.
- If users try to log in without verifying their email, they receive a prompt to verify their email first.
- The verification email contains a functional link and clear instructions.

## User Story 4: Implement Authentication Using Allauth
As a developer, I want to implement user authentication using Allauth to manage user sign-up, login, and logout.

**Tasks:**
1. Install and configure Django Allauth in the project settings.
2. Set up URLs and views for registration, login, logout, and password reset.
3. Customise Allauth settings (e.g., email verification, login methods).
4. Test the registration, login, logout, and password reset functionalities to ensure smooth integration.
5. Add middleware for session management and user authentication.

**Acceptance Criteria:**
- Allauth is properly installed and configured in the Django project.
- Registration, login, logout, and password reset functionalities are fully functional.
- The site handles user sessions securely, and user authentication is properly managed.
- The integration allows users to interact with protected features after authentication.

## User Story 5: Customizing Allauth Pages
As a site owner, I want to customise the login and registration pages to match the site's design.

**Tasks:**
1. Override the default Allauth templates for login, registration, and password reset.
2. Apply custom CSS styling to match the site's overall design.
3. Update the templates with custom branding, fonts, and colours.
4. Ensure that the customised pages are responsive and work well across different devices.
5. Test the customised forms to ensure functionality is retained after styling changes.

**Acceptance Criteria:**
- The login, registration, and password reset pages are styled consistently with the rest of the site.
- Custom branding (logo, colours, fonts) is applied to all authentication-related pages.
- The pages remain fully functional and responsive after customization.
- No styling or functional issues are present in the customised pages.

# Epic 3 - Recipes and Profile Management
## User Stories

### User Story 1: Design and Implement the Recipe Model
**Tasks:**
1. Identify fields required for the recipe model (e.g., title, ingredients, steps, meal type).
2. Define data types and constraints for each field.
3. Implement the recipe model in the database.
4. Test model functionality by creating sample recipe entries.

**Acceptance Criteria:**
- The recipe model includes essential fields such as title, ingredients, steps, meal type, and images.
- Each field is correctly validated (e.g., text fields have character limits, required fields are enforced).
- The model is saved in the database and displays data correctly.
- Test entries can be created, saved, and retrieved without errors.

### User Story 2: Create an "Add Recipe" Page for Users to Submit New Recipes
**Tasks:**
1. Design a form layout with fields that align with the recipe model.
2. Create the "Add Recipe" view and corresponding template.
3. Add input validation for form fields.
4. Link the "Add Recipe" page to the navbar for easy access.
5. Test the form by submitting sample recipes.

**Acceptance Criteria:**
- The "Add Recipe" page includes fields for all required information (e.g., title, ingredients, steps, and meal type if time allows).
- Validation messages appear for missing or incorrect inputs.
- Successful submission saves the recipe to the database.
- The page is accessible from the navbar and navigates without errors.

### User Story 3: Develop Pages to View Individual Recipes and List All Recipes
**Tasks:**
1. Design the layout for an individual recipe page.
2. Implement a recipe detail view to display individual recipe information.
3. Create a page to list all recipes with search/filter options if time allows.
4. Link recipes on the list page to their individual detail pages.
5. Test the display and navigation between pages.

**Acceptance Criteria:**
- The individual recipe page displays all recipe details (title, ingredients, instructions, etc.) clearly.
- The list page shows multiple recipes with clear organization.
- Each recipe on the list page links to its detail page.
- The user can navigate between the list and detail pages seamlessly.

### User Story 4: Set Up a Profile Page Displaying User-Specific Information
**Tasks:**
1. Design the profile page layout to show user information (e.g., username, email).
2. Add a list of user-created recipes with options to edit or delete if recipe is opened to display details page.
3. Implement logic to fetch and display only the logged-in user’s recipes.
4. Test page access restrictions to ensure only the logged-in user can view their profile.

**Acceptance Criteria:**
- The profile page shows the user’s information and a list of their recipes.
- Each recipe in the list has options for the user to edit or delete it.
- The profile page is restricted to the logged-in user and shows only their recipes.
- Users can access their profile page from the navbar.

### User Story 5: Update the Navbar to Include Links to Recipe-Related Features and Profile Access
**Tasks:**
1. Add links in the navbar for “Add Recipe,” “View Recipes,” and “Profile.”
2. Ensure links are conditionally visible based on user authentication status.
3. Style navbar links for consistency and usability.
4. Test links to ensure they navigate to the correct pages.

**Acceptance Criteria:**
- The navbar includes links to “Add Recipe,” “View Recipes,” and “Profile.”
- Links are only visible to logged-in users where appropriate.
- The navbar displays consistently across all pages and devices.
- Each link navigates to the intended page without errors.

# Epic 4 - Recipe Management Features and Enhancements
## User Stories

### User Story 1: Build an "Edit Recipe" Page for Modifying Existing Recipes
**Tasks:**
1. Create an "Edit Recipe" view and corresponding template.
2. Pre-fill the edit form with the existing recipe data.
3. Add form validation to ensure changes meet the recipe model requirements.
4. Implement functionality to save updated information to the database.
5. Test the edit functionality to ensure data is updated correctly.

**Acceptance Criteria:**
- The "Edit Recipe" page displays the existing data for all recipe fields (title, ingredients, steps, etc.).
- Users can make changes to any field and submit the form.
- The recipe updates in the database with the new information.
- Users receive a confirmation message upon successful update.
- Error messages display for any invalid inputs.

### User Story 2: Implement a "Delete Recipe" Feature for Removing Recipes
**Tasks:**
1. Add a delete option/button to each recipe in the user’s profile or on the individual recipe page.
2. Create a confirmation prompt or page to prevent accidental deletion.
3. Implement the delete view and function to remove the recipe from the database.
4. Test the delete functionality to ensure recipes are fully removed.

**Acceptance Criteria:**
- Each recipe has a delete option that requires additional confirmation from the user to confirm the action, only if the user is the owner of the recipe.
- Confirming the delete action removes the recipe from the database.
- The user is redirected to a relevant page (e.g., profile or recipe list) with a success message after deletion.
- Deleted recipes no longer appear in the list or database.

### User Story 3: Add a Review Feature Allowing Users to Leave Feedback on Recipes
**Tasks:**
1. Design the review model with a field for rating, out of 5 stars.
2. Create a form for users to leave reviews on each recipe's detail page.
3. Implement the view and logic to save reviews to the database.
4. Display average of submitted reviews on the individual recipe page.
5. Test review submission, display, and database functionality.

**Acceptance Criteria:**
- Users can submit a review with a rating and comment on any recipe detail page, except for their own recipes.
- Each review is saved and associated with the correct recipe and user.
- Average of all submitted reviews is displayed on the recipe detail page.
- Users receive a confirmation message upon successful review submission.

### User Story 4: Extend the Recipe Model with a New Data Type, "Meal Type" (e.g., Breakfast, Lunch, Dinner)
**Tasks:**
1. Add a "meal type" field to the recipe model, with options like "breakfast," "lunch," and "dinner."
2. Update any forms (e.g., add/edit recipe) to include the meal type selection.
3. Update database migrations to apply the new field.
4. Test the addition of meal types to ensure data is stored and displayed correctly.

**Acceptance Criteria:**
- The "meal type" field is added to the recipe model with options for "breakfast," "lunch," "dinner," and any other relevant categories.
- Users can select a meal type when adding or editing a recipe.
- The selected meal type is saved in the database and displays on the recipe detail page.

# Epic 5 - Home Page and Styling

## User Stories

### User Story 1: Add Home Page Content to Introduce and Show the Site’s Purpose
**Tasks:**
1. Write introductory content/about us explaining the site’s purpose and features.
2. Design and organize the content layout, including headings, images, and text.
3. Add call-to-actions to encourage recipe creation or exploring recipes.
4. Link to relevant pages from the home page (e.g., view all recipes, create a recipe).

**Acceptance Criteria:**
- The home page includes clear introductory text that describes the site’s purpose.
- Call-to-action buttons are visible and guide users to register or explore recipes.
- Links on the home page navigate correctly to relevant sections.
- The home page content is engaging and visually structured for easy reading.

### User Story 2: Style the Home Page for Visual Appeal and Usability
**Tasks:**
1. Choose a color scheme and typography that aligns with the site’s theme.
2. Design and style layout elements for visual consistency.
3. Test the page’s visual flow to ensure users can navigate content intuitively.

**Acceptance Criteria:**
- The home page has a cohesive color scheme and visual style.
- All elements are styled to be visually appealing and aligned with the theme.
- Images and visual elements are used appropriately to enhance the page.
- Users can easily read content and navigate the home page without confusion.

### User Story 3: Refine the Navbar for Better Navigation and Styling
**Tasks:**
1. Add or adjust navbar links to include updates or site changes.
2. Style the navbar for a clean and user-friendly look.
3. Test navbar behavior to ensure links are clearly visible and responsive.
4. Implement conditional rendering of links based on user authentication status.

**Acceptance Criteria:**
- The navbar includes links to essential site pages and sections.
- Styling of the navbar is consistent across all pages and matches the site’s theme.
- Links display correctly and are accessible on various devices and screen sizes.
- Links are conditionally displayed based on the user’s login status.

### User Story 4: Ensure Responsive Design Across Screen Sizes
**Tasks:**
1. Test layout and design on various screen sizes (mobile, tablet, desktop).
2. Adjust CSS for flexible grids, font sizes, and image scaling (Use Bootstrap classes).
3. Use media queries to ensure elements reflow properly on different devices.
4. Optimize navigation and key page elements for mobile usability.

**Acceptance Criteria:**
- The website displays correctly on screens of all sizes, from mobile to desktop.
- Key elements such as the navbar, content sections, and buttons are accessible and functional on all devices.
- Text, images, and layout adapt seamlessly to various screen sizes.
- Users can navigate the site comfortably on any device without layout issues.

### User Story 5: Style Authentication Pages (Sign In, Sign Out, Sign Up)
**Tasks:**
1. Style the sign-in, sign-out, and sign-up pages to match the overall site theme.
2. Ensure form fields and buttons are clearly visible and user-friendly.
3. Add validation messages for form input errors.
4. Test accessibility for form fields, labels, and buttons.

**Acceptance Criteria:**
- Authentication pages have a consistent look and feel aligned with the site’s theme.
- Form fields and buttons are styled for usability, with clear visual feedback.
- Validation messages display appropriately for invalid or missing inputs.
- Pages are accessible and user-friendly on all devices.

### User Story 6: Style the Profile Page
**Tasks:**
1. Apply consistent styling to the profile page layout and components.
2. Highlight user-specific elements (e.g., username, recipes created by the user).
3. Ensure buttons and links are clear and intuitive.
4. Test the profile page for visual consistency with other site pages.

**Acceptance Criteria:**
- The profile page matches the overall styling and theme of the site.
- User-specific elements are visually distinct and easy to locate.
- All buttons and links on the profile page are functional and intuitive.
- The profile page displays correctly on all screen sizes.

### User Story 7: Optimize CSS Code to Remove Unused Styles
**Tasks:**
1. Review existing CSS code for redundant, unused, or repeating styles.
2. Consolidate similar styles to improve efficiency and reduce file size.
3. Use CSS variables and classes to simplify styling and future updates.
4. Test all pages after CSS adjustments to ensure styling remains consistent.

**Acceptance Criteria:**
- CSS code is streamlined with no redundant or unnecessary styles.
- All pages maintain a consistent look, with no styling issues after optimization.
- CSS is organized for easy maintenance and future updates.
- The site performs smoothly with optimized CSS code.

# Epic 6 - Refinements and Additional Features
## User Stories

### User Story 1: Update "Meal Type" Options in the Recipe Model to Include a New Category: "Dessert"
**Tasks:**
1. Modify the recipe model to add "Dessert" as an option in the meal type field.
2. Update any forms (e.g., add/edit recipe) to display the new "Dessert" category.
3. Ensure that the new category is available in the database and any dropdown lists.
4. Test by creating a sample recipe with "Dessert" as the meal type to verify functionality.

**Acceptance Criteria:**
- "Dessert" is available as an option in the meal type selection for all recipe-related forms.
- The new meal type is saved in the database and displays correctly on relevant pages.
- Users can select "Dessert" when adding or editing recipes.
- Test recipes with "Dessert" as the meal type display accurately without issues.

### User Story 2: Develop a Filter Feature to Sort Recipes by Meal Type
**Tasks:**
1. Create a filter option on the recipe list page for meal types (e.g., breakfast, lunch, dinner, dessert).
2. Implement logic to filter recipes based on the selected meal type.
3. Display filtered results dynamically without needing a full page reload if possible.
4. Test the filter feature to ensure it shows the correct recipes for each meal type.

**Acceptance Criteria:**
- Users can filter recipes on the list page by selecting a meal type (e.g., breakfast, lunch, dinner, dessert).
- Only recipes matching the selected meal type display on the page.
- Users can reset the filter to view all recipes again.
- Filter functionality works smoothly and accurately, showing the correct results.

### User Story 3: Apply Title-Casing (Using `capfirst`) to Relevant User-Created Content, Such as Usernames, Recipe Titles, and Descriptions
**Tasks:**
1. Review relevant fields (e.g., usernames, recipe titles, descriptions) for title-casing needs.
2. Implement `capfirst` or similar logic to apply title casing.
3. Update views and templates to reflect title-cased formatting.
4. Test on multiple user-generated entries to ensure title casing works as expected.

**Acceptance Criteria:**
- Usernames, recipe titles, and descriptions display in title case across the site.
- All user-created content reflects title casing in views and templates.
- New content entered by users automatically applies title casing.
- Title casing displays consistently across pages and devices.

### User Story 4: Add Custom Error Pages for Common Errors (404, 403, 500)
**Tasks:**
1. Design custom templates for 404, 403, and 500 error pages.
2. Add informative messages and styling to each error page.
3. Configure the application to use custom error pages instead of defaults.
4. Test each error page by triggering the corresponding error condition.
5. Provide “go back” options on the page.

**Acceptance Criteria:**
- Custom 404, 403, and 500 error pages display with appropriate messages and styling.
- Each error page is visually consistent with the site's design.
- Error pages provide useful information to guide users (e.g., links back to home).
- Error pages display correctly when each error condition is triggered.

# Epic 7 - Deployment

## User Stories

### User Story 1: Integrate Whitenoise to Serve Static Files in Production
**Tasks:**
1. Install Whitenoise as a dependency in the project.
2. Configure the Django settings to use Whitenoise for serving static files.
3. Update `STATIC_ROOT` and `STATICFILES_STORAGE` settings for production.
4. Collect static files and verify they are served correctly.
5. Test static file delivery in a local production-like environment.

**Acceptance Criteria:**
- Whitenoise is successfully installed and configured in Django settings.
- Static files (CSS, JS, images) are served correctly in a production environment.
- No errors occur related to static files in the production environment.

### User Story 2: Prepare Files and Configurations for Deployment to Heroku
**Tasks:**
1. Set up `Procfile` for Heroku deployment.
2. Configure environment variables and secret keys for secure deployment.
3. Test the application locally using production settings.
4. Deploy the application to Heroku.
5. Add Heroku app URL to `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`.

**Acceptance Criteria:**
- The project includes all necessary files for Heroku deployment (e.g., `Procfile`).
- Environment variables are securely managed and correctly set in Heroku.
- The app deploys successfully on Heroku with all features working as expected.
- No errors or security issues are present in the deployed environment.

## Finished Timeline 
![Finished Timeline](/docs/agile/agile_images/agile_board.webp)

### Scope 

The **Recipe Blog** project is designed with a set of core features focused on providing users with an accessible and engaging platform for recipe sharing, discovery, and community engagement. The scope of the project centers around key functionalities that make it easy for users to manage their culinary content, interact with others, and explore a variety of recipes.

#### Core Features

1. **User Accounts and Authentication**  
   - **Description**: Registered users can log in, and manage their own content.
   - **Reason**: By providing secure user accounts, the platform ensures that users have a personalized experience, allowing them to manage their own content while preventing unauthorized access.

2. **Recipe Creation, Editing, and Deletion**  
   - **Description**: Registered users can create, edit, and delete their recipes, adding details like ingredients, instructions, and images..
   - **Reason**: This feature gives users a dedicated space to share their culinary creations within a space of like-minded people, or store their own recipes for future use, both fostering a sense of community and providing users with a virtual 'cook book'.

3. **Recipe Viewing and Exploration**  
   - **Description**: All users, whether logged in or not, can browse, search, and filter recipes by different meal types.
   - **Reason**: This allows users to easily discover new recipes.

4. **Rating and Review System**  
   - **Description**: Logged-in users can rate recipes created by others, with the average rating displayed on each recipe.
   - **Reason**: The rating system helps highlight popular recipes and provides valuable feedback to recipe creators.

5. **User Profiles**  
   - **Description**: Each user has a profile page displaying all the recipes they’ve created, allowing them to manage their own content.
   - **Reason**: This feature enhances personalization, allowing users to manage their contributions in one place, and makes it easy for them to showcase their culinary portfolio.

These features were chosen to balance functionality with usability, ensuring that users can easily share and explore recipes while enjoying the benefits of a supportive, interactive community.

### Structure

#### Features
- **Navbar**  
  - **Description**: A navigation bar is available at the top of every page, giving users quick access to main sections such as Home, Add Recipe, View All Recipes, and Login/Register, Log Out, Profile. The navigation adjusts based on the user’s login status: users who are not logged in will see options to sign in or create an account, while logged-in users will see options to access their profile and log out. Additionally, any attempt to access features requiring an account will automatically redirect users to the sign-up or login page, ensuring a smooth and intuitive experience.
  - **Purpose**: Provides a consistent and accessible navigation experience across devices, ensuring users can quickly find and navigate the site’s primary features.
  - **User Story**: As a user, I want a clear navigation menu so that I can easily find and access different parts of the website.
  - **Implementation**:
    - **Bootstrap Navbar Setup**: The navigation bar was built using Bootstrap’s navbar documentation as a foundation, ensuring responsiveness across different screen sizes and providing a familiar structure for easy navigation.
    - **Customization and Styling**: The navbar was then customized and styled to align with the site's visual identity and user experience goals. Colours, fonts, and spacing were modified to match the overall design theme, and custom CSS was applied to enhance the aesthetic and usability.
    - **Dynamic Links Based on User Status**: 
      - Conditional logic was implemented to display different navigation options based on the user’s login status. 
      - Logged-out users see options for signing in and creating an account, while logged-in users see links to their profile and a log-out option.
    - **Automatic Redirects**: For any actions requiring an account (like adding a recipe or leaving a review), users are automatically redirected to the login page.
    - **Dropdown Menu**: For smaller screen sizes a dropdown icon is displayed instead of the nav items, displaying a list of nav items, styled for a smaller screen size, this allows for a clean aesthetic across all screen types.

![Navbar Feature](/docs/readme_images/navbar_signed_out.webp)
![Navbar Feature](/docs/readme_images/navbar_signed_in.webp)
![Navbar Feature](/docs/readme_images/navbar_dropdown_icon.webp)
![Navbar Feature](/docs/readme_images/navbar_dropdown_items.webp)

- **Footer**  
  - **Description**: The footer includes links to social media, appearing at the bottom of every page.
  - **Purpose**: The footer offers additional navigation options and information, enhancing user accessibility.
  - **User Story**: As a user, I want a footer with extra links so that I can quickly access more resources or reach out if needed.

![Footer Feature](/docs/readme_images/footer.webp)

- **View All Recipes**  
  - **Description**: A page displaying all recipes available on the platform, with options to filter recipes by meal type.
  - **Purpose**: Allows users to explore a wide variety of recipes, encouraging discovery.
  - **User Story**: As a user, I want to see a list of all recipes so that I can browse and find interesting dishes to try.

![View All Recipes Feature](/docs/readme_images/view_all_recipes.webp)

- **Recipe Detail Page**  
  - **Description**: A dedicated page displaying all details of a selected recipe. This page serves as a comprehensive view where users can fully explore a recipe and decide if they want to try it, additionally, for the owner of the recipe, options to edit or delete said recipe will be present, and they will not have access to the option to leave a review on their own recipe.
  - **Purpose**: The recipe detail page allows users to access all necessary information about a recipe in one place, supporting informed decisions and encouraging engagement through ratings.
  - **User Story**: As a user, I want to view all details of a recipe so that I can understand the ingredients and instructions before deciding to make it.
  - **Implementation**:
    - **Recipe Model Information**: The page displays all fields from the recipe model, including the title, providing users with a complete recipe overview.
    - **Ratings**: User ratings are prominently displayed, helping users gauge the recipe's quality based on community feedback.
    - **View and Template**: A Django view retrieves the recipe details and passes them to the template. The template is structured to showcase the recipe information clearly and highlight interactive elements like the rating, edit or delete features.
    - **User Interaction**: Logged-in users can leave a rating directly from this page, while users who are the author of the recipe will instead of being able to leave a rating, they will have options to edit or delete the recipe 
    - **Navigation Options**: Links to go back to the list of all recipes or navigate to other areas of the site are included for ease of use.

![Recipe Detail Feature](/docs/readme_images/recipe_detail.webp)

- **Create an Account**  
  - **Description**: Users can register an account, providing them access to additional features like creating and reviewing recipes, provides success message upon account creation and sign in.
  - **Purpose**: Enables a personalized experience and grants access to interactive features, enhancing user engagement.
  - **User Story**: As a new user, I want to create an account so that I can add my own recipes and participate in the community.

![Sign Up Feature](/docs/readme_images/sign_up.webp)
![Sign Up Feature](/docs/readme_images/sign_in_success.webp)


- **Log In Page**  
  - **Description**: A simple and secure page where users can enter their credentials to access their account. The log-in page provides fields for a username and password.
  - **Purpose**: Allows registered users to authenticate themselves granting them access to their personalized account features, including creating and managing recipes, leaving reviews, and accessing their profile.
  - **User Story**: As a user, I want to log in to my account so that I can interact with the website fully.
  - **Implementation**:
    - **Form Fields**: Users are presented with fields for entering their username and password.
    - **Feedback**: If login fails, users receive an error message prompting them to recheck their credentials. Successful logins redirect users to the homepage or to the create a recipe page if the user had previously attempted to navigate to that page while not logged in.
    - **Password Recovery**: A link to reset a forgotten password is available to help users regain access to their account easily.
    - **Navigation**: Users not registered are encouraged to sign up through a link on this page, ensuring they know how to access the platform’s full features.

![Log In Feature](/docs/readme_images/sign_in.webp)
![Log In Feature](/docs/readme_images/sign_in_success.webp)


- **Sign Out Page**  
  - **Description**: A page or button that allows logged-in users to log out of their account, ending their session on the site.
  - **Purpose**: Enables users to sign out of their accounts when they’re finished using the site, helping to maintain privacy and security.
  - **User Story**: As a user, I want to log out of my account when I’m done to ensure my account remains secure.
  - **Implementation**:
    - **Log Out**: A button or link is available on the navigation bar, allowing users to log out with a single click.
    - **Redirect**: After logging out, users are redirected to the homepage, confirming that their session has ended.

![Log Out Feature](/docs/readme_images/sign_out.webp)
![Log Out Feature](/docs/readme_images/sign_out_success.webp)

- **Create a Recipe**  
  - **Description**: Allows logged in users to add new recipes by entering details such as the recipe title, ingredients, instructions, meal-type, calories, date of creation.
  - **Purpose**: This feature enables users to share their own culinary creations with the community, contributing to a diverse collection of recipes available on the platform.
  - **User Story**: As a user, I want to create a recipe so that I can share and store my cooking creations.
  - **Implementation**:
    - **Recipe Model**: A Django model was created to store recipe information.
    - **Recipe Creation Form**: Users access a form that allows them to input recipe details, which is only accessible to registered users to ensure that only authenticated users contribute content.
    - **View and Template**: A view handles the recipe creation process, validating inputs and saving data to the database. The template offers a clear, user-friendly interface to guide users in submitting their recipe.
    - **Feedback**: Upon successfully adding a recipe, users receive a success message to confirm that their recipe was added. If any input errors occur, users are notified to correct the entry before being able create it.

![Create Recipe Feature](/docs/readme_images/add_recipe.webp)
![Create Recipe Feature](/docs/readme_images/create_recipe_success.webp)

- **Edit Recipe**  
  - **Description**: Allows users to edit their own recipes, updating ingredients, instructions, or the image as needed.
  - **Purpose**: Allows users to keep their recipes up-to-date or refine them over time, enhancing the quality of the content on the platform.
  - **User Story**: As a user, I want to edit my recipes so that I can improve or update them based on feedback or new ideas.

![Edit Recipe Feature](/docs/readme_images/edit_recipe_form.webp)
![Edit Recipe Feature](/docs/readme_images/edit_recipe_success.webp)

- **Delete Recipe**  
  - **Description**: Users can delete any of their recipes, permanently removing them from the platform.
  - **Purpose**: Allows users to manage their content and remove recipes that they no longer wish to share.
  - **User Story**: As a user, I want to delete my recipes so that I can remove any recipes i no longer wish to share and store on the site.

![Delete Recipe Feature](/docs/readme_images/delete_recipe_page.webp)
![Delete Recipe Feature](/docs/readme_images/delete_recipe_success.webp)

- **Profile Page**  
  - **Description**: A page where logged in users can view their account information and see a list of all the recipes they have created. From here, they can also edit or delete their recipes, users who have not logged in will instead see navigation items to log in, or sign up in the profile links stead.
  - **Purpose**: The profile page provides users with a central hub to manage their contributions, allowing them to easily access, update, or remove their content as needed.
  - **User Story**: As a user, I want a profile page where I can see my account information and all of my recipes so that I can manage my content and keep track of my contributions.
  - **Implementation**:
    - **User Information Display**: Basic account information, such as the username, email, and date of account creation is displayed at the top of the profile page for easy access.
    - **Recipe List**: Below the account information for smaller screen sizes, and alongside it, a list of the user’s recipes is displayed. Upon clicking a recipe, the user is directed to the recipe detail page. Which shows the recipe information and has options to edit or delete the recipe.
    - **View and Template**: A Django view retrieves the logged-in user’s information and their associated recipes, passing them to the profile page template. The template is designed to clearly separate account details from the list of recipes.
    - **Edit and Delete Options**: For each recipe listed, users have buttons to edit or delete the recipe directly from the profile page, allowing for efficient content management without navigating to other pages.
    - **Feedback**: After editing or deleting a recipe, users receive a confirmation message, ensuring they know their action was successful.

![Profile View Feature](/docs/readme_images/profile.webp)
![Profile View Feature](/docs/readme_images/profile_display_column.webp)


- **Return Button**  
  - **Description**: A button that allows users to return to their previous page, located on pages such as recipe details or edit recipe, where users may want to navigate back to their previous view.
  - **Purpose**: The return button improves navigation by allowing users to easily return to where they came from without needing to use browser controls, enhancing user convenience and flow.
  - **User Story**: As a user, I want a “Return" button so that I can quickly return to the previous page.
  - **Implementation**:
    - **JavaScript Navigation**: The button uses JavaScript’s `history.back()` function, which takes the user back to their last visited page in the session history.
    - **Placement and Styling**: The button is styled to be easily visible but unobtrusive, located near the bottom of the page for intuitive access.

![Return Feature](/docs/readme_images/go_back_btn.webp)

- **5-Star Rating System**  
  - **Description**: Allows logged-in users who are not the owner of a recipe to rate it on a scale of 1 to 5 stars. The site then calculates and displays the average rating of each recipe based on all user ratings.
  - **Purpose**: This feature enables community members to provide feedback and helps others identify popular, high-quality recipes. By displaying the average rating, it provides a quick visual indicator of a recipe’s overall quality.
  - **User Story**: As a user, I want to rate recipes I’ve tried so that I can share my feedback and help others discover quality dishes.
  - **Implementation**:
    - **Rating Model**: A separate Django model was created to store individual ratings for each recipe, linked to the user and the recipe.
    - **Rating Submission**: Only logged-in users who are not the recipe’s owner can submit a rating.
    - **Average Calculation**: Each time a recipe is rated, the average rating is recalculated and stored in the recipe model. This average rating is then displayed on the recipe’s detail page for all users to see.
    - **Feedback**: Upon successfully submitting a rating, users receive a success message confirming that their rating has been added. If users encounter any issues (e.g., trying to rate their own recipe), an error message informs them of the restriction, logic has been implemented to only show the option to rate the recipe to users who are not the author of the recipe however, which helps prevents such an issue occuring.

  ![Rating Feature](/docs/readme_images/rate_recipe.webp)
  ![Average Rating Feature](/docs/readme_images/average_rating.webp)
  ![Rating Success](/docs/readme_images/rate_recipe_success.webp)

- **Action Success Alert Messages**  
  - **Description**: Display a success alert message whenever a user completes an action successfully, such as creating, editing, or deleting a recipe, leaving a review, signing up/out/in.
  - **Purpose**: This feature provides immediate feedback to users, confirming that their action was completed successfully. Success messages improve usability by assuring users that their interaction was processed.
  - **User Story**: As a user, I want to receive a confirmation message when I complete an action, so that I know my changes or actions have been successfull.
  - **Implementation**:
    - **Customization**: Success messages are styled to match the site's theme, appearing at the top right of the page.
    - **Close Option**: The user can manually dismiss them, ensuring that the page remains clean and uncluttered.

![Success Messages Feature](/docs/readme_images/sign_in_success.webp)
![Success Messages Feature](/docs/readme_images/sign_out_success.webp)
![Success Messages Feature](/docs/readme_images/edit_recipe_success.webp)
![Success Messages Feature](/docs/readme_images/rate_recipe_success.webp)
![Success Messages Feature](/docs/readme_images/create_recipe_success.webp)
![Success Messages Feature](/docs/readme_images/delete_recipe_success.webp)

- **Custom 404, 403, and 500 Error Pages**  
  - **Description**: Custom error pages are provided for common HTTP errors: 404 (Page Not Found), 403 (Forbidden), and 500 (Internal Server Error). These pages include user-friendly messages, a clear layout, and links back to the main sections of the site.
  - **Purpose**: Custom error pages enhance user experience by providing helpful feedback when issues occur, guiding users back to functional parts of the site instead of displaying default error messages that may be confusing or abrupt.
  - **User Story**: As a user, I want informative error pages so that I understand what went wrong and know how to return to working sections of the site.
  - **Implementation**:
    - **Error Page Templates**: Three separate HTML templates were created for each error type. Each template features a message explaining the error, and a link back to the homepage..
    - **Styling**: The error pages use consistent styling with the rest of the site, including the site's color scheme, typography, and branding elements. This ensures the error pages feel cohesive and user-friendly.
    - **View Configuration**: Django’s settings were configured to recognize and display these custom error templates whenever the corresponding HTTP errors occur. The `DEBUG` setting is set to `False` in production to allow Django to use the custom error pages.
    - **Testing**: Each error page was tested by intentionally causing specific errors (e.g., navigating to a nonexistent page for 404, testing permissions for 403, and simulating a server error for 500) to ensure they display correctly and offer a helpful experience.

  ![404 Error Page](/docs/readme_images/404_error.webp)
  ![403 Error Page](/docs/readme_images/403_error.webp)
  ![500 Error Page](/docs/readme_images/500_error.webp)

#### Features Left To Implement

### Potential Future Features to Implement

To enhance the user experience and expand the functionality of the **Recipe Blog**, the following features would improve the site:

- **Advanced Search and Filter Options**  
  - **Description**: Implement additional filters allowing users to search recipes by cuisine type, dietary restrictions, preparation time, and other attributes.
  - **Purpose**: This feature would allow users to quickly find recipes that suit their specific needs, enhancing the discoverability of content.

- **Recipe Categories and Tags**  
  - **Description**: Enable users to categorize or tag recipes (e.g., "Vegetarian," "Quick Meals," "Desserts") to facilitate browsing by theme.
  - **Purpose**: Categories and tags would make it easier for users to explore recipes by topic, creating a more organized and tailored browsing experience.

- **Recipe Collections or “Cookbooks”**  
  - **Description**: Provide a feature for users to save recipes into custom collections or digital "cookbooks" within their profile.
  - **Purpose**: This would offer users a way to organize their favorite recipes, making it easy to access them later and encouraging return visits.

- **Commenting on Reviews**  
  - **Description**: Enable users to comment on reviews or respond to feedback on their recipes.
  - **Purpose**: This feature would increase community interaction and allow for more in-depth feedback and engagement between users.

- **Weekly or Monthly Recipe Highlights**  
  - **Description**: Feature a "Recipe of the Week" or "Top Recipes of the Month" section, showcasing popular or highly-rated recipes.
  - **Purpose**: Highlighting popular recipes would promote community favorites and encourage users to engage with trending content.

- **In-App Messaging**  
  - **Description**: Allow users to message each other directly within the platform to share tips, collaborate on recipes, or give private feedback.
  - **Purpose**: This feature would enhance social interaction, building a stronger sense of community and encouraging users to connect over shared interests.

### Skeleton 

#### Wireframes
-**Home Page**:
![Home Wireframe Page](/docs/wireframe_images/home_wireframe.webp)

-**Navbar**:
![Navbar Wireframe](/docs/wireframe_images/navbar_wireframe.webp)

-**Footer**:
![Footer Wireframe](/docs/wireframe_images/footer_wireframe.webp)

-**View all Recipes Page**:
![View All Recipes Wireframe Page](/docs/wireframe_images/view_all_wireframe.webp)

-**Recipe Detail Page**:
![Recipe Detail Wireframe Page](/docs/wireframe_images/recipe_detail_wireframe.webp)

-**Sign Up Page**:
![Sign Up Wireframe Page](/docs/wireframe_images/sign_up.webp)

-**Sign In Page**:
![Sign In Wireframe Page](/docs/wireframe_images/log_in_wireframe.webp)

-**Sign Out Page**:
![Sign Out Wireframe Page](/docs/wireframe_images/sign_out.webp)

-**Add a Recipe Page**:
![Add Recipe Wireframe Page](/docs/wireframe_images/add_recipe_wireframe.webp)

-**Edit Recipe Page**:
![Edit Recipe Wireframe Page](/docs/wireframe_images/edit_recipe_wireframe.webp)

-**Delete Recipe Page**:
![Delete Recipe Wireframe Page](/docs/wireframe_images/delete_recipe_wireframe.webp)

-**Profile Page**:
![Profile Wireframe Page](/docs/wireframe_images/profile_wireframe.webp)

-**Error Pages**:
  - 404:
![Error404 Wireframe Page](/docs/wireframe_images/404error_wireframe.webp)
  - 403: 
![Error403 Wireframe Page](/docs/wireframe_images/403error_wireframe.webp)
  - 500:
![Error500 Wireframe Page](/docs/wireframe_images/500error_wireframe.webp)

#### Database Design
Describe the database schema.

#### Security
List security features.

### Surface

#### Design
### Design Approach

The **Recipe Blog** site follows a clean and accessible design approach, aimed at creating an intuitive and enjoyable user experience. Key elements of this approach include simplicity, visual balance, and responsiveness, ensuring that users can easily navigate the site, discover content, and interact with features regardless of their device or screen size.

#### Key Design Principles

- **Simplicity and Clarity**  
  The layout is designed to be straightforward, with a clear hierarchy that guides users’ attention to key elements such as the navigation bar, featured recipes, and action buttons. Each page is structured to minimize clutter, allowing content to be the primary focus.

- **Visual Consistency**  
  A cohesive color scheme and font choices are applied consistently across all pages. Colors and typography were selected to reflect the culinary theme while maintaining high readability. Consistent styling of buttons, forms, and interactive elements helps users easily identify actionable items.

- **Accessibility**  
  Accessibility is prioritized to ensure that all users, can engage with the site. Font sizes, color contrasts, and alternative text for images have been considered to meet accessibility standards. The color scheme also provides a high contrast between text and background, enhancing readability.

- **Responsive Design**  
  The site is fully responsive, adapting smoothly to different screen sizes. This ensures that users have a positive experience on any device, whether they are on a desktop, tablet, or mobile phone. Elements are arranged to flow naturally on smaller screens, with images and text resising appropriately.

- **User-Centric Navigation**  
  Navigation is intuitive, that provides quick access to the main sections. The placement and functionality of navigation elements are designed to minimize user effort, allowing users to quickly find what they need.

This design approach creates a visually appealing, user-friendly experience, making it easy for users to explore recipes, create new content, and connect with the community.

#### Colour Scheme

The **Recipe Blog** site uses a cohesive, natural color scheme that reflects a calm, inviting atmosphere, enhancing readability and user engagement. The colors were chosen to complement the culinary theme and create a visually appealing user experience. Additionally, Bootstrap’s primary and secondary color classes were integrated in some of the buttons and anchor tags.

- **Deep Green (#3A6351)**  
  This rich green serves as the about us sections background colour. It conveys freshness and naturalness, aligning well with the culinary theme.

- **Light Blue (#edf7ff)**  
  This very light blue serves as the primary background color, providing a clean canvas that helps content stand out.

- **Deep Navy (#013870)**  
  Used in the navigation bar footer, forms, and as the background colour for recipe information boxes, this stable, strong color enhances contrast and draws attention, ensuring accessibility and easy site navigation.

- **Dark Gray (#333)**  
  This color is used for the primary text, chosen for its high readability against lighter backgrounds to ensure content is easily readable.

- **Darker Gray (#222)**  
  A slightly darker shade than the text color, this is used specifically for headings to create subtle emphasis and guide the user’s attention to key sections.

- **Coral Accent (#FF6F61)**  
  This warm coral accent color is used for hover effects, call-to-action buttons, and highlights. It adds vibrancy to the design and draws attention to important interactive elements.

- **White (#ffffff)**  
  This color is used as a neutral background and for text in certain elements, enhancing contrast and ensuring that text and icons are always visible on darker backgrounds.

These colors create a welcoming and balanced aesthetic, supporting the platform's overall goals of making the Recipe Blog visually appealing, accessible, and user-friendly, without drawing attention away from the main focus of the page, the recipes.

#### Typography

The **Recipe Blog** uses a combination of two fonts, **Roboto** and **Playfair Display**, to create a harmonious balance between readability and visual elegance.

- **Roboto**  
  - **Usage**: Primarily used for body text, navigation links, and UI elements.
  - **Rationale**: Roboto is a clean, modern sans-serif font good for its readability across different screen sizes. Its simplicity complements the design and ensures that content remains legible, providing a smooth reading experience for users.

- **Playfair Display**  
  - **Usage**: Applied to headings, titles, and highlighted elements.
  - **Rationale**: Playfair Display is a serif font with a classic, elegant feel, adding a touch of sophistication to the site. It helps create visual contrast against Roboto, drawing users’ attention to key sections and enhancing the site’s aesthetic appeal.

This font combination balances functionality with style, supporting the Recipe Blog’s goal of providing an inviting and user-friendly experience while maintaining a visually pleasing, professional appearance.

#### Imagery

The **Recipe Blog** site uses carefully chosen imagery to enhance its visual appeal and create an inviting atmosphere. While images are used sparingly, each one has a specific purpose and contributes to the overall user experience.

- **Logo**  
  - **Description**: The logo is a simple, image of a plate with a fork and knife crossed over each other, symbolizing dining and food. The logo is animated to rotate, adding a subtle, dynamic effect to the branding.
  - **Purpose**: This rotating logo adds a unique touch to the site, establishing a memorable brand image that aligns with the site's focus on food and recipes.

- **Carousel Images**  
  - **Description**: The homepage features a sliding carousel with three images: gyros, meal prep containers, and a bowl of soup. Each image represents different types of meals, showcasing the diversity of recipes available on the site.
  - **Purpose**: The carousel provides a visually engaging introduction to the site, giving users an immediate sense of the culinary variety they can expect to find. The use of high-quality, appetizing images is designed to draw users in and inspire them to explore recipes.

- **About Us Image**  
  - **Description**: The "About Us" section includes an image displayed alongside the text, reinforcing the site's community-focused mission and adding a personal, welcoming feel to this page.
  - **Purpose**: This image complements the introductory text in the "About Us" section. It is 

Each image on the site has been carefully selected to support the Recipe Blog’s brand and user experience. By using food-related imagery in key sections, the site creates a visually cohesive experience that resonates with its target audience and enhances the appeal of the platform.

## Technologies
List all technologies and frameworks used, including frontend, backend, and database.

# Testing

## Manual Testing:

### 1. Navigation Bar Functionality

**Description**: Test that the navigation bar appears on all pages and correctly links to all main sections (e.g., Home, Add Recipe, View All Recipes, Login/Register, and for logged in users, log out, and profile).

**Steps**:
1. Visit each page of the site.
2. Verify that the navigation bar is present and responsive on each page.
3. Click each navigation link to confirm it redirects to the intended section.

**Expected Result**: The navigation bar is visible on all pages and links work as expected, redirecting to the correct section.
**Actual Result**: All steps carried out successfully.

### 2. User Registration

**Description**: Test the user registration functionality to ensure users can create an account.

**Steps**:
1. Navigate to the registration page.
2. Complete the registration form with valid details.
3. Submit the form.

**Expected Result**: The user is redirected to the homepage with a success message.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Registration Test Result](/docs/readme_images/sign_in_success.webp)

### 3. User Login

**Description**: Ensure that registered users can log in with their credentials.

**Steps**:
1. Navigate to the login page.
2. Enter valid login credentials.
3. Submit the login form.

**Expected Result**: The user is redirected to their profile or homepage with a success message, and the navigation bar updates to show logged-in options.
**Actual Result**: All steps carried out successfully.


**Navbar Before Sign-In**:
![Signed Out Navbar](/docs/readme_images/navbar_signed_out.webp)

**Navbar After Sign-In**:
![Signed Out Navbar](/docs/readme_images/navbar_signed_in.webp)

**Sign in Success Message**:
![Login Success Message](/docs/readme_images/sign_in_success.webp)

### 4. Create a Recipe

**Description**: Test that logged-in users can create and submit a new recipe with all required fields.

**Steps**:
1. Log in as a registered user.
2. Navigate to the "Add Recipe" page.
3. Fill out the recipe form with valid data.
4. Submit the form.

**Expected Result**: The recipe is saved, and a success message is displayed. The new recipe appears in the user’s profile and in the "All Recipes" section.
**Actual Result**: All steps carried out successfully.

**Result Images**:
![Add Recipe Form Filled Out](/docs/readme_images/add_recipe_form_filled.webp)
![Create Recipe Success Message](/docs/readme_images/create_recipe_success.webp)
![Recipe In All Recipe List](/docs/readme_images/recipe_displayed_in_view_all.webp)
![Recipe In Profile](/docs/readme_images/recipe_in_profile.webp)

### 5. Edit Recipe

**Description**: Verify that users can edit recipes they have created.

**Steps**:
1. Log in as a user who has created at least one recipe, if one is not available, create a recipe.
2. Navigate to the recipe’s detail page.
3. Click "Edit" and update recipe information.
4. Submit the updated form.

**Expected Result**: The recipe updates successfully, with a success message, and displays the modified details.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Edit Recipe Test Result](/docs/readme_images/edit_recipe_form.webp)
![Edit Recipe Test Result](/docs/readme_images/edit_recipe_success.webp)

### 6. Delete Recipe

**Description**: Ensure that users can delete recipes they have created.

**Steps**:
1. Log in as a user with recipes.
2. Go to a recipe’s detail page.
3. Click "Delete" and confirm the deletion.

**Expected Result**: The recipe is removed from the site, and a success message confirms the deletion.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Delete Recipe Test Result](/docs/readme_images/delete_recipe_page.webp)
![Delete Recipe Test Result](/docs/readme_images/delete_recipe_success.webp)

### 7. View All Recipes

**Description**: Test that all users can view the complete list of recipes.

**Steps**:
1. Navigate to the "All Recipes" page.
2. Scroll through the list to check if recipes load correctly.

**Expected Result**: The page displays a list of all recipes.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![All Recipes Test Result](/docs/readme_images/view_all_recipes.webp)

### 8. Recipe Detail Page

**Description**: Verify that users can view the full details of each recipe.

**Steps**:
1. Go to any recipe from the "All Recipes" page.
2. Click on the recipe to open the detail page.

**Expected Result**: The recipe detail page displays all information.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Recipe Detail Test Result](/docs/readme_images/recipe_detail.webp)

### 9. Rating a Recipe

**Description**: Test that logged-in users can leave a rating on a recipe they didn’t create.

**Steps**:
1. Log in and view a recipe created by another user.
2. Select a rating and submit it.

**Expected Result**: The rating is saved, the average rating is updated, and a success message is displayed.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Rating Test Result](/docs/readme_images/recipe_detail.webp)

### 10. Profile Page Display

**Description**: Ensure the profile page displays the user’s account information and their recipes.

**Steps**:
1. Log in and navigate to the profile page.
2. Review displayed information and recipe list.

**Expected Result**: The profile page shows the user's account details and a list of their recipes, also with options to edit or delete when viewed in recipe detail page.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Profile Page Test Result](/docs/readme_images/profile.webp)
![Recipe Detail Test Result](/docs/readme_images/test_recipe_detail.webp)

### 11. Responsive Design Test

**Description**: Verify that the site is responsive and adjusts correctly on different screen sizes.

**Steps**:
1. Open the site on various screen sizes (desktop, tablet, mobile).
2. Check the layout and functionality on each device.

**Expected Result**: The layout adjusts properly, and all elements are accessible on all screen sizes.
**Actual Result**: All steps carried out successfully, except for the about us image, which i decided to remove as it did not look good in smaller screen sizes, navbar modified to transform links into dropdown icon, on smaller screen sizes, instead displaying them in a column inside the dropdown, View all recipes also changed to display Recipes in columns instead of rows, profile display also changed to column. 



**Result Image**:
![Responsive Design Removed About Image](/docs/readme_images/about_us_no_image.webp)
![Responsive Design Nav Dropdown](/docs/readme_images/navbar_dropdown_icon.webp)
![Responsive Design Dropdown Items](/docs/readme_images/navbar_dropdown_items.webp)
![Responsive Design View All displayed in Column](/docs/readme_images/recipe_list_column.webp)
![Responsive Design Profile Displayed in Column](/docs/readme_images/profile_display_column.webp)

### 12. Logout Functionality

**Description**: Test that users can log out and return to the homepage.

**Steps**:
1. Log in, then click "Logout" in the navigation bar.
2. Verify redirection to the comfirmation page, click Sign out.
3. Verify redirection to the homepage with success message.

**Expected Result**: The user is logged out, the homepage loads with success message, and the navigation bar updates to show logged-out options.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Logout Test Result](/docs/readme_images/sign_out_success.webp)
![Logout Test Navbar Update](/docs/readme_images/navbar_signed_out.webp)

### 13. Error Pages (404, 403, 500)

**Description**: Check that custom error pages display for invalid URLs or server errors, or unauthorised access.

**Steps**:
1. Enter an invalid URL to trigger a 404 error.
2. Force a server error to view the 500 error page (if possible).
2. Attempt to open page with unauthorised access.

**Expected Result**: Custom 404, 403 and 500 pages display with user-friendly messages and return options.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Error Page Test Result](/docs/readme_images/404_error.webp)
![Error Page Test Result](/docs/readme_images/500_error.webp)
![Error Page Test Result](/docs/readme_images/403_error.webp)

### 14. Deployment Tests (Heroku)

**Description**: Confirm the site deploys successfully and operates correctly on Heroku.

**Steps**:
1. Deploy to Heroku.
2. Test site functionalities as listed above, and successfully loads static files.

**Expected Result**: All features work as expected on the deployed site.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Deployment Test Result](/docs/readme_images/heroku_successful_load.webp)

## Deployment

### Version Control

The **Recipe Blog** project was developed using **Gitpod** as the IDE, with Git for version control, and the code was stored in a remote GitHub repository.

Throughout development, the following Git commands were used to manage and push code updates:

- **`git add <file>`**  
  Adds the specified file(s) to the staging area, preparing them for a commit.

- **`git commit -m "commit message"`**  
  Commits the changes in the staging area to the local repository with a descriptive message.

- **`git push`**  
  Pushes all committed changes from the local repository to the remote repository on GitHub.

### Heroku Deployment

The **Recipe Blog** site was deployed to Heroku, a cloud platform that allows easy deployment and scaling of web applications. Follow these steps to deploy the project on Heroku:

1. **Set Up Heroku**
   - Go to [Heroku](https://www.heroku.com/) and create an account (or log in if you already have one).
   - In your Heroku dashboard, click the **New** button in the top right corner and select **Create New App**.
   - Choose an **App Name** (it must be unique across Heroku) and select the appropriate **Region** based on your location.
   - Click **Create App**.

2. **Configure Environment Variables**
   - Go to the **Settings** tab and click **Reveal Config Vars** to add necessary environment variables.
   - Add the following config vars:
     - `SECRET_KEY`: Your Django project's secret key.
     - `DATABASE_URL`: This should already be set by the Heroku Postgres add-on.
   - Save each config var after entering.

3. **Deploy with GitHub Integration**
   - Go to the **Deploy** tab and scroll down to **Deployment method**.
   - Under **Connect to GitHub**, click **Connect** and authorize Heroku to access your GitHub account if prompted.
   - In the search box, find the repository you want to deploy, then click **Connect** to link it to Heroku.

4. **Deploy the Application**
   - In the **Manual deploy** section, select the **main** branch and click **Deploy Branch**.
   - Heroku will begin building and deploying your app. Once completed, a message should confirm that the app was successfully deployed.
   - Click **View** to open your live site.

5. **Automatic Deploys (Optional)**
   - To enable continuous deployment, scroll to **Automatic deploys** and enable it for the main branch. This will automatically deploy new updates whenever you push to the main branch on GitHub.

Your application should now be live on Heroku! This setup provides a scalable and reliable environment for your Django project.

### Run Locally

To run the **Recipe Blog** project on your local machine, follow these steps:

1. **Clone the Repository**
   - Go to the GitHub repository you wish to clone.
   - Click on the **Code** dropdown button and select **HTTPS**.
   - Copy the repository link provided.

2. **Clone the Project Locally**
   - Open your IDE or terminal of choice (ensure **Git** is installed on your machine).
   - In the terminal, type the following command, replacing `copied-git-url` with the URL you copied:
     ```bash
     git clone copied-git-url
     ```
   - Press **Enter** to clone the project. The repository will now be downloaded to your local machine.

3. **Set Up Environment Variables**
   - Within the project directory, create a `.env` file to store your environment variables.
   - Add the necessary keys, such as `SECRET_KEY`, `DATABASE_URL`, and any others required for the project.

4. **Install Dependencies**
   - Navigate into the project directory and install the required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

5. **Apply Migrations**
   - Run the following command to set up the database:
     ```bash
     python manage.py migrate
     ```

6. **Run the Server**
   - Start the Django development server:
     ```bash
     python manage.py runserver
     ```
   - Open your browser and go to `http://127.0.0.1:8000` to view the application locally.

The project is now ready to be used on your local machine for development and testing.

### Fork Project

Forking a project allows you to create your own copy of someone else’s repository, making it easy to propose changes, experiment, or use it as a foundation for a new project.

To fork the **Recipe Blog** repository:

1. **Navigate to the Repository**
   - Go to the GitHub repository page that you want to fork.

2. **Create the Fork**
   - In the top right corner of the page, click the **Fork** button.
   - GitHub will create a copy of the full project in your own GitHub account.

3. **Modify and Experiment**
   - You now have a duplicate of the original project under your account. You can make changes to your forked copy without affecting the original repository.
   - If you wish to propose changes to the original project, you can submit a **pull request** from your forked repository.

This process also allows you to test changes before pushing it to the main/master branch.

## Credits
Acknowledge any resources, libraries, or individuals who contributed to the project.
