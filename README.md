For develop
=====
1.load project from github
### 
      git clone https://github.com/YatingZhang/WinterSchool.git
  
2.install python
### 
3.install django 1.7
### 
4.install mysql
### 
5.create database(no need to create table)
### 
      create database winSchool;
### 
6.edit setting file
### 
      file path: /WinterSchool/WinterSchool/setting.py
### 
      DATABASES = {
            'default': {
                  'ENGINE': 'django.db.backends.mysql',
                  'NAME': 'winSchool',
                  'USER': 'database username',
                  'PASSWORD': 'database password',
                  'HOST': 'localhost',
                  'PORT': '',
            }
      }
7.set up database
###
      run 'python manage.py migrate'
8.run django project
      python manage.py runserver 0.0.0.0:8080
9.visiting website
      http://0.0.0.0:8080/WinterSchool/
