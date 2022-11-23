<?php
    $error = 0;
    foreach ($_POST as $key => $value) {
        if (empty($value)) {
            $error = 1;
        }
    }

    if (!isset($_POST['agreeTerms'])) {
        $error = 1;
    }

    if($error == 1) {
        echo "<script>history.back();</script>";
        exit();
    }

    require_once 'connect.php';

    $stmt = $mysqli->prepare("INSERT INTO users(city_id, name, surname, email, pass, birthday) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("isssss", $_POST['city_id'], $_POST['name'], $_POST['surname'], $_POST['email1'], $_POST['pass1'], $_POST['birthday']);
    $stmt->execute();
?>