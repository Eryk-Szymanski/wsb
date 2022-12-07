<!DOCTYPE html>
<html lang="pl" dir="Itr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="./styles/style.css">
    <title>Użytkownicy</title>
  </head>
  <body>
    <h3>Użytkownicy z tabeli users</h3>
    <table>
      <tr>
        <th>Imię i nazwisko</th>
        <th>Miasto</th>
        <th>Data utworzenia konta</th>
      </tr>
    <?php
      require_once('./scripts/connect.php');
      $sql = "SELECT * FROM `users` INNER JOIN `cities` ON `users`.`city_id`=`cities`.id;";
      $result = $conn->query($sql);
      while ($user = $result->fetch_assoc()) {
        echo <<< E
        <tr>
          <td>$user[name] $user[surname]</td>
          <td>$user[city]</td>
          <td>$user[created_at]</td>
        </tr>
E;
      }
     ?>
    </table>
   </body>
 </html>
