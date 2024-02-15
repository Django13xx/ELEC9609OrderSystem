# Renjie Yao 16:54 03/10/2023 #

## Quick Run ##

open terminal in `HOS\backend` and run
    - python manage.py runserver
open terminal in `HOS\frontend` and run
    - npm run serve




## Details ##

# Backend-Django
    *django
    *django rest framework
    *django cors headers

# Frontend-Vue
    *vue
    *bootstrap
    *fontawesome

**Structure**
The original file structure
                            Hos
                            --> backend
                                ->> backend
                                    >>> settings.py
                                    >>> urls.py
                                ->> hos
                                    >>> models.py
                                    >>> views.py
                                ->> Static
                                    >>> Menu.csv
                                ->> manage.py
                            --> Frontend
                                ->> public
                                    >>> index.html
                                ->> src
                                    >>> components
                                    >>> App.vue
                                    >>> main.js
                            --> readme.md

**Steps**
--Backend
    `1.install django`
        - pip install django
    `2.create backend project`
        - python -m django startproject backend
        - python manage.py migrate
    `3.create Hos Model`
        - python -m django startapp hos
        * create the model menu in the backend\models.py
        in the HOS\backend
        - python manage.py makemigrations
        - python manage.py migrate
        * add data
            create in hos\management\commands
                importMenu.py
            add in HOS\backend\Static
                Menu.csv
            run in HOS\backend
                python manage.py importMenu
    `4.use restframework to add serializer viewset and urls`
        add in backend\hos
            serializers.py
        add in settings\INSTALLED_APPS[]
            'rest_framework',
        modify in backend\hos
            views.py (add MenuViewSet)
        modify in backend\backend
            urls.py (add router and register MenuViewSet)
--Frontend
    `1.install node and vue`
        search and install node and vue
    `2.vue-clil create frontend project`
            install cli
            - npm install @vue/cli -g
            (install after you can see 
            - vue -V 
            - npm -v)
        in windows terminal at path Hos
        - vue create frontend
        in frontend try
            - npm run serve
        if works then success
    `3.modify index.html main page, add bootstrap css frameworkand fontawsome font dependency`
        pay attention to these 3 files:
        public\index.html
        frontend\App.vue
        all the .vue in src\omponents
        add bootstrap 4, visit the following web page
            https://v4.bootcss.com/
        modify the public\index.html
        add fontawesome before <title> in the index.html from web:
            https://www.runoob.com/font-awesome/fontawesome-tutorial.html
    `4.modify App.vue and core components`   
        modified
            index.html
            HelloWorld.vue --> ContainerMenu.vue
            App.vue
    `5.add axios http request component`
        npm install axios --save
        in the script of ContainerMenu.vue
            import axios from 'axios'       
    `6.add request backend(BE) code`
        use axios and corresponding mounted to get menu from BE
        Achieved all the CRUD in the frontend by
        editMenu()
        deleteMenu()
        SaveMenu()
        And remember set dish_pic to blank = true and null = true for quick updating needs
        remember to set the mounted for getAll()

# Renjie Yao 16:54 03/10/2023 #


**Development History**

# Renjie Yao 12:23 04/10/2023 #

`initial staffDetail and table Database`
--Backend
Modified models.py
    add class Staff Table Order...
Add
    hos\management\commands\importStaff.py & importTable.py
    beckend\Static\table.csv & staffDetail.csv
Run python manage.py +
    makemigrations & migrate
    importStaff & importTable
Results
    db.sqlite3 has been changed and all data have been recorded
