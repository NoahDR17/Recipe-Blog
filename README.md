# Recipe Blog Project
### Introduction 
**Recipe Blog** is an interactive online platform that brings together food enthusiasts from around the world to share, discover, and celebrate culinary creations. The app allows users to create, edit, and manage their own recipes while exploring those shared by others. It also includes a rating and review system, enabling users to share feedback and discover top-rated recipes. With personalised profiles and an intuitive design, Recipe Blog offers a user-friendly experience for anyone looking to document their culinary adventures, try new dishes, and connect with a like-minded community. """Live Link"""

"""Website Preview Display"""

## Table of Contents
- [User Experience Design](#user-experience-design)
  - [The Strategy Plane](#the-strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile Planning](#agile-planning)
    - [Epics](#epics)
    - [User Stories](#user-stories)
  - [The Scope Plane](#the-scope-plane)
  - [The Structure Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
    - [Potential Future Features to Implement](#potential-future-features-to-implement)


  - [The Skeleton Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database Design](#database-design)
    - [Security](#security)
  - [The Surface Plane](#the-surface-plane)
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

### The Strategy Plane

#### Site Goals
The **Recipe Blog** aims to provide a vibrant and engaging platform for users to share their culinary creations, explore new recipes, and connect with other food enthusiasts. The primary goals of the site include:

- **User-Friendly Experience**: To create an intuitive, accessible platform where users of all skill levels can easily navigate, share, and discover recipes. A streamlined design ensures that users can quickly find the features they need, whether they’re adding a new recipe, leaving a review, or browsing the latest dishes.

- **Recipe Sharing and Management**: To empower users to create, edit, and manage their own recipes. Each recipe entry is designed to be intuitive, allowing users to share their unique methods. Personal profile pages allow users to view and organize their recipes in one place, making it easy to revisit or modify their content.

- **Discovery and Exploration**: To inspire culinary discovery by enabling users to explore a wide variety of recipes shared by others. The platform offers filtering, allowing users to find recipes that match their preferences. A rating system allows users to provide feedback.

- **Community Interaction**: To foster a sense of community by allowing users to rate each other’s recipes. The platform encourages positive interactions, creating a collaborative space where users can learn, improve, and connect over shared culinary interests.

Through these goals, **Recipe Blog** aims to cultivate a welcoming environment where food enthusiasts can document their culinary journeys, discover new flavors, and engage in a meaningful community dedicated to the art of cooking.

#### Agile Planning
Outline the Agile approach taken, including the planning and development process.

#### Epics
List and briefly describe each epic.

#### User Stories
Detail the user stories covered by each epic.

### The Scope Plane

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

### The Structure Plane

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

- **Footer**  
  - **Description**: The footer includes links to social media, appearing at the bottom of every page.
  - **Purpose**: The footer offers additional navigation options and information, enhancing user accessibility.
  - **User Story**: As a user, I want a footer with extra links so that I can quickly access more resources or reach out if needed.

- **View All Recipes**  
  - **Description**: A page displaying all recipes available on the platform, with options to filter recipes by meal type.
  - **Purpose**: Allows users to explore a wide variety of recipes, encouraging discovery.
  - **User Story**: As a user, I want to see a list of all recipes so that I can browse and find interesting dishes to try.

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

- **Create an Account**  
  - **Description**: Users can register an account, providing them access to additional features like creating and reviewing recipes.
  - **Purpose**: Enables a personalized experience and grants access to interactive features, enhancing user engagement.
  - **User Story**: As a new user, I want to create an account so that I can add my own recipes and participate in the community.

- **Log In Page**  
  - **Description**: A simple and secure page where users can enter their credentials to access their account. The log-in page provides fields for a username and password.
  - **Purpose**: Allows registered users to authenticate themselves granting them access to their personalized account features, including creating and managing recipes, leaving reviews, and accessing their profile.
  - **User Story**: As a user, I want to log in to my account so that I can interact with the website fully.
  - **Implementation**:
    - **Form Fields**: Users are presented with fields for entering their username and password.
    - **Feedback**: If login fails, users receive an error message prompting them to recheck their credentials. Successful logins redirect users to the homepage or to the create a recipe page if the user had previously attempted to navigate to that page while not logged in.
    - **Password Recovery**: A link to reset a forgotten password is available to help users regain access to their account easily.
    - **Navigation**: Users not registered are encouraged to sign up through a link on this page, ensuring they know how to access the platform’s full features.

- **Sign Out Page**  
  - **Description**: A page or button that allows logged-in users to log out of their account, ending their session on the site.
  - **Purpose**: Enables users to sign out of their accounts when they’re finished using the site, helping to maintain privacy and security.
  - **User Story**: As a user, I want to log out of my account when I’m done to ensure my account remains secure.
  - **Implementation**:
    - **Log Out**: A button or link is available on the navigation bar, allowing users to log out with a single click.
    - **Redirect**: After logging out, users are redirected to the homepage, confirming that their session has ended.

- **Create a Recipe**  
  - **Description**: Allows logged in users to add new recipes by entering details such as the recipe title, ingredients, instructions, meal-type, calories, date of creation.
  - **Purpose**: This feature enables users to share their own culinary creations with the community, contributing to a diverse collection of recipes available on the platform.
  - **User Story**: As a user, I want to create a recipe so that I can share and store my cooking creations.
  - **Implementation**:
    - **Recipe Model**: A Django model was created to store recipe information.
    - **Recipe Creation Form**: Users access a form that allows them to input recipe details, which is only accessible to registered users to ensure that only authenticated users contribute content.
    - **View and Template**: A view handles the recipe creation process, validating inputs and saving data to the database. The template offers a clear, user-friendly interface to guide users in submitting their recipe.
    - **Feedback**: Upon successfully adding a recipe, users receive a success message to confirm that their recipe was added. If any input errors occur, users are notified to correct the entry before being able create it.

- **Edit Recipe**  
  - **Description**: Allows users to edit their own recipes, updating ingredients, instructions, or the image as needed.
  - **Purpose**: Allows users to keep their recipes up-to-date or refine them over time, enhancing the quality of the content on the platform.
  - **User Story**: As a user, I want to edit my recipes so that I can improve or update them based on feedback or new ideas.

- **Delete Recipe**  
  - **Description**: Users can delete any of their recipes, permanently removing them from the platform.
  - **Purpose**: Allows users to manage their content and remove recipes that they no longer wish to share.
  - **User Story**: As a user, I want to delete my recipes so that I can remove any recipes i no longer wish to share and store on the site.

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

- **Return Button**  
  - **Description**: A button that allows users to return to their previous page, located on pages such as recipe details or edit recipe, where users may want to navigate back to their previous view.
  - **Purpose**: The return button improves navigation by allowing users to easily return to where they came from without needing to use browser controls, enhancing user convenience and flow.
  - **User Story**: As a user, I want a “Return" button so that I can quickly return to the previous page.
  - **Implementation**:
    - **JavaScript Navigation**: The button uses JavaScript’s `history.back()` function, which takes the user back to their last visited page in the session history.
    - **Placement and Styling**: The button is styled to be easily visible but unobtrusive, located near the bottom of the page for intuitive access.

- **Action Success Alert Messages**  
  - **Description**: Display a success alert message whenever a user completes an action successfully, such as creating, editing, or deleting a recipe, leaving a review, signing up/out/in.
  - **Purpose**: This feature provides immediate feedback to users, confirming that their action was completed successfully. Success messages improve usability by assuring users that their interaction was processed.
  - **User Story**: As a user, I want to receive a confirmation message when I complete an action, so that I know my changes or actions have been successfull.
  - **Implementation**:
    - **Customization**: Success messages are styled to match the site's theme, appearing at the top right of the page.
    - **Close Option**: The user can manually dismiss them, ensuring that the page remains clean and uncluttered.



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

### The Skeleton Plane

#### Wireframes
Include links or images of the wireframes for key pages, such as Home, Recipe Detail, and Profile pages.

#### Database Design
Describe the database schema.

#### Security
List security features.

### The Surface Plane

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
