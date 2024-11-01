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


#### Features Left To Implement
- **Go back button on add a recipe, recipe detail page, edit recipe page, delete recipe page, log out page, error pages.
- **Confirmation notification on succesfull recipe creation, edit, delete, review, sign up/in/out etc...

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
Describe the overall design approach, aiming for a clean, accessible user experience.

#### Colour Scheme
List and explain the colours chosen for the site.

#### Typography
Specify the fonts used and the rationale behind the selection.

#### Imagery
Discuss the use of imagery, especially food-related images, to enhance the visual appeal of the site.

## Technologies
List all technologies and frameworks used, including frontend, backend, and database.

## Testing

## Deployment

### Version Control

### Heroku Deployment
Provide instructions for deploying the site to Heroku, including setup for PostgreSQL and Whitenoise for static files.

### Run Locally
Include a step-by-step guide for setting up the project locally, covering dependencies, environment variables, and local server setup.

### Fork Project
Instructions for users interested in forking the project for their own use.

## Credits
Acknowledge any resources, libraries, or individuals who contributed to the project.
