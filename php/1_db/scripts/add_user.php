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
        $sql="INSERT INTO `users` (`id`, `city_id`, `name`, `surname`, `created_at`) VALUES (NULL, '$_POST[city_id]', '$_POST[name]', '$_POST[surname]', current_timestamp());";
        $conn->query($sql);
        if ($conn->affected_rows) {
            $_SESSION['info'] = "Prawidłowo dodano rekord";
        } else {
            $_SESSION['info'] = "Nie dodano rekordu";
        }
    }
    header('location: ../5_table_update_insert_delete.php')
?>