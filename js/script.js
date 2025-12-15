// Active navigation
const links = document.querySelectorAll(".nav a");
const current = location.pathname.split("/").pop();

links.forEach(link => {
  if (link.getAttribute("href") === current) {
    link.classList.add("active");
  }
});
