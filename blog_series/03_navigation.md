# Building Page Less: Part 3 - Turbocharging Navigation

Now that we have the base setup, let's look at how we handle navigation in **Page_Less**.

## The `up-target` Attribute
The most common Unpoly attribute you will use is `up-target`.

```html
<a href="/blog/post-1" up-target=".main-content">Read Post</a>
```

When clicked:
1.  Unpoly intercepts the click (preventing full browser reload).
2.  It uses `fetch` to get `/blog/post-1`.
3.  Changes the browser URL (pushState).
4.  Swaps the inner HTML of `.main-content` with the content from the server response.

## Animation & Transitions
One major advantage of SPAs is the ability to animate between pages. Unpoly makes this trivial with `up-transition`.

```html
<a href="..." up-target=".main-content" up-transition="move-left">
    Next Page
</a>
```

In our **Post List** view, we use this for pagination:

```html
<!-- post_list.html -->
<a class="page-link" href="?page=2" up-target=".post-list" up-transition="cross-fade">
    Next
</a>
```

Notice we target `.post-list` instead of `.main-content`. This is granular updates in action. The sidebar (Search widget) doesn't flicker or reload; only the list of posts fades out and the new list fades in.

## Active State Management
A classic pain point in MPAs is highlighting the current nav item.

Unpoly handles this automatically with the `up-alias` attribute or by simple URL matching. If the current URL matches the link's href, Unpoly adds an `.up-current` class to the link.

In our CSS:
```css
.nav-link.up-current {
    color: var(--md-sys-color-primary);
    font-weight: bold;
}
```

No template logic (`{% if request.path == ... %}`) required!

---
**[← Part 2: Setting the Foundation](./02_setup.md) | [Part 4: Modal Magic & Layers](./04_modals.md) →**
