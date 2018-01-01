title: Setting up WordPress on your own server
tags: linux
summary: Tips I found useful when installing [WordPress](http://wordpress.org) on my own server.

Here are some useful tips I found when installing [WordPress](http://wordpress.org) on my own server.

## Installation

* Follow the [Debian installation guide](http://wiki.debian.org/WordPress)

* In `/etc/apache2/sites-available/wp`, make sure the Alias

        :::apache
        Alias /wp/wp-content /var/lib/wordpress/wp-content

    comes before

        :::apache
        Alias /wp /usr/share/wordpress

* In `/etc/wordpress/config-SITENAME.php` add

        :::php
        define('FORCE_SSL_ADMIN', true);

* If you bork the MySQL database accidentally, and need to fix things [install phpmyadmin](http://wiki.debian.org/LaMp).

* If you trust users and want to increase the file upload size, add this to `/etc/wordpress/htaccess`:

        :::apache
        php_value upload_max_filesize 20M
        php_value post_max_size 40M

## Useful Plugins

[Absolute Privacy](http://www.johnkolbert.com/portfolio/wp-plugins/absolute-privacy)
: Moderated user registrations, and only logged in users can access content.

[Peter's Login Redirect]
: Fix brain malfunction with WordPress design.
  Redirect users (esp. subscribers) to the blog after login, and not the admin page!

## Theme

I couldn't care less about colors or fancy images.
But I **WANTED** the main text to be more than 10 pixels wide, and the default blog text to be in a large font.
I found the [Customizr](http://www.themesandco.com/customizr/) theme, disabled the sliders / featured posts, and set the layout of all pages to only have a right sidebar.
Additionally, to get rid of the social icons (which are pretty useless for a private blog), I created a [child theme](http://www.themesandco.com/extension/customizr-child-theme/), and put the following in `style.css`:

```css
@media (min-width: 980px) {
  .tc-header .brand {
    float: none;
    text-align: center;
    width: 100%;
  }
  .tc-header .outside {
    display: block;
    text-align: center;
  }
}

/* Hide social icons */
.navbar-wrapper.clearfix.span9 {
  display: none;
}
```

For larger fonts in posts / etc. use the following in `style.css`:
```css
section.entry-summary, section.entry-content, article div.entry-content
{
  font-size: 16pt;
  line-height: 1.2em;
}
```

All my theme customizations are [here](http://wiki.math.cmu.edu/gitweb-pub/?p=customizr-child.git).

### Quirks

* Enable the theme's retina support (or you won't be able to edit images).

* Disable the theme's lightbox effects if you're using the different lightbox plugin.

[Peter's Login Redirect]: http://www.theblog.ca/wplogin-redirect

[Responsive Lightbox]: http://wordpress.org/plugins/responsive-lightbox/
