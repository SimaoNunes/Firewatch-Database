<html>
    <head>
        <meta charset="utf-8">
        <link rel="icon" type="image/png" href= "http://www.pngall.com/wp-content/uploads/2016/04/Database-PNG.png">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <title>Base de Dados</title>
        <style>
        </style> 
    </head>
    <body>
    <h3>Cameras</h3>
    <?php
        try
        {
            $host = "db.ist.utl.pt";
            $user ="ist186512";
            $password = "fico6299";
            $dbname = $user;
        
            $db = new PDO("pgsql:host=$host;dbname=$dbname", $user, $password);
            $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
            $sql = "SELECT numcamara FROM camara;";
        
            $result = $db->prepare($sql);
            $result->execute();
        
            echo("<table border=\"0\" cellspacing=\"5\">\n");
            
            foreach($result as $row){
                echo("<tr>\n");
                echo("<td>{$row['numcamara']}</td>\n");
                echo("</tr>\n");
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
        
