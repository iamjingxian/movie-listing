#### movie-listing
simple webpage showing movie listings, created using django

instructions to load django from command prompt

```
# load django from command prompt
activate django conda activate django
load server with python3 manage.py runserver 8080
```

load webpage http://127.0.0.1:8080/about-us/

backend UI
* used a html5 color and logo formatting that looks like Netflix: Black BG, Red logo,

database
* defined a django model class called Movie
* defined characters fields relevant for this webpage: Movietitle, advisory rating, poster image url, movie duration and the url link to buy the ticket
* model is also used to create a Django Model Form in the template HTML file that you can see in this webpage’s fields etc.. (scroll to form fields)

add/delete/buy a movie
* To add: After populating form, when user clicks 'submit', it will add a new movie to the database and the webpage will be updated as you can see here (click submit!)
* To delete: made a dropdown list that loops through the database and populates the list. This is user-friendly as it ensures that the user deletes a movie that exists in the database. (no margin for error) Upon clicking 'delete' the movie is removed from the database and therefore not rendered in the page and removed from the dropdown list.
* To buy: To buy the ticket, the user would click the link below the poster, and it will redirect user to the theater webpage.
* Every button in this webpage is named, so that when the user click on any of them the function knows what the user wants to do. Otherwise, to the program this is just a “POST” or “submit” action.

ideas for improvement 
* Write a webscraping python script, so that user can submit a url to a movie and the rest of the fields in the database can be populated automatically
* when clicking on “buy ticket”, it opens a new tab so that our webpage is still in the user’s browser.
* For convenience and to prolong the time they spend on the webpage. (Has to be done with javascript to control the browser. Django only runs the webpage server and response, it does not control the browser behaviour)
