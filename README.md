Pour lancer le projet il faut avant tous crée un envirenement python :

``` bash
python -m venv env
```

Ensuite il faut activer l'envirement :

Linux  :
``` bash
source env/bin/activate
```

Windows : 
```
env\Scripts\activate
```

S'il ne sont pas deja installer il faut installé : 
``` bash
pip install django djangorestframework
```

Ensuite il faut lancer les migration :
``` bash
python manage.py migrate
```

Pour lancer le server :
```
python manage.py runserver
```