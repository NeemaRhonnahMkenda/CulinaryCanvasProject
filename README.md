# CulinaryCanvasProject

Welcome to the Culinary Canvas Project! This project is a platform where you can explore and share delicious recipes, cooking tips, and culinary experiences. Whether you're a seasoned chef or a home cook, Culinary Canvas is the perfect place to discover, create, and connect with a community of food enthusiasts.

## Features

- Explore a variety of recipes from different categories.
- Share your own favorite recipes with the community.
- Latest posts section to stay updated on trending recipes.
- User-friendly interface for a seamless cooking experience.

## UI DESIGNS

![image](https://github.com/NeemaRhonnahMkenda/CulinaryCanvasProject/assets/115183776/2505e7c4-3ee0-419c-8f19-8b0129164955)

![image](https://github.com/NeemaRhonnahMkenda/CulinaryCanvasProject/assets/115183776/ed0eee70-98cc-4e31-8766-7fe2816631a7)

![image](https://github.com/NeemaRhonnahMkenda/CulinaryCanvasProject/assets/115183776/952d435f-ac07-435e-abe8-874abe87d3f5)

![image](https://github.com/NeemaRhonnahMkenda/CulinaryCanvasProject/assets/115183776/f7eec9f3-9bab-4892-b603-0cc87466b5f7)

![image](https://github.com/NeemaRhonnahMkenda/CulinaryCanvasProject/assets/115183776/2af90f93-d141-414b-abbe-efac9ae21530)

![image](https://github.com/NeemaRhonnahMkenda/CulinaryCanvasProject/assets/115183776/ce954387-e31b-4750-82c6-474d7dfea6d0)

![image](https://github.com/NeemaRhonnahMkenda/CulinaryCanvasProject/assets/115183776/46fa4aab-2a21-4aff-bca3-f21021b6541f)

![image](https://github.com/NeemaRhonnahMkenda/CulinaryCanvasProject/assets/115183776/8c6a7ab5-f90d-409c-9625-69d7686c1b80)

![image](https://github.com/NeemaRhonnahMkenda/CulinaryCanvasProject/assets/115183776/d77554ea-2e64-4624-a0ea-5a13a2a647b7)

## Running it live (PythonAnywhere, shown on the portfolio)

The app is served at `https://neema-portfolio-pearl.vercel.app/culinary-canvas-django`:
the portfolio proxies that path to PythonAnywhere, where SQLite and uploaded photos are
stored permanently. A [Next.js rebuild](https://github.com/NeemaRhonnahMkenda/culinary-canvas)
of the same app runs at `/culinary-canvas`.

Configuration comes from environment variables (nothing secret is committed):

| Variable | Example |
| --- | --- |
| `DJANGO_SECRET_KEY` | a long random string |
| `DJANGO_DEBUG` | `0` in production |
| `DJANGO_ALLOWED_HOSTS` | `yourname.pythonanywhere.com` |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | `https://neema-portfolio-pearl.vercel.app,https://yourname.pythonanywhere.com` |
| `DJANGO_URL_PREFIX` | `culinary-canvas-django` |

Fresh database with demo content: `python manage.py migrate && python manage.py seed_demo`.

Security notes: only a recipe's author can edit or delete it (others get a 404), delete
is POST-only with a CSRF token, cookies are scoped to the app's path, and the database
is never committed (`db.sqlite3` is in `.gitignore`).
