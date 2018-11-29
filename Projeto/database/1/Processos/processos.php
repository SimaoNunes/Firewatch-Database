<html>
    <head>
        <meta charset="UTF-8">
        <link rel="icon" type="image/png" href= "http://www.pngall.com/wp-content/uploads/2016/04/Database-PNG.png">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <title>Processos</title>
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
        </style>
    </head>
    <body>
        
        <div class="centered">
            <h3>Inserir Processo</h3>
            <form action='index.php' method='post'>
                <h6>Número: <input type='text' name='n'/></h6>
                <h6><input class="btn btn-success" type="submit" value="Submit"></h6>
            </form>
        </div>

        <?php 

        if(isset($_REQUEST['n'])){
            $novo_n = $_REQUEST['n'];    

            $host = "db.ist.utl.pt";
            $user ="ist186512";
            $password = "fico6299";
            $dbname = $user;

            $db = new PDO("pgsql:host=$host;dbname=$dbname", $user, $password);
            $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            $sql = "INSERT INTO local (processosocorro) VALUES (:novo_n);";

            $result = $db->prepare($sql);
            $result->execute([':novo_n'=> $novo_n]);

            $db = null;

            header("Refresh:0");
        }

        if(isset($_REQUEST['rem'])){
            $apagar = $_REQUEST['rem'];    

            $host = "db.ist.utl.pt";
            $user ="ist186512";
            $password = "fico6299";
            $dbname = $user;

            $db = new PDO("pgsql:host=$host;dbname=$dbname", $user, $password);
            $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            $sql = "DELETE FROM local WHERE precessosocorro = (:apagar);";

            $result = $db->prepare($sql);
            $result->execute([':apagar'=> $apagar]);

            $db = null;

            $newURL = 'locais.php';
            header('Location: '.$newURL);

        }
        ?>

        <div class="container">
            <table class="table col-md-6">
                <thead class="thead-dark">
                <tr>
                    <th scope="col">Número</th>
                    <th scope="col">Remover</th>
                </tr>
                </thead>
                <tbody>
                <?php

                $host = "db.ist.utl.pt";
                $user ="ist186512";
                $password = "fico6299";
                $dbname = $user;
            
                $db = new PDO("pgsql:host=$host;dbname=$dbname", $user, $password);
                $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
                $sql = "SELECT numprocessosocorro FROM processosocorro;";
                $result = $db->prepare($sql);
                $result->execute();

                foreach($result as $row)
                {
                    echo("<tr>");
                    echo("<td>");
                    echo($row['numprocessosocorro']);
                    echo("</td>");
                    echo("<td>");
                    echo("<a href='locais.php?rem={$row['numprocessosocorro']}'><img width='20' src='https://goo.gl/uJnJJD'>");
                    echo("</td>");
                    echo("<tr>");
                }
        
                $db = null;
                ?>
                </tbody>
                
            </table>
        </div>
            
    </body>
</html>
