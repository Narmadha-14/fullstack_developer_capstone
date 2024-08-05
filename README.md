# Project Description

A national car dealership with local branches spread across the United States recently conducted a market survey. One of the suggestions that emerged from the survey was that customers would find it beneficial if they could access a central database of dealership reviews across the country.

You are a new hire at the company. You are assigned the task of building a website that allows new and existing customers to look up different branches by state and look at customer reviews of the various branches. Customers should be able to create an account and add their review for any of the branches. The management hopes this will bring transparency to the system and also increase the trust customers have in the dealership.

After thorough research and brainstorming, the team developed use cases for anonymous, authorized, and admin users.

## Add user management to the Django application.

-->Implement user management using the Django user authentication system and create a REACT frontend.

## Implement backend services.

-->Create Node.js server to manage dealers and reviews using MongoDB and dockerize it.
-->Deploy sentiment analyzer on Code Engine.
-->Create Django models and views to manage car model and car make.
-->Create Django proxy services and views to integrate dealers and reviews together.

## Add dynamic pages with Django templates.

-->Create a page that displays all the dealers.
-->Create a page that displays reviews for a selected dealer.
-->Create a page that lets the end user add a review for a selected dealer.

## Implement CI/CD, and then run and test your application

-->Set up continuous integration and delivery for code linting.
-->Run your application on Cloud IDE.
-->Test the updated application locally.
-->Deploy the application on Kubernetes.

## Solution Architecture:
The solution will consist of multiple technologies

1.The user interacts with the "Dealerships Website", a Django website, through a web browser.

2.The Django application provides the following microservices for the end user:

3.get_cars/ - To get the list of cars from
	get_dealers/ - To get the list of dealers
	get_dealers/:state - To get dealers by state
	dealer/:id - To get dealer by id
	review/dealer/:id - To get reviews specific to a dealer
	add_review/ - To post review about a dealer
	The Django application uses SQLite database to store the Car Make and the Car Model data.

The "Dealerships and Reviews Service" is an Express Mongo service running in a Docker container. It provides the following services::

/fetchDealers - To fetch the dealers
/fetchDealer/:id - To fetch the dealer by id
fetchReviews - To fetch all the reviews
fetchReview/dealer/:id - To fetch reviews for a dealer by id
/insertReview - To insert a review
"Dealerships Website" interacts with the "Dealership and Reviews Service" through the "Django Proxy Service" contained within the Django Application.

The "Sentiment Analyzer Service" is deployed on IBM Cloud Code Engine, it provides the following service:

/analyze/:text - To analyze the sentiment of the text passed. It returns positive, negative or neutral.
The "Dealerships Website" consumes the "Sentiment Analyzer Service" to analyze the sentiments of the reviews through the Django Proxy contained within the Django application.
