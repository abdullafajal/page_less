# Part 6: Instant Search

Search is a feature where users expect instant feedback. In a traditional Django app, hitting "Search" triggers a full page reload, which feels clunky.

In **Page_Less**, we implemented a live search that filters results as you type.

## The Code
The implementation is shockingly simple. It lives in `post_list.html`.

```html
<form action="{% url 'blog:post_list' %}" 
      method="get" 
      up-target=".post-list" 
      up-delay="200" 
      up-autosubmit>
    
    <input type="search" name="q" value="{{ request.GET.q }}">
</form>

<div class="post-list">
    {% for post in posts %}
        ...
    {% endfor %}
</div>
```

## Breakdown
1.  **`up-autosubmit`**: Tells Unpoly to submit the form whenever an input field triggers a `change` or `input` event.
2.  **`up-delay="200"`**: Debounces the input. It waits 200ms after the user stops typing before sending the request, preventing server hammer.
3.  **`up-target=".post-list"`**: When the response comes back, Unpoly looks for the `<div class="post-list">` in the returned HTML and replaces *only that div*.

## The Backend
The backend is completely standard logic:

```python
class PostListView(ListView):
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
             return Post.objects.filter(title__icontains=query)
        return Post.objects.all()
```

That's it. No JSON API. No specialized "Search View". The same view that renders the full page also powers the live search fragment.

This pattern is incredibly powerful for filters, sorting, and pagination.
