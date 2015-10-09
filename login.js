function clicked() {
    
    var user = document.getElementById('username');
    var pass = document.getElementById('password');
    
    
    var coruser = 'tester';
    var corpass = '123';
    
    if (user.value == coruser) {
        if (pass.value == corpass) {
            window.alert("You are looged in as " + user.value);
        } else {
            window.alert("Incorect username or password");
        }
    }
}