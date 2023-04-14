function testForm(even) {
    let errors = [];
    let success_form = [];

    let input1 = document.getElementById("fullname").value;

    if (!/^[a-z\s]+$/i.test(input1)) {
        errors.push("Only a-z and A-Z allowed");
    } else {
        let fullname = "Full name: " + input1;
        success_form.push(fullname);
    }


    // PASSWORD VALIDATION
    let password1 = document.getElementById("password1").value;
    let password2 = document.getElementById("password2").value;

    if (password1 != password2) {
        errors.push("Passwords don't match");
    }
    if (!/^(?=[\w!,.:;\-\?])[\w!,.:;\-\?]{8,20}$/.test(password1)) {
        errors.push("The password must be 8-20 characters long. It can contain uppercase and lowercase letters from a-z, numbers, and the following characters: ,.-:;?!")
    }
    
    if (password1 == password2 && (/^(?=[\w!,.:;\-\?])[\w!,.:;\-\?]{8,20}$/.test(password1))) {
        let correct_password = "Password1: " + password1;
        let correct_password2 = "Password2: " + password2;
        success_form.push(correct_password, correct_password2)
    }


     // GENDER 
     if (! (document.getElementById("gender_male").checked || document.getElementById("gender_female").checked || document.getElementById("gender_other").checked)) {
        errors.push("You must choose a gender");
    }

    if (document.getElementById("gender_male").checked) {
        let gender = "Gender: male";
        success_form.push(gender)
    }

    if (document.getElementById("gender_female").checked) {
        let gender = "Gender: female";
        success_form.push(gender)
    }

    if (document.getElementById("gender_other").checked) {
        let gender = "Gender: other";
        success_form.push(gender)
    }
    
    // HOBBIES
    var hobbies = ["games", "music", "sports", "TV"];
    var myHobbies = [];
    
    for (let choice of document.getElementsByName("hobby")) {
        if (choice.checked && hobbies.findIndex((x) => x == choice.value) != -1) {
            myHobbies.push(choice.value);
        }
    }
    if (myHobbies.length) {
        result_hobbies = `Your hobbies are: ${myHobbies.join(", ")}`;
        success_form.push(result_hobbies);
    } else {
        result_hobbies = "You have no hobbies";
        success_form.push(result_hobbies);
    }


    // BIRTHDAY
    let birthday_value = document.getElementById("birthday").value;
    let birthday = "Birthday: " + birthday_value;
    success_form.push(birthday);


    // HEIGHT
    let height_value = document.getElementById("id_number_output").value;
    let height = "Height: " + height_value + " cm";
    success_form.push(height);


    // COLOR
    let color_value = document.getElementById("color").value;
    let color = "Favorite color: " + color_value;
    success_form.push(color);
    

    // COUNTRY
    let country_value = document.getElementById("country").value;
    let country = "Country: " + country_value;
    success_form.push(country);


    // PROFESSION
    let profession_value = document.getElementById("profession").value;
    let profession = "Profession: " + profession_value;
    success_form.push(profession);


    // MESSAGE  
    // let message_value = document.getElementById("id_message").value;
    // let message = "Message: " + message_value;
    // success_form.push(message);
    let textarea = document.getElementById("id_textarea").value;
    document.getElementById("result").innerText = `textarea =\n${textarea}`;
    
    // RESULTS
    let result = document.getElementById("id_result");
    let result2 = document.getElementById("id_success");

    if (errors.length > 0) {
        result.style.color = "red";
        result.innerHTML = errors.join("<br>");
    } else {
        result.style.color = "green";
        result.innerText = "Success!";
    }

    if (errors.length === 0)  {
        result2.innerHTML = success_form.join("<br>");
    }

    event.preventDefault();
}