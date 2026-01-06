# Building Page Less: Part 7 - CRUD without Chaos

Creating, Reading, Updating, and Deleting (CRUD). The bread and butter of web apps.

## The Delete UX Problem
Deleting items usually requires a confirmation step.
-   **Old School**: A separate page "Are you sure?".
-   **Old School JS**: A generic `window.confirm()` alert.
-   **Page_Less Way**: A nice confirmation Modal that handles the deletion and redirects gracefully.

## Custom Delete Modal
We use a standard Django `DeleteView`.

```python
class PostDeleteView(DeleteView):
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")
```

In the template `post_detail.html`:
```html
<a href="..." up-layer="new" up-mode="modal" up-size="small">Delete</a>
```

This opens the confirmation page in a small, localized modal.

## Handling the Redirect
When the user clicks "Confirm Delete" inside the modal:

```html
<form method="post" up-submit up-target="body" up-layer="root">
```

We target `body` on the `root` layer.
Why?
If we just targeted `.main-content`, the modal might stay open, or we might end up with the list view rendering *inside* the modal.

By saying `up-layer="root"`, we tell Unpoly: *"The result of this action affects the entire application state. Close this modal and refresh the underlying page."*

## Flash Messages
Django's `messages` framework is fantastic, but it relies on a new page render to display alerts.

Because Unpoly swaps fragments, we need to ensure the message container is included in the swap.

In `base.html`, our messages are inside `.main-content`.
When we `up-target=".main-content"`, the messages block is re-rendered automatically. We get green success banners for free, with no extra JavaScript code to "toast" them.

For the **Delete** action specifically, since we target `body`, the entire page refreshes, guaranteeing the message appears at the top.

---
**[← Part 6: Instant Search](./06_search.md) | [Part 8: Conclusion & UI Polish](./08_conclusion.md) →**
