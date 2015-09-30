# signup_template
This is a signup page(django allauth) created for Legistify


#Instructions for setup
- Clone the project 
     
        git clone https://github.com/bansalvarun/signup_template.git
        cd signup_template
- Install the project's runtime requirements
      
      Note: Use of virtualenv is recommended.

     - install python (v2.7 is recommended)
     - install pip
     - install requirements   

            pip install -r requirements.txt

- To run the django project

        python manage.py syncdb
        
       - create a super user

            python manage.py makemigrations
            python manage.py migrate

       - visit site 

            http://localhost:8000

       
       - To use Facebook or Linkedin login feature, 

           add Facebook applications and Linkedin applications in
        
            http://localhost:8000/admin/socialaccount/socialapp/  

          - For Facebook make an app here:
                          
            developers.facebook.com
          
          - For Linkedin make an app here:

            https://www.linkedin.com/secure/developer?newapp=
      

