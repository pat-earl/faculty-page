$(document).ready( function() {
  /*
  * Clamped-width. 
  * Usage:
  *  <div data-clampedwidth=".myParent">This long content will force clamped
  *  width</div>
  *
  * Author: LV
  */
  $('[data-clampedwidth]').each(function () {
      var elem = $(this);
      var parentPanel = elem.data('clampedwidth');
      var resizeFn = function () {
	  var sideBarNavWidth = $(parentPanel).width()
	      - parseInt(elem.css('paddingLeft'))
	      - parseInt(elem.css('paddingRight'))
	      - parseInt(elem.css('marginLeft'))
	      - parseInt(elem.css('marginRight'))
	      - parseInt(elem.css('borderLeftWidth'))
	      - parseInt(elem.css('borderRightWidth'));
	  elem.css('width', sideBarNavWidth);
      };

      resizeFn();
      $(window).resize(resizeFn);
  });


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
      };

      resizeFn();
      $(window).resize(resizeFn);
  });

}); /* end ready */
