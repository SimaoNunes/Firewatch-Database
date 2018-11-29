<html>
    <body>
<?php
    try
    {
        $host = "db.ist.utl.pt";
        $user ="istxxxxx";
        $password = "xxxxxxx";
        $dbname = $user;
        
        
        $db = new PDO("pgsql:host=$host;dbname=$dbname", $user, $password);
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
        $sql = "SELECT account_number, branch_name, balance FROM account;";
        $result = $db->prepare($sql);
        $result->execute();
           
        echo("<table border=\"1\">\n");
        echo("<tr><td>account_number</td><td>branch_name</td><td>balance</td></tr>\n");
        foreach($result as $row)
        {
            echo("<tr><td>");
            echo($row['account_number']);
            echo("</td><td>");
            echo($row['branch_name']);
            echo("</td><td>");
            echo($row['balance']);
            echo("</td></tr>\n");
        }
        echo("</table>\n");
    
        $db = null;
    }
    catch (PDOException $e)
    {
        echo("<p>ERROR: {$e->getMessage()}</p>");
    }
?>
    </body>
</html>
