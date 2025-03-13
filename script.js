document.addEventListener("DOMContentLoaded", function () {
    
    // Contact Form Validation
    if (document.getElementById("contactForm")) {
        document.getElementById("contactForm").addEventListener("submit", function (e) {
            e.preventDefault();
            Swal.fire("Thank You!", "Thanks for contacting us! We'll get back to you soon.", "success");
            this.reset();
        });
    }

    // Registration Form Validation
    document.addEventListener("DOMContentLoaded", function () {
        console.log("DOM Fully Loaded!");
    
        let registerForm = document.getElementById("registerForm");
    
        if (!registerForm) {
            console.error("Form not found!");
            return;
        }
    
        registerForm.addEventListener("submit", function (event) {
            event.preventDefault(); 
            console.log("Submit button clicked!"); 
    
            Swal.fire("Success!", "Registration Successful!", "success");
        });
    });    
    
    // Login Form Validation
    if (document.getElementById("loginForm")) {
        document.getElementById("loginForm").addEventListener("submit", function (e) {
            e.preventDefault();
            Swal.fire("Success", "Login Successful!", "success");
            this.reset();
        });
    }

});
