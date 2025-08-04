# Jakub Lejk – Personal Blog & Portfolio

Welcome to my personal blog and digital portfolio, built with Django and managed using Poetry.  
This project is a curated showcase of my experience, certifications, projects, skills, and freelance services — all wrapped in a polished, responsive frontend.

## About the Project

It features:
- A professional resume-style homepage
- Dedicated sections for experience, education, skills, projects, certifications, and interests
- A custom design using Bootstrap and FontAwesome, enhanced with personalized styling
- Django templating and static file management for efficient performance
- A light backend structure that prioritizes speed and simplicity

Whether you're a client, recruiter, or curious visitor, this project offers a clear picture of what I do — and how I do it.

## Tech Stack

- Framework: Django
- Dependency Management: Poetry
- Frontend: HTML5, CSS3, Bootstrap 5, FontAwesome
- Templating: Django Template Language (DTL)
- Static File Handling: Served through NGINX server
- Icons & Fonts: Devicon, Google Fonts

## Project Highlights

- Clean separation of logic and presentation via Django templates
- Rich static asset management with custom stylesheets (`custom_styles.css`, `grayscale.css`, `dog_wrapper.css`, `projects.css`)
- Modular layout with a dynamic sidebar and scroll-to-section navigation
- Responsive design — fully functional on mobile and desktop

## Key Sections

- About Me – Brief overview of who I am and what I do
- Experience – My career history and project involvement
- Skills – Tools, technologies, and platforms I work with (Python, Django, Azure, Spark, etc.)
- Projects – Real-world applications including:
  - [Business Info Poland](https://firmy.lejk.net) – A company data lookup and document downloader
  - [Business Data API](https://github.com/JakLjk/BUSINESS-DATA-API) – The backend powering the data behind Business Info Poland
- Certifications – Verified credentials from Microsoft, Tableau, and others
- Freelance Services – Data scraping, transformation, API development and delivery

## Getting Started – Using This Project as a Template

If you'd like to use this project as a template for your own portfolio or blog, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/JakLjk/PERSONAL_BLOG
cd yourrepo
```

### 2. Install Poetry (if not already installed)
Poetry is used for dependency and virtual environment management.

Install it via the official method
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Install Dependencies
Poetry will automatically create and activate a virtual environment.
```bash
poetry install
```

### 4. Apply Migrations 
Run initial migrations and set up an admin user
```bash
poetry run python manage.py migrate
```

### 5. Generate Static Files
If static files have changed (styles, images or scripts were added/deleted) the static files have to be refreshed
```bash
poetry run python manage.py collectstatic
```

### 6. Test on the Development server
```bash
poetry run python manage.py runserver
```

## Credits and Licensing

This site is based on a template from [Start Bootstrap](https://startbootstrap.com), created by [David Miller](https://davidmiller.io).

The original template is released under the [MIT License](https://opensource.org/licenses/MIT).  
Copyright 2013–2023 Start Bootstrap LLC.

Per the license terms, this project retains the original license and attribution as required.
