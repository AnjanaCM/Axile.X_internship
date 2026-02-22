// 1️⃣ Alert
function showAlert() {
  alert("Button was clicked successfully!");
}

// 2️⃣ Form Validation
function validateForm() {
  let name = document.getElementById("name").value;
  let email = document.getElementById("email").value;

  if (name === "" || email === "") {
    alert("All fields are required!");
    return false;
  }

  if (!email.includes("@")) {
    alert("Enter a valid email!");
    return false;
  }

  alert("Form submitted successfully!");
  return true;
}

// 3️⃣ Calculator
function calculate() {
  let num1 = parseFloat(document.getElementById("num1").value);
  let num2 = parseFloat(document.getElementById("num2").value);
  let operator = document.getElementById("operator").value;
  let result;

  if (isNaN(num1) || isNaN(num2)) {
    document.getElementById("result").innerText = "Enter valid numbers!";
    return;
  }

  switch(operator) {
    case "+": result = num1 + num2; break;
    case "-": result = num1 - num2; break;
    case "*": result = num1 * num2; break;
    case "/":
      if (num2 === 0) {
        document.getElementById("result").innerText = "Cannot divide by zero!";
        return;
      }
      result = num1 / num2;
      break;
  }

  document.getElementById("result").innerText = "Result: " + result;
}

// 4️⃣ Change Text
function changeText() {
  document.getElementById("changeText").innerText =
    "The text has been changed successfully!";
}