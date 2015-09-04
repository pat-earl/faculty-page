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


  /* Easy affix:
   *
   *	<div id='before-affix'></div>
   *	<div data-affix-after='#before-affix'>
   *	    Content to affix
   *	</div>
   *
   * and don't worry about offsets or widths.
   */
  $('[data-affix-after]').each( function() {
      var elem = $(this);
      var prev = $( elem.data('affix-after') );
      var parent_panel = elem.parent();

      var resizeFn = function() {
	  elem.data('bs.affix').options.offset
	      = prev.offset().top + prev.outerHeight(true);

	  elem.affix( 'checkPosition' );

	  var sideBarNavWidth = parent_panel.width()
	      - parseInt(elem.css('paddingLeft'))
	      - parseInt(elem.css('paddingRight'))
	      - parseInt(elem.css('marginLeft'))
	      - parseInt(elem.css('marginRight'))
	      - parseInt(elem.css('borderLeftWidth'))
	      - parseInt(elem.css('borderRightWidth'));
	  elem.css('width', sideBarNavWidth);
      };

      elem.affix();
      resizeFn();
      $(window).resize(resizeFn);
  });

}); /* end ready */
