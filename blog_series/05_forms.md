# Building Page Less: Part 5 - Forms & Validation

Form handling in SPAs is notoriously tedious. You have to serialize data, prevent default, handle the fetch, catch 400 errors, parse the JSON errors, and manually map them back to input fields.

Unpoly restores the simplicity of Django Forms.

## Server-Side Validation, Client-Side Feel
In **Page_Less**, when you create a post, we use the standard `PostForm`.

```html
<form method="post" up-submit up-validate=".form-group">
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
```

### The `up-submit` flow:
1.  Unpoly serializes the form.
2.  Submits via AJAX (POST).
3.  **If the server returns 200 (Success):** It updates the target (e.g., redirects to the detail view).
4.  **If the server returns 400 (Bad Request):**
    -   Django re-renders the template with `form.errors`.
    -   Unpoly sees the non-200 status code (we need to ensure Django sends 400 on form errors, or Unpoly can detect the form re-render presence).
    -   Unpoly intelligently swaps the form HTML with the new HTML containing errors.

## `up-fail-target`
Sometimes, success and failure should look different.

```html
<form method="post" 
      up-target=".main-content" 
      up-fail-target=".card-body">
```

-   **Success**: We probably redirect to a new page, so we update `.main-content`.
-   **Failure**: We stay in the form. We only want to re-render the `.card-body` (the form container) to show errors, keeping the surrounding layout untouched.

## Live Validation (`up-validate`)
Unpoly can validate fields *while you type*, using the server!

```html
<input name="username" up-validate=".username-errors">
```

When the user blurs this field, Unpoly sends a request to the server with *just* that field's data. The server runs its validation logic (e.g., "Username already taken") and returns the response. Unpoly extracts the `.username-errors` div and updates the UI.

This gives you real-time server-side validation with zero custom API endpoints. You just use your regular Form View.

---
**[← Part 4: Modal Magic & Layers](./04_modals.md) | [Part 6: Instant Search](./06_search.md) →**
