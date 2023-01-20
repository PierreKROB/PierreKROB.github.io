<!DOCTYPE html>
<html>
<head>
    <title>Create JSON File</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <form method="post">
        <input type="submit" name="create_json" value="Create JSON File">
    </form>
    <?php
    if(isset($_POST['create_json'])) {
        $output = shell_exec('python create_json.py');
        echo "<pre>$output</pre>";
    }
    ?>
</body>
</html>
