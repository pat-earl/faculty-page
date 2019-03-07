{%- from get_file('../course_info.j2') import course -%}
title: Your Grades
breadcrumb: ../|{{course.title}}

<script>
  window.addEventListener('DOMContentLoaded', function() {
    get_grades('{{dirname}}/grades.csv');
  });
</script>
<div id='status' class='alert alert-info' role='alert'>
  Loading...
</div>

Hi <span id='student-name'>there</span>.
Here are all the grades / scores I have on record for you, along with the averages.

<table class='table' id='scores'>
  <thead><tr><th></th></tr></thead>
  <tbody></tbody>
</table>
{#-
## CGI Output
<pre id='form-output'></pre>
-#}
