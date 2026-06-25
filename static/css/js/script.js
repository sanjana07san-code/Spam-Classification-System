// ==========================================
// Spam Classification System
// script.js
// ==========================================

// Wait until page loads
document.addEventListener("DOMContentLoaded", function () {

    // Message Textarea
    const textarea = document.querySelector("textarea");

    // Form
    const form = document.querySelector("form");

    // Predict Button
    const button = document.querySelector("button[type='submit']");

    // ===============================
    // Character Counter
    // ===============================

    if (textarea) {

        const counter = document.createElement("p");

        counter.style.textAlign = "right";
        counter.style.marginTop = "8px";
        counter.style.color = "#555";
        counter.style.fontSize = "14px";

        textarea.parentNode.appendChild(counter);

        function updateCounter() {

            counter.innerHTML =
                textarea.value.length + " characters";

        }

        textarea.addEventListener("input", updateCounter);

        updateCounter();

    }

    // ===============================
    // Auto Focus
    // ===============================

    if (textarea) {

        textarea.focus();

    }

    // ===============================
    // Loading Button
    // ===============================

    if (form) {

        form.addEventListener("submit", function () {

            if (textarea.value.trim() === "") {

                alert("Please enter a message.");

                event.preventDefault();

                return;

            }

            button.disabled = true;

            button.innerHTML =
                "Predicting...";

        });

    }

});