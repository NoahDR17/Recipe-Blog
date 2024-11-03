# Testing Plan for Recipe Blog Project

## 1. Navigation Bar Functionality

**Description**: Test that the navigation bar appears on all pages and correctly links to all main sections (e.g., Home, Add Recipe, View All Recipes, Login/Register, and for logged in users, log out, and profile).

**Steps**:
1. Visit each page of the site.
2. Verify that the navigation bar is present and responsive on each page.
3. Click each navigation link to confirm it redirects to the intended section.

**Expected Result**: The navigation bar is visible on all pages and links work as expected, redirecting to the correct section.
**Actual Result**: All steps carried out successfully.

## 2. User Registration

**Description**: Test the user registration functionality to ensure users can create an account.

**Steps**:
1. Navigate to the registration page.
2. Complete the registration form with valid details.
3. Submit the form.

**Expected Result**: The user is redirected to the homepage with a success message.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Registration Test Result](/docs/readme_images/sign_in_success.webp)

## 3. User Login

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

## 4. Create a Recipe

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

## 5. Edit Recipe

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

## 6. Delete Recipe

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

## 7. View All Recipes

**Description**: Test that all users can view the complete list of recipes.

**Steps**:
1. Navigate to the "All Recipes" page.
2. Scroll through the list to check if recipes load correctly.

**Expected Result**: The page displays a list of all recipes.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![All Recipes Test Result](/docs/readme_images/view_all_recipes.webp)

## 8. Recipe Detail Page

**Description**: Verify that users can view the full details of each recipe.

**Steps**:
1. Go to any recipe from the "All Recipes" page.
2. Click on the recipe to open the detail page.

**Expected Result**: The recipe detail page displays all information.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Recipe Detail Test Result](/docs/readme_images/recipe_detail.webp)

---

## 9. Rating a Recipe

**Description**: Test that logged-in users can leave a rating on a recipe they didn’t create.

**Steps**:
1. Log in and view a recipe created by another user.
2. Select a rating and submit it.

**Expected Result**: The rating is saved, the average rating is updated, and a success message is displayed.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Rating Test Result](/docs/readme_images/recipe_detail.webp)

---

## 10. Profile Page Display

**Description**: Ensure the profile page displays the user’s account information and their recipes.

**Steps**:
1. Log in and navigate to the profile page.
2. Review displayed information and recipe list.

**Expected Result**: The profile page shows the user's account details and a list of their recipes, also with options to edit or delete when viewed in recipe detail page.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Profile Page Test Result](/docs/readme_images/profile.webp)
![Recipe Detail Test Result](/docs/readme_images/test_recipe_detail.webp)

## 11. Responsive Design Test

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

## 12. Logout Functionality

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

## 13. Error Pages (404, 403, 500)

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

## 14. Deployment Tests (Heroku)

**Description**: Confirm the site deploys successfully and operates correctly on Heroku.

**Steps**:
1. Deploy to Heroku.
2. Test site functionalities as listed above, and successfully loads static files.

**Expected Result**: All features work as expected on the deployed site.
**Actual Result**: All steps carried out successfully.

**Result Image**:
![Deployment Test Result](/docs/readme_images/heroku_successful_load.webp)


