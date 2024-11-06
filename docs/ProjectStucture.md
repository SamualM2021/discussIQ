# Project Structure
The purpose of `ProductStructure.md` is to provide a consistent, organized project structure which is crucial for maintainability and scalability.

/discussIQ
│
├── assets/               # Folder for images, logos, icons, etc.
│   └── company_logo.png  # Example: company logo image
│
├── documentation/        # Folder for documentation
│   └── dockerfile_containerization.md  # Example doc
│
├── /flask_app/             # Flask-specific code
│   ├── /static/            # Static files (e.g., CSS, JS)
│   ├── /templates/         # HTML templates
│   ├── __init__.py         # Initialize Flask app and routes
│   ├── /routes/            # Flask routes and controllers
│   ├── /models/            # Flask app data models (if needed)
│   └── /utils/             # Helper functions for Flask
│
├── /fastapi_app/           # FastAPI-specific code
│   ├── /static/            # Static files (if needed)
│   ├── /templates/         # HTML templates (if used)
│   ├── __init__.py         # Initialize FastAPI app and routes
│   ├── /routes/            # FastAPI routes and controllers
│   ├── /models/            # FastAPI app data models (if needed)
│   └── /utils/             # Helper functions for FastAPI
│
├── /shared/                # Shared code between Flask and FastAPI
│   ├── /database/          # Database models, migrations, etc.
│   ├── /utils/             # Helper functions shared across both apps
│   ├── /schemas/           # Pydantic models (for FastAPI)
│   └── /services/          # Core services, logic used by both apps
│
├── /tests/                 # Unit tests, integration tests
│   ├── /flask_tests/       # Tests for Flask-specific routes
│   ├── /fastapi_tests/     # Tests for FastAPI-specific routes
│   └── /shared_tests/      # Tests for shared services, models
│
├── requirements.txt        # Common dependencies (Flask, FastAPI, etc.)
├── requirements-dev.txt    # Development dependencies (pytest, linters)
├── Dockerfile              # Containerization (if applicable)
├── .gitignore              # Git ignore rules
├── setup.py                # Package setup and entry point
└── README.md               # Project overview and instructions

# Key Practices
Key Practices:
**Separation of Framework-Specific Code**: Keep FastAPI and Flask-specific code in their own directories (/flask_app and /fastapi_app) to avoid confusion.
**Shared Code**: Create a /shared directory for code that both frameworks can use (e.g., database models, utility functions). This will reduce code duplication.
**Testing**: Separate tests for each framework, but also have tests for shared components. It helps ensure that changes to shared code don’t break either framework.
**Documentation**: Keep all docs in a /docs folder, including detailed API docs for both FastAPI and Flask routes.
**Flexibility**: You could configure your app to choose between Flask or FastAPI as a runtime option (perhaps through environment variables or a settings file).
