# Part 2: Setting the Foundation (Django + Unpoly)

The beauty of Unpoly is that it requires almost zero configuration on the backend. Django doesn't even know Unpoly exists—it just serves HTML.

## 1. The Setup
First, we set up a standard Django project. The only "special" requirement is including the Unpoly script.

In `templates/base.html`, we load the library:

```html
<head>
    <!-- Unpoly CSS & JS -->
    <link rel="stylesheet" href="{% static 'css/unpoly.min.css' %}">
    <script src="{% static 'js/unpoly.min.js' %}"></script>
    
    <!-- CSRF Configuration -->
    <meta name="csrf-param" content="csrfmiddlewaretoken">
    <meta name="csrf-token" content="{{ csrf_token }}">
    <script>
        up.protocol.config.csrfHeader = 'X-CSRFToken';
    </script>
</head>
```

**Crucial Step:** We configure Unpoly to send the CSRF token with every request. This solves 99% of "403 Forbidden" errors people face when integrating AJAX with Django.

## 2. The Main Target
Unpoly needs to know *what* to update when a user clicks a link. By default, it updates the `body`, but that's inefficient because it re-renders the Navbar and Footer unnecessarily.

We define a "Main Content" area:

```html
<!-- base.html -->
<nav class="navbar">...</nav>

<div class="container main-content" up-main>
    {% block content %}
    {% endblock %}
</div>

<footer>...</footer>
```

Adding the `up-main` attribute is a shorthand. It tells Unpoly: *"If a link doesn't specify a target, assume they want to update this div."*

## 3. Writing Standard Views
On the Django side, we write standard Class-Based Views.

```python
# views.py
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
```

We don't need `JsonResponse`. We don't need serializers. We just render the template.

When Unpoly requests this URL, it receives the **entire HTML page**. But because it knows it only needs to update `.main-content`, it parses the response, extracts that `div`, and swaps it into the current page.

This is **Fragment Updating**, and it's the core of the Page-Less experience.
