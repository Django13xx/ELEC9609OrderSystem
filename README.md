# HotpotOrderingSystem
Copy of my code of Hos from Group2 of ELEC9609 that I finished in 2023 S2 during the study at USYD


---------------------------------------------------------------------------------------------------------

# ELEC9609-Group2
## Project Name

Hotpot Ordering System(Hos)

## Project Description

We are developing a Hotpot Ordering System.<br />
It encompasses a auto dish function: Automatically generate menus based on customer needs.<br />
Two parts are included:
1. Ordering System for customers （encompass the AI menu system）
2. Management System for Administrator (table and menu management)

## Porject Details ##

### Backend-Django
    *django
    *django rest framework
    *django cors headers

### Frontend-Vue
    *vue3
    *bootstrap
    *fontawesome

**Structure**

### Main File Structure and Distribution
- GROUP-2:
    - **Hos**
        - *backend*
            - backend
                - settings.py
                - urls.py
            - hos
                - models.py
                - management
                    - commands
                - views.py
            - Static
                - images
                - menu.csv
                - staffDetail.csv
                - table.csv
            - .env *(openai AI API key, please do not copy or use it for any other usage!)*
            - manage.py
            - db.sqlite3
        - *Frontend*
            - public
                - index.html
            - src
                - components
                - pages
                - router
                - App.vue
                - main.js
        - readme.md *(developing history)*
- README.md


## Features

For customers:
1. Customers and administrators can log in to and log out of the website.
2. Customers can view all the items in the menu.
3. Customers can view the total cost in the shopping cart.
4. Customers can view the items they have been selected in the shopping cart.
5. Customers can add new items into cart or remove current items.
6. Customers can check out when they finish ordering.
7. Customers can change the amount of items in the shopping cart.
8. Customers can choose pay for cash or card.
9. Customers can interact with the AI customer service.

For administrators:
1. Administrators can view all the items for sale.
2. Administrators can add new items or remove current items in the menu.
3. Administrators can update the prices and stock of the items.
4. Administrators can free or occupy a table.
5. Administrators can view the total turnover in one day.
6. Administrators can view the number of item that already sold in one day.

Other Functionality
1. Compulsory items need to be chosen before checking out.
2. Some of the items have limited amount for ordering.
3. Customers prefer sorting the items by category.
4. Administrator can view if customers sit and order at the table.
5. An auto-generated menu will be displayed to the customers after they choose their preferences.

## Installation

### Please redirct to the application path: `GROUP-2/Hos` first, and then carefully follow the steps below:

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   
2. Install the project dependencies:
   ```bash
   pip install -r requirements.txt

### For the following steps, you need two seperate terminal windows for backend and frontend respectively

#### In terminal ONE
3. redirect to the Backend
   ```bash
   cd backend

4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Run database initilazition:
   ```bash
   python manage.py initialDb
   python manage.py deleteHistory
   
6. Start the development server:
   ```bash
   python manage.py runserver

#### In terminal TWO
7. redirect to the Frontend
   ```bash
   cd frontend

8. Start the Vue3 server:
   ```bash
   npm run serve

## Configuration

1. You can configure the project by editing the settings.py file in .Hos/backend/backend folder.
2. Make sure to set the required environment variables for secret keys and API keys.

## Usage

### You can use the system once you finished the above steps
### Open the Hotpot Ordering System (frontend) at http://localhost:8080/
####   If you want to enter the Admin Mode,
####   log in as an example staff as
####   id:         723
####   password:   123456
### Check the backend at http://localhost:8000/ 

## Notice

### Please do NOT copy or use the Open AI API in the .env file for any purpose !!!!

## Issue: Unable to run Vue CLI Service ("vue-cli-service" not recognized)

When trying to run the Vue CLI Service using the command npm run serve, you may encounter the following error:

    ```bash
    'vue-cli-service' is not recognized as an internal or external command, operable program or batch file.
This issue usually occurs when the system cannot locate the "vue-cli-service" command.

### Solution:

### To resolve this issue, follow these steps (please add `sudo` before each commands for Linux):

1. Clear npm Cache:
Sometimes, issues in the npm cache can cause problems during installation and command execution. Clear the npm cache by running the following command:
    ```bash
    npm cache clean -f

2. Uninstall Vue CLI:
Uninstall Vue CLI using the following command:
    ```bash
    npm uninstall -g @vue/cli
    
3. Install Vue CLI Using Yarn:
Try installing Vue CLI using Yarn, as it may be more effective in resolving dependency issues:
    ```bash
    yarn global add @vue/cli

4. Update npm:
Make sure your npm is up to date by running the following command:
    ```bash
    #Skip this line if you have yarn installed
    npm install -g yarn
    #Install npm again
    npm install -g npm


5. Check Project Dependencies:
Ensure that the dependencies for your Vue project are correctly installed. Navigate to your project's root directory and run the following command:
    ```bash
    npm install

#### After completing these steps, you should be able to run npm run serve without encountering the error. If the problem persists, please provide detailed error information for further assistance.

# GROUP-2 29/10/2023 #
