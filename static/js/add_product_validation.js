function productform_validation(){

    const product_name = document.getElementById("product_name").value;
    const product_disc = document.getElementById("product_disc").value;
    // const product_img = document.getElementById("product_img").value;
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