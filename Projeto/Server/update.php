<html>
    <body>
<?php
    $account_number = $_REQUEST['account_number'];
    $balance = $_REQUEST['balance'];
    try
    {
        $host = "db.ist.utl.pt";
        $user ="istxxxxx";
        $password = "xxxxxxx";
        $dbname = $user;
        $db = new PDO("pgsql:host=$host;dbname=$dbname", $user, $password);
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        $sql = "UPDATE account SET balance = :balance WHERE account_number = :account_number;";
        echo("<p>$sql</p>");

        $result = $db->prepare($sql);
        $result->execute([':balance' => $balance, ':account_number' => $account_number]);
        
        $db = null;
    }
    catch (PDOException $e)
    {
        echo("<p>ERROR: {$e->getMessage()}</p>");
    }
?>
    </body>
</html>
