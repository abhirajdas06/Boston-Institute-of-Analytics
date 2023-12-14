# Framework Setup

This project demonstrates the setup of a Django project with two views, one using `Template Response` and the other using a `HttpResponse`.

## Task 1: Framework Setup

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

   Open your web browser and go to http://127.0.0.1:8000 to see the results.

## Additional Information

- The project contains two views: one using `Template Response` and the other using a `HttpResponse`.
- Views can be accessed by visiting http://127.0.0.1:8000.
