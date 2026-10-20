console.log("app.js is connected");

const address = "http://localhost:8000/ask"

const button = document.getElementById("send-button");
const ask = document.getElementById("question");
const answer = document.getElementById("answer-div")

console.log(button)

button.addEventListener("click", async function () {
    const response = await fetch(address, {
        method: "POST",
        body: JSON.stringify({question: ask.value}),
        headers: {"Content-Type": "application/json"},  
    })
})

