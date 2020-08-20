# Coffeebook

The aim of the website is to provide users with information on how to prepare hot an cold coffee drinks,allow visitors to add they own recipes.

## Demo

Live demo can be found [here](https://coffeebookci3.herokuapp.com/).
![](https://github.com/misza80/CI_Project3/blob/master/static/assets/images/coffeebook.png)

## UX

### User stories

As a user, I want to be able to add my own recipes to the database. (Create)\
As a user, I want to browse a large collection of coffee recipes. (Read)\
As a user, I want to be able to edit recipes. (Update)\
As a user, I want to be able to delete recipes. (Delete)

### Strategy

My goal in the design was to create a simple,easy to navigate website with a color neutral scheme.
This Data Driven Web-application was built to share recipes with other coffee lovers.
### Structure


### Skeleton
[Landing wireframe](https://github.com/misza80/CI_Project3/blob/master/static/assets/wireframes/mainpage.png) \
[List of recipes wireframe](https://github.com/misza80/CI_Project3/blob/master/static/assets/wireframes/listofrecipes.png) \
[Single recipe wireframe](https://github.com/misza80/CI_Project3/blob/master/static/assets/wireframes/singlerecipe.png) 

### Surface

The typogragphy was found on google fonts and I chose the font Pacifico for headers as it has a fun handwriting look.
 

Colours used are different shades of brown, which corresponds with the color of coffee bean.

## Technologies

1.HTML\
2.CSS\
3.Materialize\
4.JavaScript\
5.jQuery\
6.Flask\
7.Google Chrome Developer tools.\
8.Mongo DB

## Features

This site uses collapsible navbar to manage the navigation list on smaller screens.
Content is dynamically rewritten allowing for faster transitions between the subpages.
In responses to users actions content is added to the page as necessary.
User can select categories of tutorials by using a dropdown menu that will filter the content.

In the future I would like to move the cards content to JSON file.Also add pages for each category in the categories section of the site.
I would like update the information on the website on a regular basis with new articles and videos .I would also like to add a ability to comment on articles to allow for more user interaction.

## Testing


#### Errors



## Deployment

This site is hosted using Heroku, deployed directly from the Github master branch. The deployed site will update automatically upon new commits to the master branch.
In order to setup github pages I did the following:

- **Created a new repository:**
  From the main page I clicked on "New repository" button,gave it a name and clicked "Create a repository" button.


- **VS Code Setup:**
  For writing code I've used VisualStudio Code (VS Code).
  To get VS Code working correctly with GitHub,you need to install latest version of Git first,after that you can install VS Code.
  When installation finished I have cloned my repository,first by copying to clipboard the link to repository from the github page and then pasting it after `git clone` command into VS Code terminal.
  After selecting the save folder, proceeded to creating files and folders for my project.
  From the source control tab I could stage and commit changes to the repository.
  After entering the commit message I was able to push the committed changes.
  
This project was then deployed to Heroku to host the live application, following the steps below:

1.Log in to Heroku and create a new app called 'coffeebookci3'\
2.Log in to Heroku in the CLI\
3.Add the remote Heroku repo\
4.Create the requirements.txt file by running pip3 freeze --local > requirements.txt in the CLI\
5.Create a Procfile by running echo web: python run.py > Procfile in the CLI\
6.Start a web process on Heroku by running heroku ps:scale web=1 in the CLI\
7.Set environment variables in Heroku for IP, PORT,SECRET_KEY and MONGO_URI\
Restart all dynos on Heroku

## Credits



### Content



### Media



### Acknowledgements

Wireframes were made using www.draw.io

Favicon were made using www.favicon.io

**This is for educational use.**
