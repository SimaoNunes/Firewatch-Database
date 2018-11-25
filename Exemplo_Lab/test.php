<html>
<body>
<?php
	$user="ist186512";		// -> replace by the user name
	$host="db.ist.utl.pt";	        // -> server where postgres is running
	$port=5432;			// -> default port where Postgres is installed
	$password="nacREH7641";	        // -> replace with the passoword
	$dbname = $user;		// -> by default the name of the database is the name of the user
	
	$connection = pg_connect("host=$host port=$port user=$user password=$password dbname=$dbname") or die(pg_last_error());
	
	echo("<p>Connected to Postgres on $host as user $user on database $dbname.</p>");
	
	$sql = "SELECT * FROM account;";

	echo($sql);

	$result = pg_query($sql) or die('ERROR: ' . pg_last_error());
	
	$num = pg_num_rows($result);

	echo("<p>$num records retrieved:</p>");

	echo('<table border="5">');
	echo("<tr><td>account_number</td><td>branch_name</td><td>balance</td></tr>");
	while ($row = pg_fetch_assoc($result))
	{
		echo("<tr><td>");
		echo($row["account_number"]);
		echo("</td><td>");
		echo($row["branch_name"]);
		echo("</td><td>");
		echo($row["balance"]);
		echo("</td></tr>");
	}
	echo("</table>");
		
	$result = pg_free_result($result) or die('ERROR: ' . pg_last_error());
	
	echo("<p>Query result freed.</p>");
	
	pg_close($connection);
	
	echo("<p>Connection closed.</p>");

	echo("<p>Test completed successfully.</p>");
	
?>
</body>
</html>
