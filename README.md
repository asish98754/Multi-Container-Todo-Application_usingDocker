# Multi-Container Todo Application (Docker)

A simple Todo web application built with Flask and MongoDB, containerized with Docker and orchestrated using Docker Compose.

## Tech Stack

- Python (Flask)
- MongoDB
- Docker
- Docker Compose
- GitHub Actions (CI/CD)

## Project Structure

- `api/` - Flask app source code, templates, and static assets
- `Dockerfile` - Builds the Flask API image
- `docker-compose.yml` - Runs API + MongoDB together
- `.github/workflows/ci.yml` - Continuous Integration workflow
- `.github/workflows/cd.yml` - Continuous Delivery workflow

## Prerequisites

- Docker Desktop (or Docker Engine + Compose)
- Git

## Run Locally (Docker Compose)

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd Multi-Container-Todo-Application_usingDocker
   ```

2. Start the application:

   ```bash
   docker compose up -d --build
   ```

3. Open the app in your browser:

   [http://localhost:5000](http://localhost:5000)

4. Stop and clean up:

   ```bash
   docker compose down -v
   ```

## CI/CD Pipeline

This repository includes GitHub Actions workflows:

- **CI (`ci.yml`)**
  - Runs on every push and pull request
  - Builds and starts the Docker Compose services
  - Performs a smoke test against `http://localhost:5000`
  - Uploads logs on failure and always tears down containers

- **CD (`cd.yml`)**
  - Runs on push to `main` and can be triggered manually
  - Builds and pushes Docker image to GitHub Container Registry (`ghcr.io`)
  - Publishes tags: `latest` and short commit SHA
  - Optionally triggers deployment via `DEPLOY_WEBHOOK_URL` secret

## Required GitHub Settings

For CD to work, ensure:

- Repository default branch is `main` (or adjust workflow branch)
- GitHub Actions permissions allow package write (already defined in workflow)

Optional deployment trigger:

- Add repository secret: `DEPLOY_WEBHOOK_URL`

## API Notes

- App entry point: `api/app.py`
- MongoDB URI in app config currently targets compose service name:
  - `mongodb://mongo:27017/todo_db`

## License

Add your preferred license here (for example, MIT).
