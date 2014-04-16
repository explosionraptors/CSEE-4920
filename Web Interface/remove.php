<html>
<body>
<?php

	$address = $_POST['addr'];
	$user = $_POST['name'];

	$db = new mysqli("localhost", "snadmin", "snadmin*", "sensornetworks");

	if($db->connect_error){
		die("error");
	}
	
	
	$query_string1 = "delete from sp14_jyu_4920_authkeys where addr = '$address'";
	$query_string2 = "delete from sp14_jyu_4920_authkeys where user = '$user'";

	$db->query($query_string1);
	$db->query($query_string2);
	echo "successfully removed user from the list!";
	
	
	
	
	


?>
</body>
</html>