<?php
    session_start();
    if (!empty($_GET['userid'])) {
        // echo $_GET['userid'];
        require_once('./connect.php');
        $sql="DELETE FROM users WHERE `users`.`id` = $_GET[userid]";
        // $sql="DELETE FROM users WHERE `users`.`id` = 2";
        $conn->query($sql);
        if ($conn->affected_rows) {
            // echo "ok: $conn->affected_rows";
            $_SESSION['info'] = "Prawidłowo usunięto rekord o id=$_GET[userid]";
        } else {
            // echo "error $conn->affected_rows";
            $_SESSION['info'] = "Nie usunięto rekordu o id=$_GET[userid]";
        }
    }
    header('location: ../4_table__insert_delete.php')
?>