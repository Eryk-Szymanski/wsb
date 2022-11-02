<?php
    session_start();
    if (!empty($_POST)) {
        require_once('./connect.php');
        $sql="INSERT INTO `users` (`id`, `city_id`, `name`, `surname`, `created_at`) VALUES (NULL, '1', 'eryk', 'szymanski', current_timestamp());";
        $conn->query($sql);
        if ($conn->affected_rows) {
            // echo "ok: $conn->affected_rows";
            $_SESSION['info'] = "Prawidłowo usunięto rekord o id=$_GET[userid]";
        } else {
            // echo "error $conn->affected_rows";
            $_SESSION['info'] = "Nie usunięto rekordu o id=$_GET[userid]";
        }
    } else {

    }
    header('location: ../4_table__insert_delete.php')
?>