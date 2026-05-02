# Surjagad Ispat — Django Project

A full conversion of the original React/Vite frontend into a clean Django project.
All pages, styles, animations, and assets are preserved exactly.

## Project Structure

```
surjagad_ispat/
├── manage.py
├── requirements.txt
├── surjagad_ispat/         # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/                   # Main app
    ├── views.py            # All page views (index, about, business, products, careers, contact, media)
    ├── urls.py             # URL routing
    ├── templatetags/
    │   └── core_extras.py  # Custom template filters (split, divisibleby)
    ├── templates/
    │   └── core/
    │       ├── base.html           # Base layout (navbar + footer)
    │       ├── index.html          # Home page
    │       ├── about.html
    │       ├── business.html
    │       ├── products.html
    │       ├── careers.html
    │       ├── contact.html
    │       ├── media.html
    │       └── includes/           # Reusable section partials
    │           ├── page_hero.html
    │           ├── stats_bar.html
    │           ├── about_section.html
    │           ├── segments.html
    │           ├── products_section.html
    │           ├── projects.html
    │           ├── esg.html
    │           ├── trust.html
    │           ├── global.html
    │           ├── news.html
    │           └── careers_cta.html
    └── static/
        └── core/
            ├── style.css           # All styles (replaces Tailwind + styles.css)
            ├── main.js             # Reveal, Counter, Navbar, Mega-menu, Mobile drawer
            ├── favicon.ico
            └── assets/             # All images
                ├── hero-steel.jpg
                ├── plant-aerial.jpg
                ├── esg-wind.jpg
                ├── logistics-port.jpg
                ├── project-bridge.jpg
                ├── product-coils.jpg
                ├── product-sheets.jpg
                └── product-structural.jpg
```

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Apply migrations
python manage.py migrate

# 3. Collect static files
python manage.py collectstatic --noinput

# 4. Run the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000/

## Pages

| URL | View | Template |
|-----|------|----------|
| `/` | `index` | `core/index.html` |
| `/about/` | `about` | `core/about.html` |
| `/business/` | `business` | `core/business.html` |
| `/products/` | `products` | `core/products.html` |
| `/careers/` | `careers` | `core/careers.html` |
| `/contact/` | `contact` | `core/contact.html` |
| `/media/` | `media_page` | `core/media.html` |

## Hero Video

If you have the `hero.mp4` video, place it at:
```
core/static/core/videos/hero.mp4
```
Then uncomment the `<source>` tag in `core/templates/core/index.html`.

## Production Deployment

Update `settings.py`:
- Set `DEBUG = False`
- Set `ALLOWED_HOSTS` to your domain
- Use a production WSGI server (gunicorn, uWSGI)
- Serve static files via nginx or a CDN

## Docker

Build the image:

```bash
docker build -t surjagad-ispat .
```

Run the container:

```bash
docker run --rm -p 8000:8000 surjagad-ispat
```

Then open http://localhost:8000/
