# Task 3: Blog with Tag Filtering
#### Objective:
Create a simple blog system where each blog post can have multiple tags. The user should be able to filter blog posts by selecting a tag.

#### Requirements:
1. Models: You are provided with the following models:
    - BlogPost:
        - **Title**: The title of the blog post (string).
        - **Content**: The content of the blog post (text).
        - **Published** Date: The date the post was published (auto-generated).
    - Tag:
        - **Name**: The name of the tag (string).
        - **Posts**: A many-to-many relationship between `Tag` and `BlogPost`.
2. View:
    - Implement a view that:
        - Displays all blog posts by default.
        - Filters the blog posts by a selected tag if a `tag_id` is provided in the query string.
    - Pass the list of tags to the template to allow users to filter blog posts by tag.
3. Template:
    - Create a template that displays:
        - A list of tags that can be clicked to filter blog posts.
        - A list of blog posts, including their titles, content, published dates, and associated tags.
#### Deliverables:
- A working `models.py`, `views.py`, and `blog_list.html` template that implements the tag filtering.