#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""
import os
import click
import pymysql
from flask.cli import FlaskGroup
from app import create_app

# Initialize the app using factory pattern
app = create_app(os.environ.get("FLASK_CONFIG") or "default")
cli = FlaskGroup(app)


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_NAME = os.getenv("DB_NAME", "pantrybuddy_db")

@cli.command("init_db")
def init_db():
    """Run the SQL script to initialize the database and user."""
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()

        with open("utils/setup_dev_db.sql", "r") as sql_file:
            sql_script = sql_file.read()
        
        # Execute each statement separately
        for statement in sql_script.split(";"):
            if statement.strip():
                cursor.execute(statement)

        print("✅ Database and user initialized successfully!")
        connection.commit()
        cursor.close()
        connection.close()

    except Exception as e:
        print(f"❌ Error initializing database: {e}")

@cli.command("migrate")
def migrate():
    """Apply migrations to the database."""
    try:
        with app.app_context():
            from app.models import storage
            storage.reload()  # Runs Flask-Migrate's upgrade command
    except Exception as e:
        print(f"❌ Error migrating database: {e}")
    print("✅ Database migrated successfully!")


@cli.command("seed_db")
def seed_db():
    """Insert initial data into the database."""
    with app.app_context():
        from app.models import User, storage
        admin = User(username="admin", email="admin@pantrybuddy.com", role="admin")
        storage.new(admin)  # Add to session
        storage.save()  # Commit changes
    print("✅ Database seeded with initial data!")


if __name__ == "__main__":
    cli()
