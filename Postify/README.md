# Postify

**Postify** is a dynamic social media platform built using Django, where users can post, view, edit, and delete posts or tweets. It provides an engaging and responsive interface for a seamless user experience, whether on desktop or mobile.

---

## Features

### Core Functionalities:
- **User Authentication**: Users can register, log in, and log out securely.
- **Post Management**: Users can create, edit, and delete their own posts, including text and optional images.
- **Search Functionality**: Search for posts based on content or user.
- **Responsive Design**: Optimized for both desktop and mobile views.

### Design:
- **Bootstrap Integration**: Ensures a visually appealing and responsive UI.
- **Dark Mode**: A sleek dark-themed interface for better usability.
- **Image Handling**: Posts support image uploads with automatic resizing for consistent layouts.

![Screenshot_1](Screenshots\image.png)

--- ---

![Screenshot_2](Screenshots\image-3.png)  ![Screenshot_3](Screenshots\image-2.png)    
---

## Installation

### Prerequisites:
- Python 3.7+
- Django 4.0+
- SQLite
- Git

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/vedantfutane/Postify.git
   cd postify
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database in `settings.py`:
   - Update the `DATABASES` section with your database credentials.

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at [http://localhost:8000](http://localhost:8000).

---

## Key Pages
- **Home**: Displays all posts in a grid layout.
- **Create/Edit Post**: Form to add or modify posts with text and image.
- **Search Results**: Displays posts matching the search query.
- **Authentication Pages**: Register, Login, and Logout functionalities.

---

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (Development)

---

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## Acknowledgments
- Bootstrap for UI components.
- Django community for extensive documentation and support.
- OpenAI for insightful development suggestions.

---

## Contact
For any questions or feedback, feel free to reach out to:
- **Name**: Vedant Futane
- **Email**: [vedantfutane2003@gmail.com]
- **GitHub**: [https://github.com/vedantfutane]
