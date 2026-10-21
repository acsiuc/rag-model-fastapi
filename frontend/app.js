console.log("app.js is connected");

const address = "http://localhost:8000/ask"

const button = document.getElementById("send-button");
const ask = document.getElementById("question");
const answer = document.getElementById("answer-div")
const paths = document.getElementById("paths-list")

console.log(button)

button.addEventListener("click", async function(){
    answer.textContent = "thinking..."
    paths.textContent = ""
    const response = await fetch(address,{
        method: "POST",
        body: JSON.stringify({question: ask.value}),
        headers: {"Content-Type": "application/json"}
    })
    const data = await response.json()
    answer.textContent = data.answer
    
    for (const path of data.file_paths) {
        const bulletPath = document.createElement("li")
        bulletPath.textContent = path
        paths.appendChild(bulletPath)
    }
})