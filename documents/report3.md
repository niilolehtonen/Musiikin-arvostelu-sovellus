# Report 3 ('Välipalautus'):
* The current functionality of the application:
  - Users can create a user account, log in and log out.
  - Users can add a release to the 'releases' page or view other releases.
  - When adding a release, a dynamic 'reviews' tab is created for each release. On the 'reviews' tab, multiple users can review the release and view other reviews. The average rating of reviews is displayed on the 'releases' tab for each release.
  - If the user is not logged in, they can view added releases and reviews but cannot add their own releases or reviews.
  
* Progress of the application in the last two weeks:
  - The user interface has been improved with the 'layout.html' file, which is extended with the Jinja library.
  - A list of releases on the 'releases' page has been implemented, which is retrieved from the database, along with the 'add release' functionality. Dynamic 'reviews' tabs have been implemented, along with a list of reviews and 'add review' functionality.
  - The SQL schema has been changed to 'users, artists, releases, reviews'
  - The application is in production on fly.io server

* Improvements needed:
  - The 'Artists' tab should display the number of releases by the artist and the average rating of all releases. (Currently, the page only displays an empty list)
  - On the 'Reviews' page, the user ID should be replaced with the username.
  - Ensure functionality and minimize errors.
  - Enhance security (e.g. CSRF token).
  - If time allows, create a search function for the 'Releases' page and an admin user type that can delete releases or reviews.

 * __Summary: The application is in good shape but requires some fine-tuning.__