# ReviewMusic

This application allows users to review music on their internet browser. The application has been developed for the 'Database Application Project' -course as a part of my bachelor's degree in University of Helsinki.

Link to the application: https://tsoha-reviewmusic.fly.dev/

__First time connecting to the database while using the app, an internal server error might occur. If this is the case, just refresh the page and the application starts working.__

## Application requirements:
* Users can create a new account, login, and logout.
* Users can view reviews of songs and albums created by other users. Users can also view a page for a single artist that shows all of their work's reviews.
* The review page displays the average rating of all reviews, individual reviews, and information about the work (title, genre, release year).
* Users can search for works by keyword.
* Users can filter works by genre.
* Users can create a new work to be reviewed and rate it (stars and comments) if no reviews have been created for it yet. Alternatively, users can also add a new review for an existing work.
* Administrators can add and remove works or individual reviews as needed.

## Report 2 ('Välipalautus'):
* The application's user interface is in a good stage: Home page (including login), Registration page, Menu
* The SQL schema has been defined
* Login function has been implemented, although not fully functional yet
* Unfortunately, I have not been able to connect to the database, so logging in does not work in practice. It may be due to using a MacBook instead of the recommended computer. (Postgres.app has been installed and seems to be working)
* My first commit to GitHub was far too large, I committed several days of coding work at once. In the future, I will try to make commits as often as possible.

## Report 3 ('Välipalautus'):
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
