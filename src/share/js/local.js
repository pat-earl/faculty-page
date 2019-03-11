'use strict';

$(document).ready( function() {
  /* Easy Bootstrap affix. Simply do:
   *
   *	<div id='before-affix'></div>
   *	<div data-affix-after='#before-affix'>
   *	    Content to affix
   *	</div>
   *
   * and don't worry about offsets or widths or being too tall.
   *
   * CSS to enable: .affix { top: 0px }, .affix-bottom { position: absolute; }
   * CSS to disable: .affix, .affix-bottom { position: static; }
   */
  $('[data-affix-after]').each( function() {
    var elem = $(this);
    var parent_panel = elem.parent();
    var prev = $( elem.data('affix-after') );

    function resizeFn() {
      /* Set the width to it's natural width in the parent. */
      var sideBarNavWidth = parent_panel.width()
	- parseInt(elem.css('paddingLeft'))
	- parseInt(elem.css('paddingRight'))
	- parseInt(elem.css('marginLeft'))
	- parseInt(elem.css('marginRight'))
	- parseInt(elem.css('borderLeftWidth'))
	- parseInt(elem.css('borderRightWidth'));
      elem.css('width', sideBarNavWidth);

      elem.affix({
	offset: {
	  top: prev.offset().top + prev.outerHeight(true),
	  bottom: $('body>footer').outerHeight(true)
	}
      });

      elem.affix( 'checkPosition' );
    }

    if( prev.length != 1 )
      /* Create a new element immediately before. */
      prev = elem.before( '<div></div>' ).prev();

    resizeFn();
    $(window).resize(resizeFn);

    $('[data-spy~="scroll"]').each( function() {
      $(this).on('activate.bs.scrollspy', function() {
	elem.affix( 'checkPosition' );
      });
    });
  }); /* end $('[data-affix-after]') */
}); /* end ready */

function submit_comment() {
  function failfn(data) {
    $('#comment-form,#comment-sending').addClass('hidden');
    $('#comment-failed,#comment-form').removeClass( 'hidden' );
    {% if dev_env == 'local' %}
    $('#comment-failed').append('<pre>' + data + '</pre>');
    {% endif %}
  }

  $('#comment-failed,#comment-form,#comment-success').addClass('hidden');
  $('#comment-sending').removeClass( 'hidden' );

  $.post( "{{get_link('/cgi-bin/comment.py')}}",
      $('#comment-form > form').serializeArray() )
    .done( function( data ) {
	if( data.trim() == "OK" ) {
	  $('#comment-failed,#comment-form,#comment-sending')
	    .addClass('hidden');
	  $('#comment-success').removeClass( 'hidden' );
	}
	else failfn(data);
      }
    )
    .fail( failfn );
}

function get_grades(fname, show_stats=true, show_total=true) {
  function failfn( msg ) {
    $('#status')
      .attr( 'class', 'alert alert-danger' )
      .text( 'Sorry, an error occurred.' );
    {%- if dev_env == 'local' %}
      $('#status').append( ' Error: ' + 
	(typeof(msg) === 'object' && msg.hasOwnProperty('statusText') ?
	  msg.statusText : msg ));
      /* For debugging */
      get_grades.errMsg = msg;
    {%- endif -%}
  }

  $.getJSON( "{{get_link('/cgi-bin/auth/getgrades.py')}}",
    { filename: fname, show_stats: show_stats, show_total: show_total },
    function(data) {
	var table = $('#scores');
	var thead = $('<thead><tr><th></th></tr></thead>').appendTo(table)
	  .children();
	var tbody = $('<tbody></tbody>').appendTo(table);

	{% if dev_env == 'local' -%}
	/* Save for debugging */
	get_grades.data = data;
	{% endif -%}

	if( data.hasOwnProperty('error') )
	  failfn( data.error );
	else {
	  $('#status').addClass( 'hidden' );

	  if( data.name )
	    $('#student-name').text(data.name).wrap('<strong></strong>');
	  else
	    $('#status')
	      .attr( 'class', 'alert alert-warning' )
	      .text( 'Your scores were not found!' );

	  // for( let c of data.cols ) throws an error in IE
	  for ( let i=0; i < data.cols.length; i++ ) {
	      thead.append( '<th>' + data.cols[i][0] + '</th>' );
	      /* console.log( '<td>' + c[0] + '</td>' ); */
	  };

	  for ( let i=0; i < data.rows.length; i++ ) {
	    let tr = $('<tr></tr>').appendTo(tbody);

	    tr.append('<th>' + data.rows[i] + '</th>' );
	    for( let j=0; j < data.cols.length; j++ )
	      tr.append( '<td>' + data.cols[j][i+1] + '</td>' );
	  }

	  /* $('#form-output').text(JSON.stringify(data, null, 2)); */
	}
      }
    ) /* getJSON */
  .fail(failfn)
  ;
}
