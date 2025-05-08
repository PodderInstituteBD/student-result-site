 script.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const rollInput = document.querySelector('input[name="roll"]');

    form.addEventListener("submit", function (event) {
        const roll = rollInput.value.trim();

        // চেক করবো ইনপুট খালি না এবং শুধুমাত্র সংখ্যা আছে কি না
        if (roll === "" || isNaN(roll)) {
            alert("অনুগ্রহ করে একটি সঠিক রোল নাম্বার দিন (শুধু সংখ্যা)");
            event.preventDefault(); // ফর্ম সাবমিট বন্ধ করে দিবে
        }
    });
});
