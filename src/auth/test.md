title: test

## CGI Output

<pre id='form-output'></pre>

<script>
  window.addEventListener('DOMContentLoaded', function() {
      $.get( "{{get_link('/cgi-bin/auth/test.py')}}",
          '{{dirname}}/grades.csv',
          function(data) {
              $('#form-output').text(data);
          }
      );
    });
</script>
