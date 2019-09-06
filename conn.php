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
         $conn = mysqli_connect($dbhost,$dbuser,$dbpass,$dbdata);
         if(!$conn ) {
            die('Could not connect: ' . mysqli_connect_error());
         }
         echo 'Connected successfully';
         mysqli_close($conn);
      ?>
   </body>
</html>
