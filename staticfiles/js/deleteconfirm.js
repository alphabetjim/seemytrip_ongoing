/**
 * Implement delete confirmation functionality for Trip & Traveller
 */
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButton = document.getElementById('btn-delete');
const deleteConfirm = document.getElementById("deleteConfirm");
// Delete event listener
deleteButton.addEventListener("click", (e) => {
    deleteModal.show();
});