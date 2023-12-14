#  RESTful Authentication 

In this project, I have implemented token-based authentication using Django REST framework.

## Task 2:  RESTful Authentication 

1. **Set Up a Virtual Environment.**

    ```bash
    virtualenv venv
    source venv/bin/activate
    # or
    venv\Scripts\activate
    ```

2. **Install Dependencies.**

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply Migrations.**

    ```bash
    python manage.py migrate
    ```

4. **Run the Development Server.**

    ```bash
    python manage.py runserver
    ```

5. **Access the views:**

   Open your web browser and go to:
    - http://127.0.0.1:8000/ to view the list of books.
    - http://127.0.0.1:8000/add/ to add a new book.
    - http://127.0.0.1:8000/{book_id}/ to retrieve details of a specific book.
    - http://127.0.0.1:8000/delete/{book_id}/ to delete a specific book.
    - http://127.0.0.1:8000/update/{book_id}/ to update a specific book.
    Replace {book_id} with the actual ID of a book when accessing the detail, update and delete views.

    Additionally, inside the client folder, there is a Python file provided to perform operations on the API, including listing, retrieving details, and deleting books. Execute this file to interact with the API programmatically.

## Authentication and Permissions

Authentication and permissions have been configured in this project:

- **SessionAuthentication and TokenAuthentication:**
    - Both `SessionAuthentication` and `TokenAuthentication` have been added to the project's `settings.py`. 
    - I have also added `SessionAuthentication` and `TokenAuthentication` inside API Views as a comment. As i have set the `SessionAuthentication` and `TokenAuthentication` as default. The authentication_classes inside the views.py of api app is just for the refrence. 


- **Permission: IsAuthenticatedOrReadOnly:**
    - The `IsAuthenticatedOrReadOnly` permission has been set by default. 

## Additional Information

- Inside the backend folder, a Django project has been created with two apps: books and api.
- The client folder contains Python files (list.py, detail.py, update.py and delete.py) specifically designed to perform operations on the API. These scripts facilitate listing books, retrieving details, updating books and deleting books via the Django Rest Framework endpoints. To interact with the API programmatically, you can execute these files based on your desired operation.
