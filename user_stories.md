# User Stories

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