# Client Gallery Generator

A professional, self-hosted web application for photographers to upload event photos and deliver them to clients in a beautiful, private, and shareable web gallery.

## The Problem

Photographers spend hours shooting and editing, only to deliver their final work through a cold, impersonal link (like Google Drive, Dropbox, or WeTransfer). These methods are often clunky, have expiration dates, and don't reflect the premium quality of the photographer's brand.

## The Solution

This application provides a simple admin panel for photographers to:
1.  Create a new gallery (e.g., "Smith Wedding").
2.  Upload all the photos for that event.
3.  Generate a single, beautiful, and shareable link (`your-site.com/gallery/abc-123`).

The client receives a link to a stunning, responsive, and easy-to-use gallery page to view, download, and share their photos.

### Key Features (MVP)

* **Admin Panel:** A secure, password-protected dashboard for the photographer.
* **Gallery Management:** Create, Read, Update, and Delete galleries.
* **Multi-File Upload:** An easy-to-use drag-and-drop uploader for photos.
* **Unique Link Generation:** Automatically generates a unique, hard-to-guess URL for each gallery.
* **Beautiful Client-Facing Template:** A single, responsive, and elegant HTML/CSS/JS template that displays the photos.

### Tech Stack

* **Backend:** Python (Flask/Django) / Java (Spring Boot)
* **Database:** PostgreSQL / MySQL / SQLite
* **Frontend:** HTML, CSS, JavaScript (for the gallery template)
* **File Storage:** Local server storage or cloud (S3, Google Cloud Storage)

### Getting Started

1.  Clone this repository.
2.  Install backend dependencies: `pip install -r requirements.txt`
3.  Set up your `.env` file with database credentials.
4.  Run database migrations.
5.  Start the server: `python app.py`
