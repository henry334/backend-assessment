# Task 2: Contact Form Implementation
#### Objective:
Build a contact form that allows users to submit their name, email, and message. Upon submission, the form data should be saved to the database, and an email should be sent to the site administrator with the details of the message.

#### Requirements:
1. Form:
    - Create a form that collects the user's name, email, and message.
    - Validate the form so that:
        - The message must be at least 10 characters long.
2. Model:
    - You are provided with a `Contact` model that stores the following fields:
        - **Name**: The name of the user (string).
        - **Email**: The email of the user (email).
        - **Message**: The message sent by the user (text).
        - **Submitted At**: The time the message was submitted (auto-generated).
3. View:
    - Implement a view that processes the contact form:
        - For GET requests, display the form.
        - For POST requests, validate and save the form data, then send an email to the admin.
    - The admin email address should be configurable in the `settings.py` file using `ADMIN_EMAIL`.
4. Email:
    - After a successful form submission, send an email to the site administrator with the user's name, email, and message.
5. User Feedback:
    - If the form is submitted successfully, redirect the user to a "Thank You" page.
    - If there are validation errors, display them on the form page.
#### Deliverables:
A working `forms.py`, `models.py`, `views.py`, and associated templates (`contact.html`, `contact_success.html`).