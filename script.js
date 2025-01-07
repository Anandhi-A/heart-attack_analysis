document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    
    // Display a confirmation message before form submission
    form.addEventListener('submit', (event) => {
        event.preventDefault();  // Prevents form submission for demonstration
        const confirmation = confirm('Are you sure you want to submit your data for prediction?');
        if (confirmation) {
            form.submit();  // Submit the form if confirmed
        }
    });
});
