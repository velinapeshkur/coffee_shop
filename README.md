# <img width="23" alt="Favicon" src="https://cdn-icons-png.flaticon.com/512/31/31082.png"> Coffee Roasters Shop

## Table of contents

- [Overview](#overview)
- [Setup](#setup)
- [Website Demo](#website-demo)
- [Admin Panel](#admin-panel)
- [Task List](#task-list)
- [Credits](#credits)


## Overview

Coffee Roasters Shop is a personal portfolio ecommerce website, made with Python and Django framework in the backend and HTML, CSS, JQuery and Bootstrap for the frontend. Currently hosted on https://coffeeshop.pythonanywhere.com/. 

Website allows to shop as a guest and a registered user. Key features also include:
- shopping cart session handling
- interactive search bar
- displaying order history
- user profile management
- automatically generated user avatar (using initials)
- coupon system
- order confirmation email (Django SMTP)
- easy-to-use admin panel
- responsive web design

## Setup

- Clone the repository:
```sh
$ git clone https://github.com/velinapeshkur/coffee_shop.git
$ cd coffee_shop
```

- Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

- Install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```

- Generate a Django Secret Key at https://djecrety.ir/

- Copy .env file for handling environment variables:
```sh
(venv)$ cd coffee_shop
(venv)$ cp .env.example .env
```
- Edit .env file manually by adding custom variables.

&#x2757; Note: To use gmail in Django project, you need to turn on 2-step verification and generate an app password.
For more info, please visit Google Help Center page: https://support.google.com/accounts/answer/185833?hl=en 

- Make initial migrations: 
```sh
(venv)$ cd ..
(venv)$ python manage.py migrate
```

- Collect static files:
```sh
(venv)$ python manage.py collectstatic
```

- Create a superuser to access admin features:
```sh
(venv)$ python manage.py createsuperuser
```

- Run the server locally:
```sh
(venv)$ python manage.py runserver
```

- Navigate to http://127.0.0.1:8000/

## Website Demo

### Home Page

| <img width="500" alt="Screenshot 2022-07-26 at 13 23 04" src="https://user-images.githubusercontent.com/94002579/180986437-37b81ec3-d9bc-4c9d-b32f-c6707321595f.png"> | <img width="500" alt="Screenshot 2022-07-26 at 13 23 36" src="https://user-images.githubusercontent.com/94002579/180987090-6d2d0271-932e-4082-8ab0-99606093565a.png"> |
|:--:| :--: |
| *Guest View* | *Login View* |

### Search Bar

| <img width="350" alt="Screenshot 2022-07-28 at 16 45 05" src="https://user-images.githubusercontent.com/94002579/181520793-076fb0d4-8812-4760-9288-1ec71e94e82b.png"> |
| --- |

### Login & Sign Up

| <img width="500" alt="Screenshot 2022-07-26 at 13 27 30" src="https://user-images.githubusercontent.com/94002579/180988811-81e83719-1221-4913-a906-8223979b3344.png"> | <img width="500" alt="Screenshot 2022-07-26 at 13 27 55" src="https://user-images.githubusercontent.com/94002579/180988950-6e46d6a4-1e9f-447e-ba62-890968342af5.png"> |
|:--:| :--: |

### Coffee List View

| <img width="500" alt="Screenshot 2022-07-26 at 13 24 05" src="https://user-images.githubusercontent.com/94002579/180989673-b45e7819-9d00-4b2a-907d-50a7f5da6312.png"> | <img width="500" alt="Screenshot 2022-07-26 at 13 24 18" src="https://user-images.githubusercontent.com/94002579/180989685-d0c75dc2-abe4-4220-b791-1cbf8af03cf0.png"> |
|:--:| :--: |
| *All Coffees* | *Coffees by Category* |

### Coffee Detail View

| <img width="500" alt="Screenshot 2022-07-26 at 13 25 03" src="https://user-images.githubusercontent.com/94002579/180989942-26e72771-404e-40a5-8faf-ad10055c13f6.png"> | <img width="500" alt="Screenshot 2022-07-26 at 14 00 29" src="https://user-images.githubusercontent.com/94002579/180990846-3447c5ee-d8d0-46c7-902d-2dd7b7f898a6.png"> |
|:--:| :--: |

### Cart

| <img width="600" alt="Screenshot 2022-07-26 at 13 25 24" src="https://user-images.githubusercontent.com/94002579/180990254-607b4879-8d87-4824-926f-e1862dd75ce9.png"> |
| --- |

Product quantity field is editable, after changing it the total price is updated (max quantity equals total quantity of products left). 

### Checkout

| <img width="500" alt="Screenshot 2022-07-26 at 13 25 47" src="https://user-images.githubusercontent.com/94002579/180998472-a4a559e7-630b-4157-ad00-478c7de38c38.png"> | <img width="500" alt="Screenshot 2022-07-26 at 13 26 56" src="https://user-images.githubusercontent.com/94002579/180998478-dff3bc65-66c8-4797-943e-f485cfde70fb.png"> |
|:--:| :--: |
| *Login View* | *Guest View (Login Popup)* |

Add/Remove Coupon Functionality:

<img width="400" alt="Screenshot 2022-07-26 at 13 26 05" src="https://user-images.githubusercontent.com/94002579/180999432-3e18a66f-e63d-4e26-9135-1fe02062d14c.png">

### Order Confirmation 

| <img width="600" alt="Screenshot 2022-07-26 at 13 26 30" src="https://user-images.githubusercontent.com/94002579/181011747-37f17a05-2881-46c9-9d12-0ea0765d4aab.png"> | <img width="300" alt="Order Confirmation" src="https://user-images.githubusercontent.com/94002579/181021440-a91305db-4884-429a-b7e7-ce3f43beea63.png"> |
|:--:| :--: |
| *Confirmation Page* | *Confirmation Email* |

### Order History

| <img width="600" alt="Screenshot 2022-07-26 at 16 59 59" src="https://user-images.githubusercontent.com/94002579/181024560-291eddb3-afcc-45bf-b174-108cd92f76fa.png"> |
| --- |

### Profile Page

| <img width="600" alt="Screenshot 2022-07-26 at 16 59 59" src="https://user-images.githubusercontent.com/94002579/181026052-af07926d-4f9e-468a-9d1e-4e4734eafb5f.png"> |
| --- |

## Admin Panel

To access Admin Panel, navigate to http://127.0.0.1:8000/admin/ and log in with superuser credentials. 

### Products

| <img width="600" alt="Screenshot 2022-07-28 at 13 22 31" src="https://user-images.githubusercontent.com/94002579/181483686-ff054725-fbdb-4ec5-a625-26a6594db867.png"> |
| --- |

Admin can easily update product quantity in list view (also updates automatically after ordering). 

### Coupons

| <img width="600" alt="Screenshot 2022-07-28 at 13 22 21" src="https://user-images.githubusercontent.com/94002579/181484343-42e3f574-4b65-4d73-95e4-d0511c501642.png"> |
| --- |

### Orders 

| <img width="600" alt="Screenshot 2022-07-28 at 13 22 50" src="https://user-images.githubusercontent.com/94002579/181485111-77fdf905-f810-4a1b-911d-88ff516495d6.png"> |
| --- |

Manage orders by using admin list actions:
|<img width="498" alt="Screenshot 2022-07-28 at 13 22 56" src="https://user-images.githubusercontent.com/94002579/181486260-476490cb-a9b0-49fc-9265-1488ce5f7dfd.png">|
| --- |

*Show selected orders on a separate page* - custom admin action made with bootstrap cards: 
|<img width="600" alt="Screenshot 2022-07-28 at 13 24 05" src="https://user-images.githubusercontent.com/94002579/181486920-cfa084e5-5b01-466b-b101-fca365d0a613.png">|
| --- |

## Task List

- [ ] Replace no-template views with AJAX calls
- [ ] Enable login with email
- [ ] Enable social login
- [ ] Add 'Forgot password' option to login page
- [ ] Add 'Favourites'
- [ ] Integrate payment system
- [ ] Redesign navbar for small screens

## Credits

All rights for logo and images belong to [UE Coffee Roasters](https://uecoffeeroasters.com/).
