# Building Page Less: A Modern Django + Unpoly Masterclass
## Part 1: The Case for Page-Less Apps

**Welcome to the "Building Page Less" series.** In this 8-part journey, we will build a production-grade blogging platform that feels like a Single-Page Application (SPA) but keeps the simplicity of a standard Django project.

### Series Overview
1.  **[Part 1: The Case for Page-Less Apps](#)** (You are here)
2.  **[Part 2: Setting the Foundation (Django + Unpoly)](./02_setup.md)**
3.  **[Part 3: Turbocharging Navigation](./03_navigation.md)**
4.  **[Part 4: Modal Magic & Layers](./04_modals.md)**
5.  **[Part 5: Forms & Validation](./05_forms.md)**
6.  **[Part 6: Instant Search](./06_search.md)**
7.  **[Part 7: CRUD without Chaos](./07_crud_messages.md)**
8.  **[Part 8: Conclusion & UI Polish](./08_conclusion.md)**

---

## The "SPA Fatigue" is Real
For the last decade, web development has drifted towards a heavy, bifurcated architecture: a backend API (Django DRF, FastAPI) and a completely separate frontend SPA (React, Vue, Next.js).

While this architecture makes sense for massive teams like Facebook or Airbnb, for 90% of projects, it introduces crushing complexity:
-   **State Synchronization**: You have to manually keep the client state in sync with the server.
-   **Hydration**: You need complex SSR (Server Side Rendering) just to make your site SEO friendly.
-   **Duplicate Logic**: Validation logic often lives in both Python (backend) and JavaScript (frontend).
-   **Build Tools**: Webpack, Babel, Vite, npm, node_modules... the chain never ends.

## Enter HTML-Over-The-Wire
What if you could keep the simplicity of "Old School" Django—standard Views, standard Templates, standard Forms—but get the **speed and fluid feel** of a SPA?

That's the promise of **HTML-Over-The-Wire**. Instead of sending JSON and letting JavaScript build the DOM, you send fast, ready-to-render HTML fragments.

## Why Unpoly?
There are many tools in this space (HTMX, Hotwire/Turbo), but **Unpoly** is unique. It considers itself a "progressive enhancement framework" that treats your server-side app as the source of truth.

Unpoly gives you:
1.  **SPA Navigation**: It intercepts links, fetches the next page via AJAX, and swaps the body content.
2.  **Modals & Layers**: It can take *any* URL and open it in a modal or drawer, without you writing a single line of modal-management JS.
3.  **Validation**: It can submit a form, detect a server-side error, and update *just* the form fields with the error messages.

## The Page_Less Project
In this series, we will dissect **Page_Less**, a production-ready blogging platform built with Django 6.0 and Unpoly.

We will cover:
-   How to set up the "One Layout to Rule Them All".
-   Building a modal-based Authentication flow (Login/Signup).
-   Creating a "live search" that feels instant.
-   Handling CRUD operations without full page reloads.

---
**[Next: Part 2 - Setting the Foundation →](./02_setup.md)**
