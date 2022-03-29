function validate(){
    const username = document.getElementById("username").value;
    const f_name = document.getElementById("f_name").value;
    const l_name = document.getElementById("l_name").value;
    const email = document.getElementById("email").value;
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    const password = document.getElementById("password").value;
    const c_password = document.getElementById("c_password").value;
    var submition = 1;

    if(username == ""){
        document.getElementById("error_username").innerHTML = "Enter you're User name.";
        submition = 0;
    }

    else if(!isNaN(username) || (!isNaN(username[0]))){
        document.getElementById("error_username").innerHTML = "First latter must be alphabet."
        submition = 0;
    }

    else{
        document.getElementById("error_username").innerHTML = "";
        submition = 1;
    }

    if(f_name == ""){
        document.getElementById("error_f_name").innerHTML = "Enter you're First name.";
        submition = 0;
    }

    else if(!isNaN(f_name) || (!isNaN(f_name[0]))){
        document.getElementById("error_f_name").innerHTML = "First latter must be alphabet."
        submition = 0;
    }

    else{
        document.getElementById("error_f_name").innerHTML = "";
        submition = 1;
    }

    if(l_name == ""){
        document.getElementById("error_l_name").innerHTML = "Enter you're Last name.";
        submition = 0;
    }

    else if(!isNaN(l_name) || (!isNaN(l_name[0]))){
        document.getElementById("error_l_name").innerHTML = "First latter must be alphabet."
        submition = 0;
    }

    else{
        document.getElementById("error_l_name").innerHTML = "";
        submition = 1;
    }


    if(email == ""){
        document.getElementById("error_email").innerHTML = "Enter your Mail ID";
        submition = 0;

    }
    else if(!isNaN(email)){
        document.getElementById("error_email").innerHTML = "Alphabests are not allowed";
        submition = 0;

    }
    else if(validRegex.test(email)==false){
        document.getElementById("error_email").innerHTML = "Enter valid email.";
        submition = 0;
    }
    else{
        document.getElementById("error_email").innerHTML = "";
        submition = 1;
    }

    if(password == ""){
        document.getElementById("error_password").innerHTML = "Enter your password.";
        submition = 0;
    }

    else if((password.length <= 6) || (password.length >= 13)){
        document.getElementById("error_password").innerHTML = "Password must be in 6 to 13 charactors.";
        submition = 0;
    }

    else{
        document.getElementById("error_password").innerHTML = "";
        submition = 1;
    }

    if(c_password == ""){
        document.getElementById("error_c_password").innerHTML = "Confirm your password."
        submition = 0;
    }

    else if(password != c_password){
        document.getElementById("error_c_password").innerHTML = "Your password doesn't match."
        submition = 0;
    }

    else{
        document.getElementById("error_c_password").innerHTML = "";
        submition = 1;
    }

    if(submition===1){
        document.getElementById("submit").innerHTML = "Submited";
        return true;
    }
    else{
        return false;
    }
}

// Log in validation

function login_validate(){

    const username = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    var submition = 1;

    if(username == ""){
        document.getElementById("username").innerHTML = "Enter you're User name.";
        submition = 0;
    }

    else if(!isNaN(username) || (!isNaN(username[0]))){
        document.getElementById("username").innerHTML = "First latter must be alphabet.";
        submition = 0;
    }

    else{
        document.getElementById("username").innerHTML = "";
        submition = 1;
    }
    
    if(password == ""){
        document.getElementById("log_password").innerHTML = "Enter you're Password.";
        submition = 0;
    }

    else{
        document.getElementById("log_password").innerHTML = "";
        submition = 1;
    }

    if(submition===1){
        return true;
    }
    else{
        return false;
    }
}

// App Product Validation

function productform_validation(){

    const product_name = document.getElementById("product_name").value;
    const product_disc = document.getElementById("product_disc").value;
    // const product_img = document.getElementById("product_img");
    const product_price = document.getElementById("product_price").value;
    var submition = 1;

    if(product_name == ""){
        document.getElementById("error_product_name").innerHTML = "Enter Product Name.";
        submition = 0;
    }

    else if(!isNaN(product_name) || (!isNaN(product_name[0]))){
        document.getElementById("error_product_name").innerHTML = "First latter must be alphabet.";
        submition = 0;
    }

    else{
        document.getElementById("error_product_name").innerHTML = "";
        submition = 1;
    }

    if(product_disc == ""){
        document.getElementById("error_product_disc").innerHTML = "Enter Product Discription.";
        submition = 0;
    }

    else{
        document.getElementById("error_product_disc").innerHTML = "";
        submition = 1;
    }

    // if(product_img == ""){
    //     document.getElementById("error_product_img").innerHTML = "Upload a Product Image.";
    //     submition = 0;
    // }

    // else{
    //     document.getElementById("error_product_img").innerHTML = "";
    //     submition = 1;
    // }

    if(product_price == ""){
        document.getElementById("error_product_price").innerHTML = "Enter Product Price.";
        submition = 0;
    }

    else if(isNaN(product_price) || (!isNaN(product_price) < 0)){
        document.getElementById("error_product_price").innerHTML = "Enter a valid Product Price.";
        submition = 0;
    }

    else{
        document.getElementById("error_product_price").innerHTML = "";
        submition = 1;
    }

    if(submition===1){
        return true;
    }
    else{
        return false;
    }

}