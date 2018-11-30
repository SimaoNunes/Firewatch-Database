<html>
    <head>
        <meta charset="UTF-8">
        <link rel="icon" type="image/png" href= "http://www.pngall.com/wp-content/uploads/2016/04/Database-PNG.png">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <title>Meios Apoio</title>
        <style>
            body{
                background-color: #474747;
            }
            h3{
                color: white;
                text-align: center;
            }
            h6{
                color: white;
                text-align: center;
                margin-left: 130;
                margin-right: 130;
            }
            img{
                cursor: pointer;
            }
            a{
                margin: 1;
            }
            table{
                color: white;
                margin: 0 auto;
            }
            .centered{
                margin: 20 auto;
            }
            .leftie{
                margin: 10 10;
            }
        </style>
    </head>
    <body>
        
        <div class="leftie">
            <a href='..'><button type="button" class="btn btn-primary">Back</button></a>
        </div>

        <div class="centered">
            <h3>Listar Meios</h3>
            <form action='accionados.php' method='post'>
                <h6>Nº Processo Socorro: <input type='number' name='n' min='0' required='required'/></h6>
                <h6><input class="btn btn-success" type="submit" value="Submit"/></h6>
            </form>
        </div>

        <?php 

        if(isset($_REQUEST['n'])){

            $n = $_REQUEST['n'];

            echo("<div class='container'>
                <table class='table col-md-8'>
                <thead class='thead-dark'>
                <tr>
                    <th style='text-align:center' scope='col'>Nº Meio</th>
                    <th style='text-align:center' scope='col'>Entidade</th>
                    <th style='text-align:center' scope='col'>Nº Processo</th>
                </tr>
                </thead>
                <tbody>");

                $host = 'db.ist.utl.pt';
                $user ="ist186512";
                $password = "fico6299";
                $dbname = $user;
            
                $db = new PDO("pgsql:host=$host;dbname=$dbname", $user, $password);
                $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
                $sql = "SELECT * FROM acciona WHERE numprocessosocorro = :n;";
                $result = $db->prepare($sql);
                $result->execute([':n' => $n]);

                foreach($result as $row)
                {
                    echo("<tr>");
                    echo("<td style='text-align:center'>");
                    echo($row['nummeio']);
                    echo("</td>");
                    echo("<td style='text-align:center'>");
                    echo($row['nomeentidade']);
                    echo("</td>");
                    echo("<td style='text-align:center'>");
                    echo($row['numprocessosocorro']);
                    echo("</td>");
                    echo("<tr>");
                }
        
                $db = null;
                
                echo("</tbody>
                
            </table>
        </div>");
        }
        

        ?>
     
            
    </body>
</html>
