from flask import Flask, redirect, url_for, flash, request, Response


def CreateApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jflkdsjfalksjfdsa jfsdlkjfdsljfa'   
   
    from .views import views
    from .resume import resume
    from .contact import contact
    from .projects import projects
    
    bp_list = [views, resume, contact, projects]
        
    for bp in bp_list:
        app.register_blueprint(bp, url_prefix='/')
        

        
    return app