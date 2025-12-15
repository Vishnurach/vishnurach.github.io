
const ham=document.getElementById("hamburger");
const nav=document.getElementById("navMenu");
if(ham){
  ham.onclick=()=>nav.classList.toggle("open");
}
