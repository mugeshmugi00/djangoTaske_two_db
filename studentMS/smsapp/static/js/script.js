const deleteCourseBtns = document.querySelectorAll(".deleteCourseBtn"); 
const courseDeleteModals = document.querySelectorAll(".courseDeleteModal");

deleteCourseBtns.forEach((btn, i) => {
  btn.addEventListener("click", () => {
    courseDeleteModals[i].style.display = "flex";
  });
});

function closePopup(event) {
  event.target.closest(".courseDeleteModal").style.display = "none";
}

// student
const studentDeleteModals = document.querySelectorAll(".studentDeleteModal")
const deleteStudentBtns = document.querySelectorAll(".deleteCourseBtn")


deleteStudentBtns.forEach((btn, i) => {
  btn.addEventListener("click", () => {
    studentDeleteModals[i].style.display = "flex";
  });
});

function closePopup(event) {
  event.target.closest(".studentDeleteModal").style.display = "none";
}
