{% if dev_env == "local" -%}
#! /usr/bin/php
Content-type: text/plain;
{% endif %}
<?php
  if( !is_array( $_SERVER ) || !array_key_exists( 'REQUEST_METHOD', $_SERVER )
      || $_SERVER['REQUEST_METHOD'] != 'POST')
     exit();
  
  function oneline( $s )
  {
    return str_replace( array( "\n", "\r" ), '', $s );
  }

  $name = oneline( $_POST['name'] );
  $email = oneline( $_POST['email'] );
  $subject = oneline( $_POST['subject'] );
  $page = oneline( $_POST['page'] );
  $date = strftime( '%F %T %Z' );
  $comment = $_POST['comment']; // Newlines are allowed here.

  $body = '';
  $body .= "page: $page\n";
  $body .= "subject: $subject\n";
  $body .= "name: $name\n";
  $body .= "email: $email\n";
  $body .= "date: $date\n";
  $body .= "referer: $HTTP_REFERER\n";
  $body .= "ip: $HTTP_ADDR\n";
  $body .= "\n$comment";

  {% if dev_env == 'local' %}
    print( "[$page]: $subject\n$body\n" );
    phpinfo();
  {% else %}
    if ( mail( 'gautam@math.cmu.edu', "[$page]: $subject", $body,
      "From: Blog <gautam@math.cmu.edu>" ) )
    {
      echo( "Success" );
    }
    else {
      echo( "Failed" );
    }
  {% endif %}
?>
