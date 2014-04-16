<html>
<body>
<?php

	$address = $_POST['addr'];
	$user = $_POST['name'];

	$db = new mysqli("localhost", "snadmin", "snadmin*", "sensornetworks");

	if($db->connect_error){
		die("error");
	}
	

	
	$query_string = "INSERT INTO sp14_jyu_4920_authkeys (addr, user) values ('$address', '$user')";

	$db->query($query_string);
	
	echo "successfully added user to the list!";
	
	
	
	
	


?>
</body>
</html>