const deleteCourseBtns = document.querySelectorAll("#deleteCourseBtn");
const courseDeleteModals = document.querySelectorAll("#courseDeleteModal");
console.log(deleteCourseBtns);

deleteCourseBtns.forEach((btn, i) => {
  btn.addEventListener("click", (e) => {
    console.log(e);
    console.log(i, "i=============");

    courseDeleteModals[i].style.display = "block";
    courseDeleteModals[i].classList.remove("hidden");
  });
});
