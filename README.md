# Crowdfunding Back End
    "Helping hands" by Trang Vo - SheCodes 2025 cohort

## Planning:
### Concept/Name
- Name: Helping hands
- Concept: The app is a crowdfunding platform specifically for support toward local elderly people.
  The "Helping hands" campaign is the featured or launch campaign, but other users can create their own fundraisers.

### Intended Audience/User Stories
The intended audience of this app are: elderly/local communities seeking help around the house (fundraising), local volunteers with skills to help out (pledging).

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

| URL         |Purpose                              | HTTP Method | Request Body    | Success Response Code | Authentication/Authorisation |
| ---         | -----------                         | -------     | ------------    | --------------------- | ---------------------------- |
| /users/     | Create a new user                   | POST        | JSON payload #{fundraiser_id"}|201      | Any logged in users          |
| /users/     | Fetch one user                      | GET         | N/A             |              200      | None                         |
| /users/     | Update one user                     | PUT         | JSON Payload    |              201      | Any logged in users          |
| /users/     | Fetch all users                     | GET         | N/A             |              200      |                              |
|/api-token-auth/| Get user's token                 | POST        | JSON payload #{fundraiser_id"}|201      | Any logged in users          |
|/fundraisers/| Create a new fundraiser             | POST        | JSON Payload    |              201      | Any logged in users          |         
|/fundraisers/| Fetch one fundraiser                | GET         | N/A             |              200      | None                         |
|/fundraisers/| Update one fundraiser               | GET         | N/A             |              200      | None                         |
|/fundraisers/| Fetch all fundraisers               | GET         | N/A             |              200      |                              |
| /pledges/   | Create a new pledge for a fundraiser| POST        | JSON payload #{fundraiser_id"}|201      | Any logged in users          |
| /pledges/   | Fetch one pledge                    | GET         | N/A             |              200      | None                         |
| /pledges/   | Update one pledge                   | POST        | JSON Payload    |              201      | Any logged in users          |
| /pledges/   | Fetch all pledges                   | GET         | N/A             |              200      |                              |

### DB Schema
![](  ./database.drawio.svg)

## Project Requirements
Your crowdfunding project must:

- [x] Be separated into two distinct projects: an API built using the Django Rest Framework and a website built using React. 
- [ ] Have a cool name, bonus points if it includes a pun and/or missing vowels. See https://namelix.com/ for inspiration. <sup><sup>(Bonus Points are meaningless)</sup></sup>
- [x] Have a clear target audience.
- [x] Have user accounts. A user should have at least the following attributes:
  - [x] Username
  - [x] Email address
  - [x] Password
- [x] Ability to create a “fundraiser” to be crowdfunded which will include at least the following attributes:
  - [x] Title
  - [x] Owner (a user)
  - [x] Description
  - [x] Image
  - [x] Target amount to raise
  - [x] Whether it is currently open to accepting new supporters or not
  - [x] When the fundraiser was created
- [x] Ability to “pledge” to a fundraiser. A pledge should include at least the following attributes:
  - [x] An amount
  - [x] The fundraiser the pledge is for
  - [x] The supporter/user (i.e. who created the pledge)
  - [x] Whether the pledge is anonymous or not
  - [x] A comment to go along with the pledge
- [ ] Implement suitable update/delete functionality, e.g. should a fundraiser owner be allowed to update its description?
- [ ] Implement suitable permissions, e.g. who is allowed to delete a pledge?
- [ ] Return the relevant status codes for both successful and unsuccessful requests to the API.
- [ ] Handle failed requests gracefully (e.g. you should have a custom 404 page rather than the default error page).
- [ ] Use Token Authentication, including an endpoint to obtain a token along with the current user's details.
- [ ] Implement responsive design.

Please include the following in your readme doc:
- [x] A link to the deployed project - https://crowdfunding-backend-trangvo-7661bbaf5a0b.herokuapp.com/fundraisers/
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Step by step instructions for how to register a new user and create a new fundraiser (i.e. endpoints and body data).
- [ ] Your refined API specification and Database Schema - ![](./database.drawio.svg)
