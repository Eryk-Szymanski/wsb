<?php
    session_start();
    if (isset($_POST)) {
        foreach ($_POST as $value) {
            if (empty($value)) {
                header('location: ../5_table_update_insert_delete.php');
                exit();
            }
        }
        require_once('./connect.php');
        $sql="UPDATE `users` SET `city_id` = '$_POST[city_id]', `name` = '$_POST[name]', `surname` = '$_POST[surname]' WHERE `users`.`id` = $_SESSION[updateid]";
        $conn->query($sql);
        if ($conn->affected_rows) {
            $_SESSION['info'] = "Prawidłowo zaktualizowano rekord";
        } else {
            $_SESSION['info'] = "Nie zaktualizowano rekordu";
        }
    }
    header('location: ../5_table_update_insert_delete.php')
?>