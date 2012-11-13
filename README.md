About Postato
----

This is Postato (don't sue me)! a vote-based blogging system made with djangoappengine.

**REQUIREMENTS**

+ [Python ver. 2.7](http://www.python.org/download/releases/2.7/)
+ [Git](https://github.com/)
+ [Mercurial](http://mercurial.selenic.com)


Installation and usage
----------------------

Clone the repository:

        % git clone git://github.com/samuele-mattiuzzo/posta-to-app.git posta-to

Now we need to download all the required libraries.
There's a script provided inside *srv* folder:

        % cd posta-to/srv
        % python align_libs.py

This script downloads for you (either with git or hg):

+ [django-nonrel][1]
+ [djangoappengine][2]
+ [django-toolbox][3]
+ [django-autoload][4]
+ [django-dbindexer][5]
+ [django-filetransfers][6]

then copies the modules inside your project root folder.

**NOTE**: make sure you have python, git and mercurial installed before running this script.

Last thing to do is pushing some data inside the database.

        % python manage.py syncdb

Insert an admin user when prompted for (not required)

Launch the application:

		% dev_appserver.py .

and point your browser to *http://localhost:8080/*


Developement status
----------------
- Vote tracking for users
- Tagging system (new one or maybe [django-tagging][7])
- Image uploading with resizing
- Image cancellation
- Css color restyling


[1]: https://github.com/django-nonrel
[2]: https://github.com/djangoappengine
[3]: https://github.com/django-nonrel/djangotoolbox
[4]: http://bitbucket.org/twanschik/django-autoload/
[5]: https://github.com/django-nonrel/django-dbindexer
[6]: https://bitbucket.org/wkornewald/django-filetransfers
[7]: http://code.google.com/p/django-tagging/
