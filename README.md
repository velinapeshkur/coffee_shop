# <img width="20" alt="Favicon" src="https://cdn-icons-png.flaticon.com/512/31/31082.png"> coffee_shop

website description

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

- Copy and edit .env file for handling environment variables:
```sh
(venv)$ cd coffee_shop
(venv)$ cp .env.example .env
(venv)$ echo SECRET_KEY='your_token' > .env
(venv)$ echo DEBUG=True >> .env
```
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

<img width="600" alt="Screenshot 2022-07-26 at 13 25 24" src="https://user-images.githubusercontent.com/94002579/180990254-607b4879-8d87-4824-926f-e1862dd75ce9.png"> 
Product quantity field is editable, after changing it the total price is updated (max quantity equals total quantity of products left)

### Checkout

| <img width="500" alt="Screenshot 2022-07-26 at 13 25 47" src="https://user-images.githubusercontent.com/94002579/180998472-a4a559e7-630b-4157-ad00-478c7de38c38.png"> | <img width="500" alt="Screenshot 2022-07-26 at 13 26 56" src="https://user-images.githubusercontent.com/94002579/180998478-dff3bc65-66c8-4797-943e-f485cfde70fb.png"> |
|:--:| :--: |
| *Login View* | *Guest View (Login Popup)* |

Add/Remove Coupon Functionality:

<img width="400" alt="Screenshot 2022-07-26 at 13 26 05" src="https://user-images.githubusercontent.com/94002579/180999432-3e18a66f-e63d-4e26-9135-1fe02062d14c.png">

Order Confirmation Page: 

<img width="600" alt="Screenshot 2022-07-26 at 13 26 30" src="https://user-images.githubusercontent.com/94002579/181011747-37f17a05-2881-46c9-9d12-0ea0765d4aab.png">


## Admin Panel
