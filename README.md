# Page Less

**Page Less** is a modern, high-performance blogging platform that combines the robustness of **Django** with the fluid, single-page-application (SPA) feel of **Unpoly**, all styled with a custom **Material 3** design system built on top of **Bootstrap 5**.

This project demonstrates how to build "page-less" experiences—where navigation feels instant and context is preserved—without the complexity of a separate frontend framework (like React or Vue) or a JSON API.

---

## 📚 Table of Contents
1. [Introduction](#introduction)
2. [Tech Stack Overview](#tech-stack-overview)
3. [Project Setup](#project-setup)
4. [Architecture & Codebase Tour](#architecture--codebase-tour)
5. [Key Features](#key-features)

---

## <a name="introduction"></a> 1️⃣ Introduction

### The "Page Less" Philosophy
Modern web development often forces a choice: build a traditional Multi-Page Application (MPA) that feels slow due to full page reloads, or build a Single-Page Application (SPA) that introduces massive complexity (state management, hydration, API layers).

**Page Less** takes a third path: **HTML-Over-The-Wire**.

Using [Unpoly](https://unpoly.com/), we interpret HTML interactions (links, forms) as requests for page *fragments*. The server renders standard Django templates, but the browser only updates the specific parts of the page that changed (e.g., the main content area), preserving the scroll position, focus, and loaded JavaScript and CSS.

### Unpoly vs. SPAs
-   **SEO**: Native. Search engines see standard HTML pages.
-   **Performance**: The "first contentful paint" is fast because it's just HTML. No heavy JS bundles to parse before rendering.
-   **Maintainability**: You write standard Django views and templates. No serialization serializers, no client-side routing logic.

---

## <a name="tech-stack-overview"></a> 2️⃣ Tech Stack Overview

### 🐍 Backend: Django 6.0 (Class-Based Views)
We use Django's generic **Class-Based Views (CBVs)** (`ListView`, `DetailView`, `CreateView`, etc.) for almost all logic.
-   **Why?** CBVs provide standard patterns for CRUD operations, reducing boilerplate. They integrate perfectly with Unpoly—if a form is invalid, Django re-renders it with errors; Unpoly simply swaps the form HTML into place.

### ⚡ Frontend Logic: Unpoly
The "engine" of the frontend.
-   **`up-target`**: Tells links which part of the page to update (e.g., `.main-content`).
-   **`up-layer`**: Handles modals, drawers, and overlays natively.
-   **`up-validate`**: Provides live server-side validation.
-   **Why?** It gives us Modal handling, hungry-loading, and history management (back/forward buttons work naturally) with zero custom JavaScript.

### 🎨 UI Framework: Bootstrap 5 + Material 3
We use Bootstrap 5 for the grid system and utility classes, but we have heavily customized it to implement **Material 3** design principles.
-   **Design Tokens**: Custom CSS variables for colors (Primary Purple), typography (Roboto), and shapes (Pills/Rounded).
-   **Glassmorphism**: A custom translucent navbar effect using `backdrop-filter`.
-   **Why?** Bootstrap handles the messy layout/responsiveness, while our custom CSS layer ensures the app looks unique and premium, not like a "default Bootstrap site".

### 📦 Package Manager: uv
We use `uv` (from Astral) for extremely fast Python package management.

---

## <a name="project-setup"></a> 3️⃣ Project Setup

Follow these steps to get the project running locally.

### Prerequisites
-   Python 3.13+
-   `uv` (Recommended) or `pip`

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/page_less.git
    cd page_less
    ```

2.  **Install dependencies/Manage Environment:**
    ```bash
    # Using uv (Creates venv and installs deps)
    uv sync
    source .venv/bin/activate
    
    # OR using pip
    # python -m venv .venv
    # source .venv/bin/activate
    # pip install -r requirements.txt
    ```

3.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Create a Superuser (Optional):**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000/`.

---

## <a name="architecture--codebase-tour"></a> 4️⃣ Architecture & Codebase Tour

The project follows a modular "apps" structure within the `apps/` directory to keep components decoupled.

### 📂 `config/`
The project heart.
-   `settings/`: Split settings (not implemented yet in this demo, but standard practice). Currently `settings.py`.
-   `urls.py`: The main entry point for routing.

### 📂 `apps/core/`
Contains shared logic and the landing page.
-   **`views.py`**: Includes the `HomeView`, rendering the landing page.
-   **`templates/core/home.html`**: The landing page template.

### 📂 `apps/accounts/`
Handles User Authentication.
-   **`models.py`**: Defines `CustomUser` (inheriting `AbstractUser`). Always start a Django project with a custom user model!
-   **`views.py`**:
    -   `LoginView`, `SignUpView`: These inherit from Django's generic views but use `SuccessMessageMixin`. They are designed to be opened in **Unpoly Modals** (`up-layer="new"`).
-   **`forms.py`**: Custom forms for User creation.

### 📂 `apps/blog/`
The core business logic.
-   **`models.py`**:
    -   `Post`: The main entity (Title, Slug, Content, Author).
    -   `Comment`: Related to Post and Author.
-   **`views.py`**:
    -   `PostListView`: Standard list with pagination.
    -   `PostDetailView`: Shows content + comments.
    -   `PostCreateView` / `PostUpdateView`: Uses `PostForm`. Configured to redirect to the detail view on success.
    -   `PostDeleteView`: Special handling to target the `body` layer on success to refresh the whole page (msg + removal).
-   **`forms.py`**:
    -   `PostForm`: Overrides widgets to add `form-select` and `form-control` classes, enforcing the Material 3 look on standard Django form fields.

### 📂 `static/css/main.css`
**The Design System.**
This file defines:
-   `:root` variables for M3 Colors (`--md-sys-color-primary`, etc.).
-   Global overrides for `body`, `h1-h6`.
-   Component overrides for `.btn` (pill shapes), `.card` (elevation), `.navbar` (glassmorphism).

### 📂 `templates/`
-   **`base.html`**: The master template.
    -   Loads Unpoly (`unpoly.min.js`) and Bootstrap.
    -   Defines the Navbar and the generic `{% block content %}` container.
    -   **Crucial**: Defines the `<div class="main-content" up-main>` which is the default target for all Unpoly links.

---

## <a name="key-features"></a> 5️⃣ Key Features

### 🚀 Page-Less Navigation
Links in the navbar have `up-target=".main-content"`. When clicked, Unpoly fetches the URL, extracts the `.main-content` div from the response, and swaps *only* that div. The Navbar and Footer persist.

### 📱 Modal Authentication
Login and Signup buttons use `up-layer="new" up-mode="cover"`.
-   This opens the content in a full-screen overlay (on mobile) or a centered modal (on desktop) without leaving the current page context.
-   Upon successful login, the modal closes, and the underlying page refreshes (`up-layer="root"`).

### 🔍 Live Search
The search bar uses `up-autosubmit` and `up-target=".post-list"`.
-   Typing in the search box automatically submits the form via AJAX.
-   The server returns the filtered list.
-   Unpoly updates just the list area, creating a "live search" feel.

### 🎨 Material 3 Design
The UI feels "native" and premium due to:
-   **Pill Buttons**: High border-radius.
-   **Stateful Colors**: Proper hover/active states derived from M3/Figma tokens.
-   **Elevation**: Soft shadows instead of hard borders.
