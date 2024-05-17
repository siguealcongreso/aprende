# learn

learn es una aplicación web para aplicar quizes.

## Para contribuir a la aplicación

1. Copia este repositorio a tu cuenta (Crea un fork)

2. Clona de tu repositorio a tu computadora:

       git clone git@github.com:<tu-usuario>/learn.git

3. Crea un entorno virtual

       cd learn
       python3 -m venv env

4. Activa el entorno virtual

       . env/bin/activate

5. Instala la aplicación con sus dependencias en modo de desarrollo

       pip install -e .

6. Corre la aplicación

       pserve development.ini

7. Crea una rama para las modificaciones

       git checkout -b agregar-mejora

8. Haz modificaciones

9. Empuja tus modificaciones a tu repositorio

10. Solicita que se incluyan tus cambios (Crea un Pull Request)

## Para generar la documentación

1. Activa el entorno virtual

       . env/bin/activate

2. Instala la dependencia para la documentación

       pip install -e '.[doc]'

3. Genera la documentación

       cd docs
       make html

4. Navega a build/html/index.html
