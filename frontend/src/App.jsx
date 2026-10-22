import "./App.css";
import { useState } from "react";

const address = "http://localhost:8000/ask";

function App() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState('');
  const [paths, setPaths] = useState([]);

  function handleTyping(event) {
    setQuestion(event.target.value);
  }
  async function answer() {
    const response = await fetch(address, {
      method: "POST",
      body: JSON.stringify({ question }),
      headers: { "Content-Type": "application/json" },
    });
    const data = await response.json();
    setResult(data.answer)
    setPaths(data.file_paths)
    console.log(data);
  }

  return (
    <>
      <h1>fastapi.search</h1>
      <input value={question} onChange={handleTyping}></input>
      <button onClick={answer}>Send</button>
      <div>{result}</div>
      <ul>
        {paths.map((path) => <li key={path}>{path}</li>)}
      </ul>
    </>
  );
}

export default App;
