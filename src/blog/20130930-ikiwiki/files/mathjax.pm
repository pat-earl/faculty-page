#!/usr/bin/perl
# Created   : Fri 04 Oct 2013 01:19:02 PM EDT
# Modified  : Sat 05 Oct 2013 11:58:52 AM EDT
# Author    : GI <a@b.c>, where a='gi1242+perl', b='gmail', c='com'
#
# Allows adding the MathJAX scripts via a tag.
# 
# The directive [[!mathjax]] will add the MathJAX script from CDN. By default
# it will look for a config file in /javascript/mathjax-config.js. If you want
# to include config in a different location do so via the config parameter. E.g.
#
#   [[!mathjax config="myconfig"]]
#
# Your config file can also contain latex macros. (External scripts can not be
# linked to using the config parameter.)
#
# Only one config file per invocation is supported. If you inline two pages
# each sourcing a different config file, then only the config from the last one
# inlined will be included.

package IkiWiki::Plugin::mathjax;

use warnings;
use strict;
use IkiWiki 3.00;

my %mathjax_config; # Disable by default.

sub import {
    hook(type => "preprocess", id => "mathjax", call => \&preprocess);
    hook(type => "format", id => "mathjax", call => \&format);
}

sub preprocess(@)
{
    my %params=@_;
    my $page = $params{destpage};

    my $config_file = exists( $params{config} ) ? 
	$params{config} : "/javascript/mathjax-config";
    my $js = bestlink( $page, "$config_file.js" );

    if ( length( $js ) ) {
	$mathjax_config{$page} = urlto( $js, $page );
    }
    else {
	if( exists( $params{config} ) ) {
	    error( "$params{config}.js: " . gettext( "script not found" ) );
	}
	else {
	    # No config param, and default config not found.
	    # Include MathJAX with no config.
	    $mathjax_config{$page} = "NONE";
	}
    }

    return ""; #Directive produces no output.
}

sub format (@) {
    my %params=@_;

    my $page = $params{page};
    if( exists( $mathjax_config{$page} ) )
    {
	# Add MathJAX config at the end of the head section.
	my $cdn_url = ( defined $config{url} && $config{url}=~/^https:/ ) ? "https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js?config=TeX-AMS_HTML" : "http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML";

	my $script_tag = "\n<script src='$cdn_url' type='text/javascript'>"
	    . "</script>\n";
	if ( $mathjax_config{$page} ne "NONE" ) {
	    $script_tag .= "<script src='$mathjax_config{$page}' "
	    . "type='text/javascript'></script>\n";
	}

	if (! ($params{content}=~s!^(<body[^>]*>)!$1.$script_tag!em)) {
	    # no <body> tag, probably in preview mode
	    $params{content}=$script_tag.$params{content};
	}
    }

    return $params{content};
}

1;
