# Cooker

<p align="center">
  <img src="app/static/images/cooker-logo.png" alt="Cooker logo" width="320">
</p>


A tutorial Flask recipe app built for the [Flask-Commands tutorial docs](https://flask-commands.readthedocs.io/en/stable/), demonstrating routes, controllers, models, migrations, templates, Tailwind CSS, and a small seeded SQLite database.

The app demonstrates a simple recipe project with public recipe pages and a test kitchen area for managing recipes, ingredients, cook steps, tips, comments, and images. It uses Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, and Tailwind CSS.

## Tutorial Safety Note

This project is designed only for tutorial and educational purposes. It is not production-ready.

Some admin-style areas, including the test kitchen routes for creating, updating, and deleting records, intentionally do not include authentication, authorization, or CSRF protection. This keeps the example focused on the Flask-Commands tutorial concepts, but it also means the app should only be run locally in a trusted development environment.

Before adapting this project for a real application, add proper login protection, permission checks, CSRF protection, form validation, error handling, and production-safe configuration.

## Important Database Note

This tutorial repo intentionally includes `cooker_dev.db` so learners can start with a development database that already contains fake data.

To make that possible, `.gitignore` currently includes this exception:

```gitignore
!cooker_dev.db
```

If you use this project as the starting point for your own application, I highly recommend removing that line from `.gitignore`.

That way local development databases will stay ignored and you will not accidentally push a database file to GitHub, whether it contains development or production data.

## Getting Started

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Then update `.env` with values like:

```env
SECRET_KEY=your-secret-key
FLASK_APP=run.py
FLASK_CONFIG=development
APP_NAME=Cooker
SQLALCHEMY_DEVELOPMENT_DATABASE_URI=sqlite:///cooker_dev.db
SQLALCHEMY_PRODUCTION_DATABASE_URI=
```

Run database migrations:

```bash
flask db upgrade
```

Start the Flask development server:

```bash
flask run --debug
```

Then visit:

```text
http://127.0.0.1:5000
```

## Tailwind CSS

Install Node dependencies:

```bash
npm install
```

Watch and rebuild the development CSS file:

```bash
npm run watch:css
```

Build the minified CSS file:

```bash
npm run build:css
```

## macOS Helper Script


After you have completed the setup steps above, you can use the included `run.sh` helper script when returning to work on the project.

This script is not required for setup. It is just a macOS convenience script that opens the common tutorial workflow for you.

Before running it, open `run.sh` and replace every instance of:

```text
CHANGE_TO_YOUR_PARENT_DIRECTORY_TO_COOKER
```

with the path to the parent folder that contains the `cooker` project.

For example, if your project lives here:

```text
/Users/drewbutcher/Documents/demos/cooker
```

then the parent directory is:

```text
/Users/drewbutcher/Documents/demos
```

So this line:

```bash
cd CHANGE_TO_YOUR_PARENT_DIRECTORY_TO_COOKER/cooker
```

should become:

```bash
cd /Users/drewbutcher/Documents/demos/cooker
```

After updating the path, run:

```bash
./run.sh
```

The script opens Terminal tabs for the Flask shell, the Flask development server, Tailwind CSS commands, VS Code, and Chrome.

This script is macOS-specific. It uses Terminal, Chrome, VS Code, `osascript`, and `fswatch`, so you may need to install or adjust those tools for your machine.

## Project Structure

```text
app/
  controllers/      Request handling logic
  models/           SQLAlchemy models
  routes/           Flask blueprints and route definitions
  static/           CSS assets
  templates/        Jinja templates

config/             Flask configuration classes
migrations/         Flask-Migrate / Alembic migration files
run.py              Application entry point
requirements.txt    Python dependencies
package.json        Tailwind CSS scripts
```

## What This App Demonstrates

- Flask application factory setup
- Environment-based configuration
- SQLAlchemy models and relationships
- Flask-Migrate database migrations
- Blueprint-based route organization
- Controller-style request handling
- Jinja templates
- Tailwind CSS build scripts
- A small tutorial-friendly SQLite development database