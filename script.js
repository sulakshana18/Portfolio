/* Typing Animation */

const text="AI & ML Developer";

let i=0;

function typing(){

if(i<text.length){

document.querySelector(".typing").innerHTML+=text.charAt(i);

i++;

setTimeout(typing,100);

}

}

typing();

/* Scroll Reveal */

window.addEventListener("scroll",()=>{

document.querySelectorAll(".reveal").forEach(el=>{

const top=el.getBoundingClientRect().top;

if(top<window.innerHeight-100){

el.classList.add("active");

}

});

});

/* AI Background */

const canvas=document.getElementById("bg");

const ctx=canvas.getContext("2d");

canvas.width=window.innerWidth;

canvas.height=window.innerHeight;

let particles=[];

for(let i=0;i<120;i++){

particles.push({

x:Math.random()*canvas.width,

y:Math.random()*canvas.height,

r:Math.random()*2

});

}

function draw(){

ctx.clearRect(0,0,canvas.width,canvas.height);

ctx.fillStyle="white";

particles.forEach(p=>{

ctx.beginPath();

ctx.arc(p.x,p.y,p.r,0,Math.PI*2);

ctx.fill();

p.y+=0.4;

if(p.y>canvas.height)p.y=0;

});

requestAnimationFrame(draw);

}

draw();

/* GitHub Projects */

fetch("https://api.github.com/users/sulakshana18/repos")

.then(res=>res.json())

.then(data=>{

const container=document.getElementById("githubProjects");

data.slice(0,4).forEach(repo=>{

container.innerHTML+=`

<div class="project-card">

<h3>${repo.name}</h3>

<p>${repo.description || "GitHub Project"}</p>

<a href="${repo.html_url}" target="_blank">View Code</a>

</div>

`;

});
function sendMessage(){

let input=document.getElementById("chatInput");

let chat=document.getElementById("chatBody");

let user=input.value;

chat.innerHTML+=`<p><b>You:</b> ${user}</p>`;

let reply="I can help you explore Sulakshana's portfolio!";

if(user.toLowerCase().includes("skills")){

reply="Skills include Java, HTML, CSS, JavaScript, MySQL.";

}

if(user.toLowerCase().includes("projects")){

reply="Projects include House Hunt, Signature Matching ML system.";

}

chat.innerHTML+=`<p><b>AI:</b> ${reply}</p>`;

input.value="";

}


});gsap.from(".hero",{

opacity:0,

y:80,

duration:1.5

});

gsap.from(".glass",{

opacity:0,

y:60,

duration:1,

stagger:0.3

});
const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(
75,
window.innerWidth / window.innerHeight,
0.1,
1000
);

const renderer = new THREE.WebGLRenderer({ alpha:true });

renderer.setSize(window.innerWidth, window.innerHeight);

document.getElementById("three-bg").appendChild(renderer.domElement);


/* Geometry */

const geometry = new THREE.SphereGeometry(0.05, 16, 16);

const material = new THREE.MeshBasicMaterial({ color:0x3b82f6 });

const particles = [];


/* Create many particles */

for(let i=0;i<500;i++){

let mesh = new THREE.Mesh(geometry, material);

mesh.position.x=(Math.random()-0.5)*10;

mesh.position.y=(Math.random()-0.5)*10;

mesh.position.z=(Math.random()-0.5)*10;

scene.add(mesh);

particles.push(mesh);

}


camera.position.z=5;


/* Animation */

function animate(){

requestAnimationFrame(animate);

particles.forEach(p=>{

p.rotation.x+=0.01;

p.rotation.y+=0.01;

});

renderer.render(scene,camera);

}

animate();
document.addEventListener("mousemove",(event)=>{

camera.position.x=(event.clientX/window.innerWidth-0.5)*2;

camera.position.y=-(event.clientY/window.innerHeight-0.5)*2;

});