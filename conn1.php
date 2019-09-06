<html>
   <head>
      <title>Connecting MySQL Server</title>
   </head>
   <body>
      <?php
	$dbhost = 'localhost';
	$dbuser = 'root';
	$dbpass = 'Tulsi@991';
	$dbdata = 'searchdb';
	try {
		if ($db = mysqli_connect($dbhost, $dbuser, $dbpass, $dbdata)) {
			//do something
		}
		else {
			throw new Exception('Unable to connect');
		}
	}
	catch(Exception $e) {
		echo $e->getMessage();
    	}
     ?>
   </body>
</html>