[[[[[[[[FAILED\
        `Frontend Structure build up`
        --Frontend
        Add src\layouts folder
            + Main.vue
        Add src\pages folder
            + Home.vue
            + About.vue
        Add in src
            + routes.js
        Add in src\components
            + VLink.vue
[[[[[[[[FAILED/ and DELETED
`working on the AI dish order system`
--Design
    Input:
    json with the detail of
        number_of_people: integerField
            1/2/2-4/4-8
        taste_perferences: ManyToManyField
            不吃麦麸 - No Wheat
            不吃蔬菜 - No Vegetables
            不吃猪肉 - No Pork
            不吃豆制品 - No Soy Products
            不吃乳制品 - No Dairy
            不能吃辣 - No Spicy

        dining_style: CharField
            勇于尝鲜 - Adventurous Eater
            大吃特吃 - Hearty Appetite
            本店热门 - House Specialties
            传统经典 - Traditional Classics
            随机搭配 - Random Pairings
    Output:
    json with the selected_dishes
--Backend
Modified views.py
    import JsonResponse & models.menu
    add def auto_dish(request)
Modified urls.py
    add urlpatterns auto_dish
--Frontend
Add new components AutoDish.vue
`Working on the optimized of Hos-menu page`
--Frontend
stick the table header to the top of the menu list
margin and set the right position for all the elements

# Renjie Yao 15:21 04/10/2023 #

`Working on the AI dish order system`
Start design the AI algorithm
`Working on the optimized of Hos-menu page`
--Frontend
    Add dialog for not saving empty data into menu database
    Add dialog for success save(update/add)/delete action
[[[[[[[[FAILED\
`import beef image from BE to FE`
--Backend
Modified Static\menu.csv & hos\management\commands\importMenu.py
    only initial beef for now
Modified backend\settins.py & urls.py
Add in Static
    1_Beef.png

--Frontend
Modified 
[[[[[[[[FAILED/ and KEEP for now

# Renjie Yao 16:14 04/10/2023 #

added
    menu
    table
    staff

try to add 
    home page

# Renjie Yao 18:05 07/10/2023 #
*Continue
`import beef image from BE to FE`
--Backend
create the static URL in
    setting.py
modify the menu.csv for URL path data
    menu.csv importMenu.py
--Frontend
change the text <td> in <tbody> of ContainerMeny.vue to import the ${ImageName}.jpg by the url: 
    http://127.0.0.1:8000/static/images/${ImageName}.jpg 
remember to use the <img> to view the image instead of show the URL path in text form.
*Things need to finished:
`Working on the AI dish order system`
Start design the AI algorithm
`Working on the optimized of Hos-menu page`
# Renjie Yao 18:22 07/10/2023 # 


# Renjie Yao & Shuxin Zhu 00:40 16/10/2023 #
`Router is not active in FE`
-- Write Router from the beginning
    --define the path for each page
    --make the router with button

-- optimized the style of the FE
    --change the contents in each pages and make full use of components and pages
    --color and align and style
    --template script style

`Tips for database maintainance`
    如何维护后端数据库：
    1. 在Static里面新建或更改表格
    2.backend/hos/management/commands中新增importNewTable.py（如果你在第一步中增加了新的.csv文件），写法参考其他的commands
    3.在manage.py的同一路径下，运行”python manage.py importXXX“
    注意看是否成功，想要在db.sqlite3中看到改变，记得打开db后使用左上角的刷新按钮

`Working on the AutoDish in BE`
    (Shuxin Zhu)

# Renjie Yao 14:30 16/10/2023 #
`Router Function`
add in router folder
    router.js
Finished the Router and now working from the Welcome Pages
Path:
welcome-(Admin)-login-menu-shoppingcart（parallel with menu）-order success-payment-pay success-receipt-(help)-bye-(Admin)--BACK TO welcome
# Renjie Yao 17:59 16/10/2023 #

# Renjie Yao 11:58 17/10/2023 #
`Functionality of the Menu page`
Done:
    use table menu and table shopCart
    add button for AIMenu
    add/delete functions of the menu and shopCart
Achieved:
1. Customers can view all the items in the menu.
2. Customers can view the total cost in the shopping cart.
3. Customers can view the items they have been selected in the shopping cart.
4. Customers can add new items into cart or remove current items
5. Customers can change the amount of items in the shopping cart
# Renjie Yao 15:57 17/10/2023 #

# Renjie Yao 15:57 17/10/2023 #
`Functionality of the User login`
To achieve:
Customers and administrators can log in to and log out of the website
# Renjie Yao 18:17 17/10/2023 #
achieved:
FE --> BE
    using v-model to do the customer phone number saving
Working on:
    other page views and optimizition
    full stack data transfer

# Renjie Yao 18:15 18/10/2023 #

The table with status of false can not be chosen now

Use jquery to connect the AI Menu

# Renjie Yao & Shuxin Zhu 19:50 19/10/2023 #
`Finish the full pipeline of Customer`
    params including: table_id, people_number, order_code, total_amount
`Working on`
    Debug of customer pipeline
    Admin mode for tables
# Renjie Yao 21:01 19/10/2023 #
`Finished`
    Admin mode for tables
    add the dialog of payment status
`Debug`
    phone number and table should be filled before route to next page

# Renjie Yao & Shuxin Zhu 2:21 20/10/2023 #
`Working on`
1. admin login
2. payment can change the status of the order been paid
3. Administrators can view the total turnover in one day.
    make record of all the finished payment (order)
    add them together in the admin mode
4. Administrators can view the number of item that already sold in one day.
# Renjie Yao & Shuxin Zhu 2:21 20/10/2023 #
1. External API(ChatGPT-3.5 is implemented.)
2. pip install openai && pip install python-decouple before running the frontend.
3. Menu page components optimized.
# Shuxin Zhu 6:21 20/10/2023 #

# Group 02 18:25 20/10/2023 #
Development Finished
Debug Testing Deployment Started!!!!!!!!!!!

# Renjie Yao 17:03 24/10/2023 #
`add new routes`
hosWelcome ->
    adminLogin ->
        adminMainMenu ->
            manageMenu
            manageTable
            showAllOrders
^---------Back(to hosWelcome)

`Problem`
Login
# Renjie Yao 17:05 24/10/2023 #

# Renjie Yao 18:08 25/10/2023 #
Concentrate the manage.py commands as
    deleteHistory (Delete Order, orderContent, payment and Customer)
    &
    initialDb (initial Menu, Table and Staff)
Optimized the payment
    can NOT go back from cardPay to the Payment (choice) page
Optimized the layout of the Admin Login
Optimized the order success page
    add a setTimeOut(1000) for the situtations that the order content can not be show completely while adding order content to the database
# Renjie Yao 18:17 25/10/2023 #

# Zimeng Liu 11:03 29/10/23 #
For frontend
Define the initial data of CardPayPage
Add Listening and Dynamic Input Validation for input variable
The following input are subject to form entry restrictions：
    cardholder_name (letter only )
    card_number (number only )
    expireDate (number and “/” only )
    cvv (number only )
 The input does not matched will be automatically deleted
Separated the payment initiation logic (processPayment method) from the actual payment submission logic (submitCardPay method)
Add dynamic request URL to connect with API in backend
Improved handling of responses received from the backend
    Clearly reflect to the user whether the payment was successful or not
    A feedback can be received by users when an error occurs during the request process
# Zimeng Liu 11:13 29/10/23 #

# Zimeng Liu 11:33 29/10/23 #
For backend
Add one cardpay class 
Creat a new .csv file named cardpay.csv to store simulated payment data
Creat import_cards.py 
Add hos_cardpay form to database
Create a new API endpoint to connect with frontend
# Zimeng Liu 11:42 29/10/23 #

# Zimeng Liu 12:25 29/10/23 #
Add new items in .gitignore to ignore some mac system default files
Prevent the confliction when merging files
# Zimeng Liu 12:27 29/10/23 #