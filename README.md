# Learn2Learn

## Purpose of this site

This site has been created so that users can share and seek information about education choices.   
Registered users can create, edit and delete their own posts and share their experiences with various educations. They can also comment and like other people's posts.

![am i responsive](/documentation/testing/location_responsive.png)

### User Stories


I used Github Issues to record the following user stories:
 
- Manage posts - As a site admin I can create, read, update and delete posts so that I can manage the content on the site
- Pagination - As a site user I can view a paginated list of posts so that I can easily select a post to view.
- Account registration - As a site user I can register an account so that I can comment and like posts
- Landing page - As a site user I can go to the landing page so that I can see the purpose of the website
- Account registration - As a site user I can register an account so that I can comment and like posts
- Read content - As a site user / admin I can view the content and comments on an individual post so that I can read the comments and content on the page
- Create a post - As a site user I can create a new post so that I can share education tips with other users
- Update posts - As a site user I can edit my posts so that I can update or correct information
- Delete posts - As a site user I can delete my posts so that I can remove them from the website
- Create a post - As a signed in user I can create a new post so that I can share locations with other users.
- Comment on a post - As a site user I can leave a comment on a post so that I can interact with the content
- Delete posts - As a signed in user I can delete my posts so that I can remove them from the website.
- View likes - As a site user/admin I can view the number of likes on each post so that I can see which is most popular
- Like/unlike - As a site user I can like or unlike a post so that I can interact with the content

### Agile Development Tool

During this project, I have used Agile software development tool and thus used Kanban Template to create the project for this website.
As I start working on each issue I move it to the 'In progress' column.  When the coding for each issue has been completed, the issue is then moved to the 'done' column.

![my kanban board](/media/images/kanban.png)


### Data Model

I needed two data models to make this website work. The first data model is the Post. This contains the information for the post. I have a second data model for the comments which are linked to a post.

#### Location post model

| Key | Name | Type
|-----|----------------|------------------|
| | title (unique) | Char(200)
| foreign key | author | User Model
| | created_date | DateTime
| | content | TextField
| | featured_image | Cloudinary_image
| | excerpt | TextField
| many-to-many | likes | User Model
| label for url | slug (unique) | slugfield

#### Comment model

| Key | Name | Type
|--------|----------------|-------------------|
|foreign key | post | Post Model
| | name | Char(80)
| | body | TextField
| | created_on | DateTime

### Features

A short introduction to my site. 
Since my page crashed an hour before submit and I haven't had time to solve it in such a short time, I'm submitting this as I have it.

![my kanban board](/media/images/nav-bar.png)
![my kanban board](/media/images/main-site.png)
![my kanban board](/media/images/footer.png)
![my kanban board](/media/images/register.png)
![my kanban board](/media/images/add-post.png)
![my kanban board](/media/images/error.png)

### Deploy
- Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually.
- Click View to view the deployed site.

## Credits
- I used 'I think therefore I blog' to set up files, Heroku app, Cloudinary, environmental variables and GitHub Projects.
- Credits goes to Dennis Ivy on Youtube for the help with alot of codes on the site. 
- I used GitHub Projects and Kanban for user stories like 'I think therefore I blog'
- I used card system from 'I think therefore I blog' for displaying posts.
- I used the messages from 'I think therefore I blog'
- I used colors from: https://color-hex.org/
- I used bootstrap links from 'I think therefore I blog'.
- I used the images from: https://www.pexels.com/


## Acknowledgements
Learn2Learn was completed as a Porfolio 4 Project for the Full Stack Software Developer education at the Code Institute. I would like to thank the Slack Community and Code Institute for the help and support during this project. A better version is comming in the future with a lots of fun stuff on the page!