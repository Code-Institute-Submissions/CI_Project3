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
4.jQuery\
5.Flask\
6.Google Chrome Developer tools \
7.Mongo DB \
8.Heroku

## Features

This site uses collapsible navbar to manage the navigation list on smaller screens.
Users can: 
- See all recipes overview (cards)
- Select to display only single category of recipes.
- Add a recipe.
- Edit recipes.
- Remove a recipe.


In the future I would like to add user registration and login as well as a user dashboard,so users can manage their recipes better. 

## Testing
I tested this project manually. \
Aim of the test was to verify that the webiste works correctly across different operating systems,browsers and devices.
Website was tested on Google Chrome,Firefox and Opera browsers in their latest versions.Website was tested on multiple mobile device (iPhone 5,6,XR Samsung Galaxy s5,Apple Ipad) to ensure compatibility and responsivness.
Chrome developer tools were also used to check for compatibility and responsiveness.
Collapsible navbar works correctly on mobile devices. 
Code was validated using W3C, JsHint and PEP8 online validation services.All links were tested manually and will open within same browser tab.I used a lot of console.log() to see if my code us running correctly.
#### Errors

No errors were found in the final deployment.

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


### Content

Images for recipes were obtained from Google Images.


### Media
Backround by  <a href="https://unsplash.com/@nordwood?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">NordWood Themes</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span> \
Carousel photos by: \
<a href="https://unsplash.com/@prestongoff?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Preston Goff</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a> \
<a href="https://unsplash.com/@gtk1x?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Gerson Cifuentes</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a> \
<a href="https://unsplash.com/@nadyeldems?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Dan Smedley</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a> \
<a href="https://unsplash.com/@kcatimmer?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Kenny Timmer</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a>

### Acknowledgements

Wireframes were made using www.wireframe.cc
 

**This is for educational use.**
