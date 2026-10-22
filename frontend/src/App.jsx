import { useState } from "react";

const address = "http://localhost:8000/ask";

function App() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState("");
  const [paths, setPaths] = useState([]);
  const [thinking, setThinking] = useState(false);

  function handleTyping(event) {
    setQuestion(event.target.value);
  }
  async function answer() {
    setThinking(true);
    setPaths([]);
    try {
      const response = await fetch(address, {
        method: "POST",
        body: JSON.stringify({ question }),
        headers: { "Content-Type": "application/json" },
      });
      const data = await response.json();
      setResult(data.answer);
      setPaths(data.file_paths);
    } catch {
      setResult("The API failed. Please try again later");
    } finally {
      setThinking(false);
    }
  }

  return (
    <>
      <h1 className="text-4xl">fastapi.search</h1>
      <input value={question} onChange={handleTyping}></input>
      <button onClick={answer} disabled={thinking}>
        Send
      </button>
      <div>{thinking ? "thinking..." : result}</div>
      <ul>
        {paths.map((path) => (
          <li key={path}>{path}</li>
        ))}
      </ul>
    </>
  );
}

export default App;
