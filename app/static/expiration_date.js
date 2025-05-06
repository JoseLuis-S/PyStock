/**
 * Set the expiration date input to have today's date as the minimum.
 * This prevents selecting past dates.
 */
document.addEventListener("DOMContentLoaded", () => {
    const expirationInput = document.getElementById("expiration_date");
    const today = new Date().toISOString().split("T")[0];
    expirationInput.min = today;
    expirationInput.value = today;
});