<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guestbook</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .entry { border-bottom: 1px solid #ddd; padding: 10px 0; }
    </style>
</head>
<body>
    <h1>Guestbook</h1>
    <form action="guestbook.php" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Sign</button>
    </form>
    <h2>Entries</h2>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = htmlspecialchars($_POST["name"]);
        $message = htmlspecialchars($_POST["message"]);
        $entry = "$name: $message\n";
        file_put_contents("guestbook.txt", $entry, FILE_APPEND);
    }

    if (file_exists("guestbook.txt")) {
        $entries = file("guestbook.txt", FILE_IGNORE_NEW_LINES);
        foreach ($entries as $entry) {
            echo "<div class=\"entry\">" . htmlspecialchars($entry) . "</div>";
        }
    }
    ?>
</body>
</html>
