## Django-Vue-Init
This is for make the initialized develop environment quickly  
Sometimes I need to show up the my plan to someone quickly or test to somethings in a short period  
Of course, it's not except that during in development meetings too  
Although This is very simple. This is useful to me  
This environment was created by `Django` and `Vuejs`  

### Clone
```sh
git clone https://github.com/indra-kr/django-vue-init.git
```

### Backend (apidemo)
I think it will be a good environment, if you already after installed and enabled a like `virtualenv` on yours.  
Because below steps will be install a few python packages on your environment.  

#### Build
In the `backend` directory:
```sh
pip3 install -r requirements.txt && python manage.py migrate
```

#### Run 
```sh
python3 manage.py runserver
```

#### API Test
The backend will open a local network using `127.0.0.1:8000` 
You can do a API test by below command:
```sh
curl http://127.0.0.1:8000/api/v1/apidemo/
```
Also, you can see the response on your web browser  
http://127.0.0.1:8000/api/v1/apidemo/

### Frontend (vuedemo)

#### Build and Run for development mode
In the `frontend` directory:
```sh
npm install && npm run dev
```

The frontend will open a local network by `127.0.0.1:8080`  
You can check the API call transaction on your web browser

> Note: Definitely, this frontend environment is not for deployment.  
> Because of that, you can find webpack modules from frontend directory.  
> This is just for come up with backend and frontend environment more than quickly.  
> Please don't forget it.  
