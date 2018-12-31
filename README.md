[![Build Status](https://travis-ci.org/PhilSurgenor/milestone5.svg?branch=master)](https://travis-ci.org/PhilSurgenor/milestone5)

Phil Surgenor - Milestone Project 5
===

<br>

## Fullstack Development
[visit the project website here](https://ua-issue-tracker.herokuapp.com/)

My task for this project was to build a ticketing app and tracked and displayed issues pertaining to an app called the Unicorn Attractor.

There were key features that needed to be added to fulfil the brief. These were as follows:

There were to be two types of ticket, a bug report and a feature suggestion.

The bug report should allow the user to describe the issue, comment on the ticket, upvote the bug to make it more of a piority. It should also indicate its status, wether fixed, being fixed to still to do.

The feature suggestion should allow the same, but to upvote a feature some sort of payment had to be made. Instead of make the user pay everytime they wanted to upvote a feature, I decided to sell tokens or UniCoins as they are called on the site. You can buy the coins in 5s 10s and 15s. It costs 1 coin per upvote and allows the user to upvote multiple times without having to go through the payment process every time they wanted to upvote a feature.

Another part of the site was to show charts of how many bugs and features were completed each day month and year.

As the site has developed, I believe it serves the purpose very well. There is a social side to it as you can comment of the tickets, these comments display username and date created. This helps bring a sense of comunity to the site.

I have registered a user as staff to allow you to get access to the admin section and so you can preform tasks like change tickets to fixed etc. The username is: staff-user and the password is: unicornpass

<br>

## UX

To make this project a success, I had to think very hard about how potential users might, navigate and interact with all that was required.

I start out with a site map to give me an idea of how each feature and page would sit along side each other.

Once I had an initial concept in my head I started to lay out some wireframes (there are two files, SiteStructure.pdf and wireframes.pdf above) using Balsamiq Mockups. These gave me a very good indication of how each part of the UI would sit within the browser.

A key part of the app was the ability to upvote bugs and features, as with most modern sites upvotes and likes are done using ajax. I decided to use the same method, so there was no need for a page refresh which would be detrimental to the user experience.


<br>

## Technologies

#### Frontend
HTML5

CSS3

Bootstrap 4

jQuery

chart.js

Bootswatch Theme (Lumen)




#### Backend

Django 1.11

Python

PostgresQL Database

AWS

Travis Continuous Intergration


<br>


## Testing

Most of the testing for this app was done manually. I find as I start building I am constantly testing each feature and intentionally trying to find fault or break the app. I find this a very effective way to test. 

I took each app and made sure all the functionally worked as it should. There were times when things didn't work like they were supposed to and I had to figure out how to fix them.

I found the debugger tool within Djanog to be extremly helpful. I like the way it traces back each step until it get to the part that was broken.


I thoroughly tested the login and registration, the adding tickets, upvoting, payments, adding tokens and using them to 'buy' upvotes. 

Another great piece of software that I used was Travis CI. As I started to build and make the app more complicated, Travis was able to be a reassurance that the build was succeeding.

Another thing that helped with testing was I very early deployed to Heroku. Thsi meant as I tested the site and push the files to GitHub and Heroku, I got near instant feedback if something in the build had gone wrong. This meant I could sort one or two problems out, instead of leaving it until the end when ther could have been even more issues.


<br>

### Deployment

As I mentioned above I deployed quite early on in the process of making the app. There was a number of things I had to do to get the app up and running on Heroku. I decided to host a PostgresQl Database with Heroku to keep all the data for the app. I also decided to use Amazon Web Services S3 Bucket to hold all my static files, these included css and js. Along with these where all the images for the site.

When I was testing and building the site, I kept the static files local, so I didn't have to upload the CSS for example everytime I made a change.

Also when in the development stage, I used an environment file to house secret keys and passwords, this file was on the .gitignore file so it would get into the public space. These environment variables where then transferred to Heroku and saved in the Config Vars section of thier website.

I created a requirements.txt file with all the django packages that I was using to that Heroku could use the same settings. I also need to create a Procfile so that Heroku could run the app properly.

After all this was complete I tested the site again to make sure everything was still working as it should.

<br>

### Credits

As mentioned above, I used a bootswatch theme, Lumen, to help with the styling and look of the site. Some of the pictures of unicors where taken from google images. The phones used in the pictures were a free download on Photoshop.
