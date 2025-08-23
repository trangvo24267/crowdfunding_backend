# Crowdfunding Back End
{{ your name here }}

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality
- Home Page
    - Featured kickstarters
- Search page
    - Search specific fundraiser
-Create New Fundraiser Page
    - Form with fundraiser details
    - Ability to submit
    - Nice error pages for validation

- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}
- Display Fundraiser
    - Shows all information about fundraiser
    - Show all pledges made so far
### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
| /fundraisers| Fetch all the fundraisers    | GET     |   N/A        |              200      |     None                     |
| /fundraisers| Create a new fundraiser      | POST    | JSON Payload |              201      |   Any logged in users        |
| /pledges/   | Fetch all the pledges        | GET     | N/A          |              200      |                              |
| /pledges/   | Create a new pledge for a fundraiser| POST     | JSON payload #{fundraiser_id"}|201| Any logged in users |



### DB Schema
![](  ./database.drawio.svg  )

Your name
Your concept
Your audience
Some of the front end pages/functionality that we know of so far
The "API Spec" table with the 3 "endpoints" (I'll speak more to what we mean by API and endpoints in class on saturday)
See in the :thread: with my partially completed README as a reference. I've filled in the first 2 lines of the API Spec, you complete the 3rd
Ignore the DB schema bit, we'll talk about that later