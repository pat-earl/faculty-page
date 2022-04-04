title: CSC273 - Lectures
breadcrumb: index.md

{% set lectures = (
    {"name": "Course Introduction", "file": "slides/introduction.md"},
    {"name": "Chapter 1 - SDLC", "file": "slides/chapter1.pdf"},
    {"name": "Chapter 2 - Origins of Software", "file": "slides/chapter2.pdf"},
    {"name": "Application Integration", "file": "slides/integration.md"},
    {"name": "Application Programming Interfaces", "file": "slides/api.md"},
    {"name": "Introduction to Microservices", "file": "slides/microservices.md"},
) %}

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor -%}


# Resources

- AWS PowerPoints are available in the *Student Guide* files for each module. Located on the AWS Academy website. 
- [Hoppscotch API Tools](https://hoppscotch.io/)
- [GO Rest API](https://gorest.co.in/)
- [JSONPlaceHolder](https://jsonplaceholder.typicode.com/guide/)