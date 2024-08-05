# Project Overview:

A national car dealership with local branches spread across the United States recently conducted a market survey. One of the suggestions that emerged from the survey was that customers would find it beneficial if they could access a central database of dealership reviews across the country.

This project allows new and existing customers to look up different branches by state and look at customer reviews of the various branches. Customers should be able to create an account and add their review for any of the branches. The management hopes this will bring transparency to the system and also increase the trust customers have in the dealership.

After thorough research and brainstorming, the team developed use cases for anonymous, authorized, and admin users.

## Use cases for anonymous users:
	1.View the Contact Us page.
	2.View the About Us page.
	3.View the list of dealerships.
	4.Filter the list of dealerships by state:
	5.Select Show all or a specific state from the State dropdown on the dealership page.
	6.View all states if nothing is selected in the dropdown.
	7.View a table of dealerships for the selected state when the form is submitted.
	8.Click on a dealership to view the reviews for that dealership on the details page with each review displayed on a bootstrap card.
	9.Log in using their credentials.

## Use cases for authorized users:
	In addition to the above, authorized users should be able to write a review for any dealership on the dealership's page. In order to enable authorized users to write their reviews:
	1.A Review button should be provided against each dealer listed in the dealership table.
	2.Clicking on the Review button should take the user to the review page.
	3.Filling the form on the review page and submitting it should add the review.
	4.On submission, the user should be taken back to the dealership detail page with the submitted review featured at the top of the reviews list, sorted on time.

## Use cases for admin users:
	1.Log in to the admin site with a predefined username and password.
	2.Add new make, model, and other attributes.

# Project Description

## Add user management to the Django application.

	1.Implement user management using the Django user authentication system and create a REACT frontend.

## Implement backend services.

	1.Create Node.js server to manage dealers and reviews using MongoDB and dockerize it.
	2.Deploy sentiment analyzer on Code Engine.
	3.Create Django models and views to manage car model and car make.
	4.Create Django proxy services and views to integrate dealers and reviews together.

## Add dynamic pages with Django templates.

	1.Create a page that displays all the dealers.
	2.Create a page that displays reviews for a selected dealer.
	3.Create a page that lets the end user add a review for a selected dealer.

## Implement CI/CD, and then run and test your application

	1.Set up continuous integration and delivery for code linting.
	2.Run your application on Cloud IDE.
	3.Test the updated application locally.
	4.Deploy the application on Kubernetes.

## Solution Architecture:
The solution will consist of multiple technologies:

	1.The user interacts with the "Dealerships Website", a Django website, through a web browser.
	2.The Django application provides the following microservices for the end user:
	        get_cars/ - To get the list of cars from
		get_dealers/ - To get the list of dealers
		get_dealers/:state - To get dealers by state
		dealer/:id - To get dealer by id
		review/dealer/:id - To get reviews specific to a dealer
		add_review/ - To post review about a dealer
	3.The Django application uses SQLite database to store the **Car Make** and the **Car Model** data.
	4.The "Dealerships and Reviews Service" is an Express Mongo service running in a Docker container. It provides the following services:
		/fetchDealers - To fetch the dealers
		/fetchDealer/:id - To fetch the dealer by id
		fetchReviews - To fetch all the reviews
		fetchReview/dealer/:id - To fetch reviews for a dealer by id
		/insertReview - To insert a review
	5."Dealerships Website" interacts with the "Dealership and Reviews Service" through the "Django Proxy Service" contained within the Django Application.	
	6.The "Sentiment Analyzer Service" is deployed on IBM Cloud Code Engine, it provides the following service:	
		/analyze/:text - To analyze the sentiment of the text passed. It returns positive, negative or neutral.
	7.The "Dealerships Website" consumes the "Sentiment Analyzer Service" to analyze the sentiments of the reviews through the Django Proxy contained within the Django application.

 ![image](https://github.com/user-attachments/assets/02e376c4-02aa-4bff-be8c-04d26ac9dbb4)

