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
   * and don't worry about offsets or widths. (Affix is also disabled if the
   * element is too tall.)
   */
  $('[data-affix-after]').each( function() {
      var elem = $(this);
      var prev = $( elem.data('affix-after') );
      var parent_panel = elem.parent();

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

	  /* Set affix offset to bottom of the previous element */
	  elem.data('bs.affix').options.offset
	      = prev.offset().top + prev.outerHeight(true);

	  /* Disable affix behaviour if element is too tall. */
	  elem.css( 'position',
	      (elem.height() > $(window).height() - 20) ? 'static' : '' );

	  /* Make sure position is consistent */
	  elem.affix( 'checkPosition' );
      };

      elem.affix();
      resizeFn();
      $(window).resize(resizeFn);
  });

}); /* end ready */
