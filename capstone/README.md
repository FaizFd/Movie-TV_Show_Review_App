Distinctiveness and Complexity:
This project satisfies the distinctiveness and complexity as it has all the concepts thought is this course. It is a multiple page web application that utilizes Django, JavaScript, HTML and CSS. This project is a IMDB like website where users can look up their favourite movies/TV shows and find information relating to them like posters, synopsis, trailer, cast, my rating and IMDB’s rating. Users can also add Movies/TV Shows to their watch list. Users can post their reviews. Users can also find where the movie/tv show is available to watch. The project was built using Django as a backend framework and JavaScript as a frontend programming language.  All generated information are saved in database (SQLite by default).All WebPages of the project are mobile-responsive.
Requirements: 
•	Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
•	 Create superuser with python manage.py createsuperuser. This step is optional
•	Go to website address and register an account.
Files and Directories: 
•	capstone
o	static/capstone: Contains all static content.
	styles.css: contains compiled CSS files
o	templates/capstone: 
	cartpage.html: If user is signed in, shows the content they add to their watch list. If not says “No content found in your watchlist.” 
	category.html: Shows the genre of the movie/tv show.
	categorys.html: Search by only movies or only tv shows.(extends after clicking categpages.html)
	categoryss.html: Search by year of release. (extends after clicking categpagess.html)
	categpage.html: Contains all the genres available in this website you can search by.  
	categpages.html: Search by only movies or only tv shows.
	categpagess.html: Search by year of release.
	create.html: Form that creates listing of all movies and tv shows available in this project. (this is a front end form and users can also create their own listing)
	 index.html: This the index page of this project. It has an image carousel that shows all the trending movies/tv shows. It also has all the movies/tv shows in this website with a pagination count of 10 listings.
	layout.html: It contains the layout of this project which is similar for all the pages. It has a mobile responsive top navigation bar and a search bar.
	listingpage.html: This is the listingpage of a movie/tv show. This contains all the information about the movie/tv show.
	login.html: This is the login page of the website.
	register.html: If the user does not have an account they can make one here.
	search.html: This shows the search results.
o	admin.py: Here I added some admin classes and re-registered User model.
o	models.py: Contains all the models I added in this project.
o	urls.py: Contains all the application’s URLs.
o	views.py: Contains all of the application views.
