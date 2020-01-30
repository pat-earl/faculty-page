{% raw -%}
window.MathJax = { 
    tex: {
	inlineMath: [ ['$','$'], ['\\(', '\\)']  ],
	// inlineMath: [ ['\\(', '\\)']  ],
	tagSide: "right",
	// equationNumbers: {autoNumber: "AMS"},
        tags: 'ams',
	macros: {
	    // RR: '{\\bf R}',
	    // bold: ['{\\bf #1}', 1]
	    eps:	'\\varepsilon',
	    suchthat:   '\\backepsilon',
	    st:		'\\mid',
	    dv:		'\\nabla\\cdot',
	    curl:	'\\nabla\\times',
	    defeq:	'\\stackrel{\\text{def}}{=}',

	    leq:	'\\leqslant',
	    geq:	'\\geqslant',
	    subset:	'\\subseteq',
	    supset:	'\\supseteq',

	    R:		'\\mathbb{R}',
	    C:	    	'\\mathbb{C}',
	    N:	    	'\\mathbb{N}',
	    Z:	    	'\\mathbb{Z}',
	    Q:	    	'\\mathbb{Q}',

	    lap:	'\\Delta',
	    laplacian:	'\\Delta',
	    inv:	'^{-1}',
	    transpose:	'^*',
	    grad:	'\\nabla',
	    gradt:	'\\grad\\transpose',
	    gradperp:	'\\grad^\\perp',
	    dlim:	'\\lim\\limits', // display style limits
	    dliminf:    '\\liminf\\limits',
	    dlimsup:    '\\limsup\\limits',
	    dlimto:	[ '\\dlim_{#1 \\to #2}', 2, 'x' ],
	    Perp:	'^\\perp',
	    dmax:	'\\max\\limits',
	    dmin:	'\\min\\limits',

	    cosec:	'\\operatorname{cosec}',
	    cosech:	'\\operatorname{cosech}',
	    sech:	'\\operatorname{sech}',
	    'var':	'\\operatorname{Var}',
	    im:		'\\operatorname{im}',
	    re:	    	'\\operatorname{re}',
	    rank:	'\\operatorname{rank}',
	    Span:	'\\operatorname{span}',
	    Ad:		'\\operatorname{adj}',
	    trace:	'\\operatorname{tr}',
	    erf:	'\\operatorname{erf}',
	    sign:	'\\operatorname{sign}',
	    supp:	'\\operatorname{supp}',
	    esssup:	'\\operatorname{ess\\,sup}\\limits',

	    abs:	[ '\\left\\lvert#1\\right\\rvert', 1 ],
	    norm:	[ '\\left\\lVert#1\\right\\rVert', 1 ],
	    ip:		[ '\\left\\langle#1,#2\\right\\rangle', 2 ],

	    setstar:    [ '\\left\\{#1\\right\\}', 1 ],
	    parenstar:  [ '\\left(#1\\right)', 1 ],
	    brakstar:   [ '\\left[#1\\right]', 1 ],
	    set:	[ '#1\\{#2#1\\}', 2, '' ],
	    paren:      [ '#1(#2#1)', 2, '' ],
	    brak:       [ '#1[#2#1]', 2, '' ]
	    // IE+compat doesn't like commas after the last item.
	}
    }
}
{%- endraw %}
