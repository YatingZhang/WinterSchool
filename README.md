For develop

1.load project from github
  git clone https://github.com/YatingZhang/WinterSchool.git
2.install python
3.install django 1.7
4.install mysql
5.create database winSchool(no need to create table)
6.edit setting file
  file path: /WinterSchool/WinterSchool/setting.py
  edit:
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
7.run 'python manage.py migrate' to set up database
