#!/usr/bin/perl  -w

#include libraries
use DBI;
use  CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);

#definition of variables
$db="emp";
$host="localhost";
$user="root";
$password="Tulsi@991";
my $name = "Al Bento";

#connect to MySQL database
my $dbh   = DBI->connect ("DBI:mysql:database=$db:host=$host",
                                        $user,
                                        $password) 
                                       or die "Can't connect to database: $DBI::errstr\n";

#convert the quoted Perl value to DBI quoted Perl 
my $qname = $dbh->quote( $name);

#prepare the query
my $sth = $dbh->prepare( "
              SELECT * 
              FROM emptbl WHERE empno =$qname");

#execute the query
$sth->execute( );

# Prepare HTML headers 
print header, start_html (-title=>"Content of Table people",-bgcolor=>'white');
print "<H1>Content of Table people</H1>\n";
print "<TABLE border=1>\n";
print "<TR><TH> Name</TH>><TH>Address</TH>\n";

## Retrieve the results of a row of data and  send to browser

while ( ($name,$address) = $sth->fetchrow_array( ) )  {
        print "<tr><td>$name</td><td>$address</td></tr>\n";
}

#end the HTML
print "</table></body></html>\n";

#end program
$sth->finish( );
$dbh->disconnect( );
exit;
