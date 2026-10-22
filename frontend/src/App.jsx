import { useState } from "react";
import Markdown from "react-markdown";

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
    <div className="max-w-2xl mx-auto flex flex-col gap-4 p-4">
      <h1 className="text-4xl text-center">fastapi.search</h1>
      <div className="flex gap-2">
        <input
          value={question}
          onChange={handleTyping}
          className="border rounded-lg p-2 flex-1"
        ></input>
        <button
          onClick={answer}
          disabled={thinking}
          className="disabled:opacity-50 bg-green-600 text-white px-4 rounded-lg"
        >
          Send
        </button>
      </div>
      <div className="prose">
        <Markdown>{thinking ? "thinking..." : result}</Markdown>
      </div>
      {paths.length > 0 && (
        <div>
          <h2 className="font-semibold">Sources:</h2>
          <ul className="marker:text-green-600 list-disc pl-5">
            {paths.map((path) => (
              <li key={path}>{path}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
