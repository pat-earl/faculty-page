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

      if( prev.length != 1 ) {
	/* Create a new element immediately before. */
	prev = elem.before( '<div></div>' ).prev();
      }

      var resizeFn = function() {
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
      };

      resizeFn();
      $(window).resize(resizeFn);

      $('[data-spy~="scroll"]').each( function() {
	$(this).on('activate.bs.scrollspy', function() {
	  elem.affix( 'checkPosition' );
	});
      });
  });

}); /* end ready */

function submit_comment() {
  $('#comment-failed,#comment-form,#comment-success').addClass('hidden');
  $('#comment-sending').removeClass( 'hidden' );

  var failfn = function(data) {
    $('#comment-form,#comment-sending').addClass('hidden');
    $('#comment-failed,#comment-form').removeClass( 'hidden' );
    {% if dev_env == 'local' %}
    $('#comment-failed').append('<pre>' + data + '</pre>');
    {% endif %}
  };

  $.post( "{{get_link('/cgi-bin/comment.py')}}",
      $('#comment-form > form').serializeArray() )
    .done( function( data ) {
	if( data.trim() == "OK" ) {
	  $('#comment-failed,#comment-form,#comment-sending').addClass('hidden');
	  $('#comment-success').removeClass( 'hidden' );
	}
	else failfn(data);
      }
    )
    .fail( failfn );
}
