<?php
    function set_message($connection) {
        //checks to make sure that submit button is submited before code is run
        if (isset($_POST['message_submit'])) {

            $id = $_POST['id'];
            $date = $_POST['date'];
            $message = $_POST['message'];

            $sql = "INSERT INTO comments (id, date, comment) VALUES ('$id', '$date', '$message')";
            $result = mysqli_stmt_init($connection);
            mysqli_stmt_bind_param($result, "sss", $id, $date, $message);
            mysqli_close($connection);

        }
    }
?>