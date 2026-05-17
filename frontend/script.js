console.log("Portfolio Website Running");

fetch("https://personal-portfolio-website-vulz.onrender.com/projects")
.then(response => response.json())
.then(data => {

    let projectDiv = document.getElementById("projects");

    projectDiv.innerHTML = "";

    data.forEach(project => {

        projectDiv.innerHTML += `
            <div class="project-card">
                <h3>${project.title}</h3>
                <p>${project.description}</p>
            </div>
        `;
    });

});