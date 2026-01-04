# Part 4: Modal Magic & Layers

This is where Unpoly truly shines. Handling Modals in a traditional app usually involves:
1.  Hidden DOM nodes (`<div id="myModal" style="display:none">`).
2.  JavaScript to show/hide them.
3.  AJAX to fetch content into them.

Unpoly introduces the concept of **Layers**.

## Authentication in a Modal
In **Page_Less**, we wanted Login and Signup to be accessible from anywhere without leaving the current page.

### The Code
```html
<a href="{% url 'login' %}" 
   up-layer="new" 
   up-mode="cover" 
   up-target=".login-form">
   Login
</a>
```

-   `up-layer="new"`: Tells Unpoly to open a *new layer* (a modal/overlay) instead of swapping the current content.
-   `up-mode="cover"`: Specifies the style. "Cover" is a full-screen overlay (great for mobile), while "modal" is a centered box.

### The Backend View
The `LoginView` doesn't know it's in a modal. It just renders `accounts/login.html`.

Unpoly fetches that page. Because we requested a *new layer*, Unpoly takes the response, strips out the `<body>` wrapper (mostly), and places the content into a dedicated modal container in the DOM.

## Stacking Layers
You can stack layers infinitely.
Page -> Modal (Login) -> Drawer (Terms of Service).

When you close a layer (`up-dismiss`), it destroys that specific DOM tree and returns focus to the layer below it.

## Closing on Success
This is the trickiest part of modal auth: **How do we close the modal and update the main page after login?**

In our `LoginView` form submission:

```html
<form method="post" up-submit up-target=".main-content" up-layer="root">
```

We added `up-layer="root"`. This tells Unpoly: *"When this form submits successfully, don't update the modal. Instead, update the ROOT layer (the background page)."*

By updating the Root layer, Unpoly automatically detects that it should close the modal layer to show the updated root. The result? A user logs in, the modal vanishes, and the header updates to say "Hello, User" seamlessly.
