<html>
    <body>
        <h3>Change balance for account <?=$_REQUEST['account_number']?></h3>
        <form action="update.php" method="post">
            <p><input type="hidden" name="account_number" value="<?=$_REQUEST['account_number']?>"/></p>
            <p>New balance: <input type="text" name="balance"/></p>
            <p><input type="submit" value="Submit"/></p>
        </form>
    </body>
</html>
