<?php
  session_start();
?>
<!DOCTYPE html>
<html lang="pl" dir="Itr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="./styles/style.css">
    <title>Użytkownicy</title>
  </head>
  <body>
    <h3>Użytkownicy z tabeli users</h3>
  <!-- komunikaty -->
    <?php
      if (isset($_SESSION['info'])) {
        echo $_SESSION['info'];
        unset($_SESSION['info']);
      }
    ?>
    <table>
      <tr>
        <th>Imię i nazwisko</th>
        <th>Miasto</th>
        <th>Data utworzenia konta</th>
      </tr>
    <?php
      require_once('./scripts/connect.php');
      $sql = "SELECT `users`.`id`, `users`.`name`, `users`.`surname`, `users`.`created_at`, `cities`.`city` FROM `users` INNER JOIN `cities` ON `users`.`city_id`=`cities`.id;";
      $result = $conn->query($sql);
      while ($user = $result->fetch_assoc()) {
        echo <<< E
        <tr>
          <td>$user[name] $user[surname]</td>
          <td>$user[city]</td>
          <td>$user[created_at]</td>
          <td><a href="./scripts/delete_user.php?userid=$user[id]">Usuń</a></td>
          <td><a href="./5_table_update_insert_delete.php?updateuserid=$user[id]">Aktualizuj</a></td>
        </tr>
E;
      }
      echo "</table>";
      if (isset($_GET['adduser'])) {
        echo '<h4>Dodawanie nowego użytkownika</h4>';
        echo <<< ADDUSER
          <form action="./scripts/add_user.php" method="post">
            <select name="city_id">
ADDUSER;
        $sql="SELECT * FROM `cities`";
        $result=$conn->query($sql);
        while ($city=$result->fetch_assoc()) {
          echo "<option value=\"$city[id]\">$city[city]</option>";
        }
        echo <<< ADDUSER
            </select><br><br>
            <input type="text" name="name" placeholder="Podaj imię"><br><br>
            <input type="text" name="surname" placeholder="Podaj nazwisko"><br><br>
            <input type="submit" value="Dodaj użytkownika"><br><br>
          </form>
ADDUSER;
      } else {
        echo '<a href="./5_table_update_insert_delete.php?adduser=1">Dodaj użytkownika</a>';
      }

      if(!empty($_GET['updateuserid'])) {
        echo "<h4>Aktualizacja użytkownika o id=$_GET[updateuserid]</h4>";
        $sql="SELECT * FROM `users` WHERE `id`=$_GET[updateuserid]";
        $result = $conn->query($sql);
        $user = $result->fetch_assoc();
        // echo "$user[city_id]";

        echo <<< UPDATEUSER
          <form action="./scripts/update_user.php" method="post">
            <select name="city_id">
UPDATEUSER;
        // $sql="SELECT * FROM `cities` WHERE `id`=$user[city_id]";
        $sql="SELECT * FROM `cities`";
        $result=$conn->query($sql);
        while ($city=$result->fetch_assoc()) {
          if($city['id'] == $user['city_id']) {
            echo "<option value=\"$city[id]\" selected>$city[city]</option>";
          } else {
            echo "<option value=\"$city[id]\">$city[city]</option>";
          }
        }
        echo <<< UPDATEUSER
            </select><br><br>
            <input type="text" name="name" value="$user[name]"><br><br>
            <input type="text" name="surname" value="$user[surname]"><br><br>
            <input type="submit" value="Aktualizuj użytkownika"><br><br>
          </form>
UPDATEUSER;

        $_SESSION['updateid'] = $user['id'];
      }
     ?>
      
  </body>
 </html>
 <!-- aoishdisa -->