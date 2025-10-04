# Crowdfunding Back End
{{ Trang Vo }}

## Planning:
### Concept/Name
- Name: Helping hands
- Concept: The app is a crowdfunding platform specifically for support toward local elderly people.
  The "Helping hands" campaign is the featured or launch campaign, but other users can create their own fundraisers.

### Intended Audience/User Stories
The intended audience of this app are divided into three key segments: project creators, donors, and the broader Community.

### Front End Pages/Functionality
- Homepage: Featured Fundraisers
    - Hero section with call to action
    - Featured fundraisers with progress bars and donation buttons
    - Overview of the platform's mission and impact

- All Fundraisers Page 
    - A list of all available Fundraisers
    - Filter options by tasks (e.g.)
    - Ability to sort projects by funding progress or creation date

- Create New Fundraiser Page
    - Form with campaign details (name, species, description, goal) 
    - Ability to submit new campaign details to the database
    - User validation to ensure all fields are filled correctly

- A Specific  Fundraiser Details Page 
    - etailed information about a single fundraiser
    - Shows progress towards the fundraising goal 
    - Option to make a donation
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