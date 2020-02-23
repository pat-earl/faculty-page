<?php
require_once( 'SSOHelper.php' );

$sso = new SSOHelper();

// this should be the same in your code and in your Discourse settings:
// $secret = 'same secret set in discourse';
require_once( 'secret.php' ); # Sets $secret
$sso->setSecret( $secret );

// load the payload passed in by Discourse
$payload = $_GET['sso'];
$signature = $_GET['sig'];

// validate the payload
if (!($sso->validatePayload($payload, $signature))) {
    // invaild, deny
    header("HTTP/1.1 403 Forbidden");
    echo("Bad SSO request");
    die();
}

$nonce = $sso->getNonce($payload);

// Required and must be consistent with your application
$userEmail = getenv( 'eppn' );

// Required and must be unique to your application
$userId = strstr( $userEmail, '@', true );

// Optional - if you don't set these, Discourse will generate suggestions
// based on the email address
/* $extraParameters = array(
    'username' => $userUsername,
    'name'     => $userFullName
  ); */
$extraParameters = array();
$extraParameters['add_groups'] = 'trust_level_0,trust_level_1';
if( strpos( getenv('affiliation'), 'Faculty@andrew.cmu.edu' ) !== false )
  $extraParameters['add_groups'] .= 'trust_level_2';


// build query string and redirect back to the Discourse site
$query = $sso->getSignInString($nonce, $userId, $userEmail, $extraParameters );
header('Location: https://zym.math.cmu.edu/session/sso_login?' . $query);
exit(0);
?>
