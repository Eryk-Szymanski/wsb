<?php
  $conn = new mysqli("localhost", "root", "", "project");
  echo "<hr>";
  echo $conn->connect_errno;
?>
